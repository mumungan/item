from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from .. import db
from ..forms import WriteinfoForm
from ..models import Farminfo, Writeinfo
from .auth_views import login_required

bp = Blueprint('writeinfo', __name__, url_prefix='/writeinfo')


@bp.route('/create/<int:farminfo_id>', methods=('POST',))
@login_required
def create(farminfo_id):
    form = WriteinfoForm()
    farminfo = Farminfo.query.get_or_404(farminfo_id)
    if form.validate_on_submit():
        content = request.form['content']
        writeinfo = Writeinfo(content=content, create_date=datetime.now(), user=g.user)
        farminfo.writeinfo_set.append(writeinfo)
        db.session.commit()
        return redirect(url_for('farminfo.detail', farminfo_id=farminfo_id))
    return render_template('farminfo/farminfo_detail.html', farminfo=farminfo, form=form)

@bp.route('/modify/<int:writeinfo_id>', methods=('GET', 'POST'))
@login_required
def modify(writeinfo_id):
    writeinfo = Writeinfo.query.get_or_404(writeinfo_id)
    if g.user != writeinfo.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('farminfo.detail', farminfo_id=writeinfo.farminfo.id))
    if request.method == "POST":
        form = WriteinfoForm()
        if form.validate_on_submit():
            form.populate_obj(writeinfo)
            writeinfo.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('farminfo.detail', farminfo_id=writeinfo.farminfo.id))
    else:
        form = WriteinfoForm(obj=writeinfo)
    return render_template('writeinfo/writeinfo_form.html', form=form)

@bp.route('/delete/<int:writeinfo_id>')
@login_required
def delete(writeinfo_id):
    writeinfo = Writeinfo.query.get_or_404(writeinfo_id)
    farminfo_id = writeinfo.farminfo.id
    if g.user != writeinfo.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(writeinfo)
        db.session.commit()
    return redirect(url_for('farminfo.detail', farminfo_id=farminfo_id))    