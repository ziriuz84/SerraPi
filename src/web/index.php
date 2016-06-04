<html>
<head>
<title>Serra web</title>
</head>
<body>
<?php
$servername = "localhost";
$username = "testuser";
$password = "test123";
$dbname = "testdb";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
} 
$sql = "SELECT * FROM TRHInt";
$result = $conn->query($sql);
if ($result->num_rows > 0){
	while ($row = $result->fetch_assoc()){
		echo $row['Time']. " | ".$row['T']." °C | ".$row['RH']."% <br />";
	}
} else {
	echo "0 results";
}
$conn->close();
?>
</body>
</html>
