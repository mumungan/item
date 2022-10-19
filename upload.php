<?php
include("menunav.php")
?>
<form enctype="multipart/form-data" action="filerecption.php" method="POST">
   <input type="hidden" name="MAX_FILE_SIZE" value="30000" />
   <input name="userfile" type="file" />
   <input type="submit" value="upload" />
</form>
<?php
include("menufoot.php");
 ?>
