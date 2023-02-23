<!DOCTYPE html>

<html>
<head>
    <meta charset="UTF-8">
    <title>Lab #2 | List</title>
    <link rel="stylesheet" href="styles.css">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <?php
    require_once "connection.php";
    ?>

    <div id="wrapper">
        <a href="index.php">На головну</a>

        <?php
        $url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
        $url_components = parse_url($url);
        parse_str($url_components['query'], $params);
        $table = $params["table"];
        $row_id = $params["id"];

        echo "Редагування рядку в таблиці '$table'<br>";

        $sql = "SELECT * FROM $table WHERE id=$row_id";
        $data = mysqli_fetch_row(mysqli_query($conn, $sql));
        $sql = "SELECT COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = 'backend_labs' AND TABLE_NAME = '$table'";
        $columns = mysqli_fetch_all(mysqli_query($conn, $sql));
        
        $fk = null;
        foreach (range(0,sizeof($data)-1) as $i) {
            $k = $columns[$i][0];
            $v = $data[$i];
            if (!preg_match("/_id/i", $k)) {
                echo "<br>$k = $v";
            } else {
                $fk = $v;
            };
        };
        
        if ($fk != null) {
            $sql = "SELECT val FROM statuses WHERE id=$fk";
            $status = mysqli_fetch_row(mysqli_query($conn, $sql))[0];
            echo "<br><br>status = $status";
        };
        ?>
    </div>

</body>

<!-- Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>