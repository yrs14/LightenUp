<?php
    
    $height = $_POST['height'];
    $weight = $_POST['weight'];
    $age = $_POST['age'];
    $gender = $_POST['gender'];
    
    $info = mysqli_connect("localhost", "root", "abc123", "lightenUp");
    $query = "INSERT INTO data (height, weight, age, gender) VALUES ('$height', '$weight', '$age', '$gender')";


?>

