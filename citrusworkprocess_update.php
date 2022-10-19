<?php
include("menunav.php");
$conn = mysqli_connect('localhost', 'root', 'stone246', 'citrusworkpesticide');
settype($_POST['id'], 'integer');
$filtered = array(
    'id'=>mysqli_real_escape_string($conn, $_POST['id']),
    'wdate'=>mysqli_real_escape_string($conn, $_POST['wdate']),
    'work'=>mysqli_real_escape_string($conn, $_POST['work']),
    'pesticide'=>mysqli_real_escape_string($conn, $_POST['pesticide'])
  );
$sql = "
  UPDATE citruswork
    SET
      wdate = '{$filtered['wdate']}',
      work = '{$filtered['work']}',
      pesticide = '{$filtered['pesticide']}'
    WHERE
      id = {$filtered['id']}
";
$result = mysqli_query($conn, $sql);
if($result === false){
  echo '저장하는 과정에서 문제가 생겼습니다';
  error_log(mysqli_error($conn));
} else {
  echo '성공했습니다. <a href="citruswork.php">돌아가기</a>';
}
include("menufoot.php");
?>
