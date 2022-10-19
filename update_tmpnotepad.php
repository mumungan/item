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
if(isset($_GET['id'])) {
  $filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
  $sql = "SELECT * FROM topic WHERE id={$filtered_id}";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_array($result);
  $article['title'] = htmlspecialchars($row['title']);
  $article['description'] = htmlspecialchars($row['description']);

  $update_tmpnotepad = '<a href="update_tmpnotepad.php?id='.$_GET['id'].'">수정</a>';
}
?>
      <article>
        <h1>메모장</h1>
        <ol>
          <?=$list?>
        </ol>
  <form action="update_tmpnotepadprocess.php" method="POST">
    <input type="hidden" name="id" value="<?=$_GET['id']?>">
    <p>제목:<input type="text" name="title" placeholder="제목을 입력하세요" value="<?=$article['title']?>"></p>
    <p>내용:
      <textarea name="description" rows="10" cols="80" placeholder="본문을 입력하세요"><?=$article['description']?></textarea>
    </p>
    <p><input type="submit"></p>
  </form>
</article>
<?php include("menufoot.php");?>
