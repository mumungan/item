<?php
include("menunav.php");
$conn = mysqli_connect('localhost', 'root', 'stone246', 'tmpnotepad');
$sql = "SELECT * FROM topic";
$result = mysqli_query($conn, $sql);
$list = '';
while($row = mysqli_fetch_array($result)) {
  $escaped_title = htmlspecialchars($row['title']);
  $list = $list."<li><a href=\"tmpnotepad.php?id={$row['id']}\">{$escaped_title}</a></li>";
}

$article = array(
  'title'=>'',
  'description'=>''
);
$update_tmpnotepad = '';
$delete_tmpnotepad = '';

if(isset($_GET['id'])) {
  $filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
  $sql = "SELECT * FROM topic WHERE id={$filtered_id}";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_array($result);
  $article['title'] = htmlspecialchars($row['title']);
  $article['description'] = htmlspecialchars($row['description']);

  $update_tmpnotepad = '<a href="update_tmpnotepad.php?id='.$_GET['id'].'">수정</a>';
  $delete_tmpnotepad = '
    <form action="delete_tmpnotepadprocess.php" method="post">
      <input type="hidden" name="id" value="'.$_GET['id'].'">
      <input type="submit" value="delete">
    </form>
  ';
}
?>
      <article>
        <h1>메모장</h1>
        <ol>
          <?=$list?>
        </ol>
        <a href="create_tmpnotepad.php">쓰기</a>
        <?=$update_tmpnotepad?>
        <?=$delete_tmpnotepad?>
        <h2><?=$article['title']?></h2>
        <?=$article['description']?>
      </article>
<?php include("menufoot.php");?>
