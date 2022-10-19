<?php
include("menunav.php");
$conn = mysqli_connect('localhost', 'root', 'stone246', 'citrusworkpesticide');
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>감귤 작업일지</title>
  </head>
  <body>
    <h1>감귤 작업일지</h1>
    <table border="2">
      <thead>
        <tr> <th>ID</th> <th>날짜</th> <th>작업내용</th> <th>농약명</th> <th>수정</th> <th>삭제</th> </tr>
      </thead>
      <tbody>
        <?php
        $sql = "SELECT * FROM citruswork";
        $result = mysqli_query($conn, $sql);
        while($row = mysqli_fetch_array($result)){
          $filtered = array(
            'id'=>htmlspecialchars($row['id']),
            'wdate'=>htmlspecialchars($row['wdate']),
            'work'=>htmlspecialchars($row['work']),
            'pesticide'=>htmlspecialchars($row['pesticide'])
          );
          ?>
          <tr>
            <td><?=$filtered['id']?></td>
            <td><?=$filtered['wdate']?></td>
            <td><?=$filtered['work']?></td>
            <td><?=$filtered['pesticide']?></td>
            <td><a href="citruswork.php?id=<?=$filtered['id']?>">수정</a></td>
            <td>
              <form  action="citrusworkprocess_delete.php" method="post" onsubmit="if(!confirm('정말로 삭제하시겠습니까?')){return false;}">
                <input type="hidden" name="id" value="<?=$filtered['id']?>">
                <input type="submit" value="삭제">
              </form>
            </td>
          </tr>
          <?php
        }
        ?>
      </table>
        <?php
          $article = array(
            'wdate'=>'',
            'work'=>'',
            'pesticide'=>''
          );
          $label_submit = '작성';
          $form_action = 'citrusworkprocess_create.php';
          $form_id = '';
          if(isset($_GET['id'])) {
            $filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
            settype($filtered_id, 'integer');
            $sql = "SELECT * FROM citruswork WHERE id={$filtered_id}";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_array($result);
            $article['wdate'] = htmlspecialchars($row['wdate']);
            $article['work'] = htmlspecialchars($row['work']);
            $article['pesticide'] = htmlspecialchars($row['pesticide']);
            $label_submit = '수정';
            $form_action = 'citrusworkprocess_update.php';
            $form_id = '<input type="hidden" name="id" value="'.$_GET['id'].'">';
           }
        ?>
    <form action="<?=$form_action?>" method="POST">
      <?=$form_id?>
      <p><input type="date" name="wdate" value="<?=$article['wdate']?>"></p>
      <p><input type="text" name="work" placeholder="작업한 내용을 입력하세요" value="<?=$article['work']?>"></p>
      <p><input type="text" name="pesticide" placeholder="농약명을 입력하세요" value="<?=$article['pesticide']?>"></p>
      <p><input type="submit" value="<?=$label_submit?>"></p>
    </form>
  </body>
</html>
