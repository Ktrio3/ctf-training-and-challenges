<!DOCTYPE html>

<?php
// require("flag.txt") is easiest way, but you can do more complicated stuff :)
// 1; $f = fopen("flag.txt", "r"); echo fread($f,filesize("flag.txt")); fclose($f)
if( isset($_POST["equation"]) )
{
  eval("\$a = " . $_POST["equation"] . ";");
}
else
{
  $a = "";
}
?>

<html>
<body>
  <form action="inject.php" method="post">
    <p> Want to do some math? Enter an equation!</p>
    <textarea name="equation"></textarea><br/><br/>
    <input type="submit" value="Submit">
  </form>
  <br/>
  <?php print_r($a);?>
</body>
</html>
