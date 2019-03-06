<!DOCTYPE html>

<?php 
	if(isset($_GET['name']) && !empty($_GET['name']))
		$name = $_GET["name"];
	else
		$name = "";
?>

<html lang="en">
	<body>
		<?php if($name == ""): ?>
			<h1> Hello guest! Enter your name </h1>
		<?php else:?>
			<h1> Hello <?php echo $name;?>!</h1>
		<?php endif;?>
		<form action="xss.php" method="GET">
			<input type="text" name="name"/>
			<input type="submit"/>
		</form>
		<?php if($name != ""): ?>
			<h1> This is what was inserted: </h1>
			<p> Hello <?php echo htmlspecialchars($name);?>!</p>
		<?php endif;?>
	</body>
</html>