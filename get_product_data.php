<?php
// Enable CORS (adjust this based on your requirements)
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

// Establish a connection to the SQLite database
$pdo = new PDO('sqlite:D:/VisualStudioCodeProjects/ScaleUpCaseStudyWebsite/Website/products.db');

// Perform SQL query to get data
$query = "SELECT * FROM products";
$result = $pdo->query($query);

// Fetch data as an associative array
$data = $result->fetchAll(PDO::FETCH_ASSOC);

// Convert data to JSON format
$jsonData = json_encode($data);

// Return JSON response
echo $jsonData;
?>
