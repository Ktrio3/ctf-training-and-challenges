<!DOCTYPE html>

<?php 
	$servername = "localhost";
	$username = "demo";
	$password = "demo";
	$dbname = "demo";
	mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);

	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 

	$query = "";
	$result = "";
	if(isset($_GET['user']) && !empty($_GET['user']))
	{	
		$pass = '';
		if(isset($_GET['pass']) && !empty($_GET['pass']))
		{
			$pass = $_GET['pass'];
		}
		$query = "SELECT * FROM Users2 WHERE User = '" . $_GET['user'];
		$query .= "' AND Password = '" . $pass . "'";
		try{
			$result = $conn->query($query);
		} catch (Exception $e) {
			echo 'Caught exception: ',  $e->getMessage(), "\n";
		}
		
	}
	$conn->close();
?>

<html lang="en">
	<body>
		<?php 
			if ($result != '' && $result->num_rows > 0) {
				// output data of each row
				$row = $result->fetch_assoc();
				echo "<h1>Logged in as: " . $row['User'] . "</h1>";
				echo $row['Password'];
			} else if($result != '' && isset($_GET['user']) && !empty($_GET['user']))			
			{
				echo '<h1>Failed login</h1>';
			}
		?>
		<form action="sql.php" method="GET">
			<label>Username: <input type="text" name="user"/></label><br/>
			<label>Password: <input type="text" name="pass"/></label>
			<input type="submit"/>
		</form>
		<?php if($query != ""): ?>
			<h1> This is the query that was ran: </h1>
			<p><?php echo $query;?>!</p>
		<?php endif;?>
	</body>
</html>