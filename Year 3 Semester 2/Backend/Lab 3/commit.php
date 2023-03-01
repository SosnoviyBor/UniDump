<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        require_once "connection.php";
        // Read common POST data
        $mode = $_POST["mode"];
        $table = $_POST["table"];
        $skipped_keys = ["mode","id","table"];
        // echo '<pre>'; print_r($_POST); echo '</pre>';

        if ($mode === "edit") {
            // Prepare data for SQL query
            $data = "";
            foreach ($_POST as $k => $v) {
                if (in_array($k, $skipped_keys)) { continue; }

                if (is_numeric($v)) {
                    $data = $data . "$k = $v,";
                } else {
                    $data = $data . "$k = '$v',";
                }
            }
            $data = rtrim($data, ",");
    
            // Commit query
            $id = $_POST["id"];
            $sql = "UPDATE $table SET $data WHERE id=$id";
            mysqli_query($conn, $sql);
        } else if ($mode === "new") {
            // Prepare data for SQL query
            $columns = "";
            $values = "";
            foreach ($_POST as $k => $v) {
                if (in_array($k, $skipped_keys)) { continue; }

                $columns = $columns . "$k,";
                if (is_numeric($v)) {
                    $values = $values . "$v,";
                } else {
                    $values = $values . "'$v',";
                }
            }
            $columns = rtrim($columns, ",");
            $values = rtrim($values, ",");
    
            // Commit query
            $sql = "INSERT INTO $table ($columns) VALUES ($values)";
            mysqli_query($conn, $sql);
        } else if ($mode === "delete") {
            // Delete by id
            $id = $_POST["id"];
            $sql = "DELETE FROM $table WHERE id=$id";
            mysqli_query($conn, $sql);
        } else {
            echo "Непідтримуваний режим роботи файлу '$mode'";
            die;
        }
    }

    header("Location: /table.php?table=$table");
    die();
?>