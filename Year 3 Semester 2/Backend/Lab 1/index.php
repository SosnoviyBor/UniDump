<!DOCTYPE html>

<html>
  <head>
    <meta charset="UTF-8">
    <title>Lab #1</title>
  </head>
  <body>

    <h1>Hello world!</h1>

    <?php
    include "secrets.php";
    
    // Create the new database
    // This section of code made only for demonstration purposes and not intended to be run
    // $conn = new mysqli($servername, $username, $password);
    // if ($conn->connect_error) {
    //   die("Connection failed: " . $conn->connect_error);
    // }
    // echo "Connected successfully";

    // // Create database
    // $sql = "CREATE DATABASE $database";
    // if ($conn->query($sql) === TRUE) {
    //   echo "Database created successfully";
    // } else {
    //   echo "An error occured" . $conn->error;
    // }
    // $conn->close();
    
    // Connect to the specific database
    $conn = new mysqli($servername, $username, $password, $database);
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }
    echo "Connected successfully";

    // Спроектувати структуру бази даних оголошень про квартири:
    // вид оголошення (здам / продам / зніму / куплю), адреса, кількість кімнат, дата, ціна.
    // Create new table 1
    $sql = "CREATE TABLE ad (
      id int,
      status_id int,
      adress varchar(511),
      rooms int,
      publication_date datetime DEFAULT CURRENT_TIMESTAMP,
      last_update_date datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      cost_hrn int,
      PRIMARY KEY (id)
    )";
    if ($conn->query($sql) === TRUE) {
      echo "Database created successfully";
    } else {
      echo "An error occured" . $conn->error;
    }

    // Create new table 2
    $sql = "CREATE TABLE statuses (
      id int,
      val varchar(100),
      PRIMARY KEY (id)
    )";
    if ($conn->query($sql) === TRUE) {
      echo "Database created successfully";
    } else {
      echo "An error occured" . $conn->error;
    }
    
    $conn->close();
    ?>

  </body>
</html>