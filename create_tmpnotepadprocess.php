<?php
include("menunav.php");
$conn = mysqli_connect('localhost', 'root', 'stone246', 'tmpnotepad');
$filtered = array(
    'title'=>mysqli_real_escape_string($conn, $_POST['title']),
    'description'=>mysqli_real_escape_string($conn, $_POST['description'])
  );
$sql = "
  INSERT INTO topic
    (title, description, created)
    VALUES(
        '{$filtered['title']}',
        '{$filtered['description']}',
        NOW()
    )
";
$result = mysqli_query($conn, $sql);
if($result === false){
  echo '저장하는 과정에서 문제가 생겼습니다';
  error_log(mysqli_error($conn));
} else {
  echo '성공했습니다. <a href="tmpnotepad.php">돌아가기</a>';
}
include("menufoot.php");
?>
