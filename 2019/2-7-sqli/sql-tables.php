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

	$user = "";
	if(isset($_GET['user']) && !empty($_GET['user']))
	{	
		$user = $_GET['user'];
	
		
	}
	$query = "SELECT * FROM Users WHERE User LIKE '%" . $user ."%'";

	try
	{
		$result = $conn->query($query);
	} catch (Exception $e) {
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}

	$conn->close();
?>

<html lang="en">
	<body>
		<?php 
			if ($result->num_rows > 0) {
				// output data of each row
				 while($row = $result->fetch_assoc()) {
					echo "id: " . $row["ID"]. " - Name: " . $row["User"]. "<br>";
				}
				echo "<br/>";
			}
		?>
		<form action="sql-tables.php" method="GET">
			<label>Username: <input type="text" name="user"/></label><br/>
			<input type="submit"/>
		</form>
		<?php if($query != ""): ?>
			<h1> This is the query that was ran: </h1>
			<p><?php echo $query;?>!</p>
		<?php endif;?>
	</body>
</html>