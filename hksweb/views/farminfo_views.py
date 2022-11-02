from flask import Blueprint, render_template, request, url_for, g, flash
from datetime import datetime
from werkzeug.utils import redirect

from .. import db
from ..models import Farminfo
from ..forms import FarminfoForm, WriteinfoForm
from ..views.auth_views import login_required

bp = Blueprint('farminfo', __name__, url_prefix='/farminfo')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    farminfo_list = Farminfo.query.order_by(Farminfo.create_date.desc())
    farminfo_list = farminfo_list.paginate(page=page, per_page=10)
    return render_template('farminfo/farminfo_list.html', farminfo_list=farminfo_list)


@bp.route('/detail/<int:farminfo_id>/')
def detail(farminfo_id):
    form = WriteinfoForm()
    farminfo = Farminfo.query.get_or_404(farminfo_id)
    return render_template('farminfo/farminfo_detail.html', farminfo=farminfo, form=form) 

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = FarminfoForm()
    if request.method == 'POST' and form.validate_on_submit():
        farminfo = Farminfo(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(farminfo)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('farminfo/farminfo_form.html', form=form)  

@bp.route('/modify/<int:farminfo_id>', methods=('GET', 'POST'))
@login_required
def modify(farminfo_id):
    farminfo = Farminfo.query.get_or_404(farminfo_id)
    if g.user != farminfo.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('farminfo.detail', farminfo_id=farminfo_id))
    if request.method == 'POST':  # POST 요청
        form = FarminfoForm()
        if form.validate_on_submit():
            form.populate_obj(farminfo)
            farminfo.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('farminfo.detail', farminfo_id=farminfo_id))
    else:  # GET 요청
        form = FarminfoForm(obj=farminfo)
    return render_template('farminfo/farminfo_form.html', form=form)      

@bp.route('/delete/<int:farminfo_id>')
@login_required
def delete(farminfo_id):
    farminfo = Farminfo.query.get_or_404(farminfo_id)
    if g.user != farminfo.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('farminfo.detail', farminfo_id=farminfo_id))
    db.session.delete(farminfo)
    db.session.commit()
    return redirect(url_for('farminfo._list'))    