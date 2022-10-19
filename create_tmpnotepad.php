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
?>
      <article>
        <h1>메모장</h1>
        <ol>
          <?=$list?>
        </ol>
  <form action="create_tmpnotepadprocess.php" method="POST">
    <p>제목:<input type="text" name="title" placeholder="제목을 입력하세요"></p>
    <p>내용:
      <textarea name="description" rows="10" cols="80" placeholder="본문을 입력하세요"></textarea>
    </p>
    <p><input type="submit"></p>
  </form>
</article>
<?php include("menufoot.php");?>
