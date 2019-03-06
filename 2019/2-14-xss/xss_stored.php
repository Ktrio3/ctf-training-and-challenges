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

	if(isset($_POST['cookie']) && !empty($_POST['cookie']))
	{
		$cookie = $_POST['cookie'];
		setcookie("TestCookie", $cookie);
	}

	$user = "";
	if(isset($_POST['user']) && !empty($_POST['user']))
	{	
		$user = $_POST['user'];
		if(isset($_POST['comment']) && !empty($_POST['comment']))
		{	
			$comment = $_POST['comment'];

			$query = "INSERT INTO comments (Comment, User, Time) VALUES ('" . $comment . "', '" . $user . "', NOW())";
			try
			{
				$result = $conn->query($query);
			} catch (Exception $e) {
				echo 'Caught exception: ',  $e->getMessage(), "\n";
			}
		}	
	}

	$query = "SELECT * FROM comments ORDER BY Time";

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
		<form action="xss_stored.php" method="POST">
			<label>Username: <input type="text" name="user"/></label><br/>
			<label>Comment: <textarea  name="comment"> </textarea></label><br/>
			<input type="submit"/><br/>
		</form>
		<form action="xss_stored.php" method="POST">
			<label>Set a secret cookie: <input type="text" name="cookie"/></label><br/>
			<input type="submit"/><br/>
		</form>
		<?php 
			if ($result->num_rows > 0) {
				// output data of each row
				 while($row = $result->fetch_assoc()) {
					echo "<strong>" . $row["Time"]. "&mdash;User </strong>" . $row["User"]. "<strong> commented: </strong>"; 
					echo $row["Comment"]. "<br>\n";
				}
				echo "<br/>";
			}
		?>
	</body>
</html>