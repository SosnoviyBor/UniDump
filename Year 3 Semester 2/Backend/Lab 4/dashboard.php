<!DOCTYPE html>

<html>
<head>
    <meta charset="UTF-8">
    <title>Lab #4 | Dashboard</title>
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

        <?php
        // Read URI params
        $url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
        $url_components = parse_url($url);
        parse_str($url_components['query'], $params);
        $mode = $params["mode"];
        $table = $params["table"];
        $row_id = $params["id"];
        $html = "<a href='table.php?table=$table'><b>Повернутись до таблиці '$table'</b></a>";

        // Check if modes (hyperlink sources) are supported
        $supported_modes = ["new","edit"];
        if (!in_array($mode, $supported_modes)) {
            echo "Невідомий режим сторінки dashboard.php";
            die;
        }

        // Get columns data
        $sql = "SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = 'backend_labs' AND TABLE_NAME = '$table'";
        $columns = mysqli_fetch_all(mysqli_query($conn, $sql));

        // Do specific tasks for each mode
        if ($mode === "edit") {
            // Get row data for editing
            $sql = "SELECT * FROM $table WHERE id=$row_id";
            $data = mysqli_fetch_row(mysqli_query($conn, $sql));

            $html = $html . "<h4>Редагування рядку id={$row_id} в таблиці '$table'</h4>";
        } else if ($mode === "new") {
            $html = $html . "<h4>Створення нового рядку в таблиці '$table'</h4>";
        }

        $form = "
            <form action='/commit.php' method='POST'>
                <input type='text' id='mode' value='$mode' name='mode' hidden readonly>
                <input type='text' id='table' value='$table' name='table' hidden readonly>";
        $supported_dtypes = ["int","varchar","datetime"];
        // Generate form's inoput fields
        foreach (range(0, sizeof($columns)-1) as $i) {
            $column = $columns[$i][0];
            $dtype = $columns[$i][1];
            $val = ($mode === "edit") ? "value='$data[$i]'" : "";

            // Check if this datatype is supported
            if (!in_array($dtype, $supported_dtypes)) {
                echo "Отримано непідтримуваний тип даних '$dtype' у колонці '$column'";
                die;
            } else if ($dtype === "datetime") {
                // Datetimes are being set by database, not user
                continue;
            }

            // Generate datatype specific variables for input fields
            if ($dtype === "int") {
                $inp_type = "number";
                $max_len = "";
            } else if ($dtype === "varchar") {
                $inp_type = "text";
                $max_len = "maxlength='{$columns[$i][2]}'";
            }

            // Generate input fields
            if ($column === "id") {
                // If column is id
                $form = $form . "<input type='$inp_type' id='$column' name='$column' readonly hidden $val><br>";
            } else if (!preg_match("/_id/i", $column)) {
                // If common column
                $form = $form . "<label for='$column'>$column:</label><br>
                                <input type='$inp_type' id='$column' name='$column' required $val $max_len><br>";
            } else {
                // If column is FK
                // Get other table's data
                $sql = "SELECT * FROM statuses";
                $statuses = mysqli_fetch_all(mysqli_query($conn, $sql));

                $form = $form . "<label for='$column'>$column:</label><br>
                                <select id='statuses' name='status_id'>";
                // Generate options for the dropdown
                foreach ($statuses as $s) {
                    $id = $s[0];
                    $status = $s[1];
                    $selected = ($status === $data[$i]) ? "selected" : "";
                    $form = $form . "<option value='$id' $selected>$status (id=$id)</option>";
                }
                $form = $form . "</select><br>";
            };
        };
        $form = $form . "<br><input type='submit' value='Підтвердити'></form>";

        // Make deletion form for "edit" mode
        if ($mode === "edit") {
            $form = $form . "
                <form action='/commit.php' method='POST'>
                    <input type='text' id='mode' value='delete' name='mode' hidden readonly>
                    <input type='text' id='table' value='$table' name='table' hidden readonly>
                    <input type='text' id='id' value='$row_id' name='id' hidden readonly>
                    <input type='submit' value='Видалити'>
                </form>";
        }

        $html = $html . $form;
        echo $html;
        ?>
    </div>

</body>

<!-- Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>