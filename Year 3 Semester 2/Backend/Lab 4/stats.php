<!DOCTYPE html>

<html>
<head>
    <meta charset="UTF-8">
    <title>Lab #4 | Stats</title>
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
        <h4><a href="index.php">На головну сторінку</a></h4>
        <?php
        // Get table list
        $sql= "SHOW TABLES";
        $tables = mysqli_fetch_all(mysqli_query($conn, $sql));

        // List tables
        foreach ($tables as $table) {
            $table = $table[0];
            $html = "<br><h5>Таблиця '$table'</h5>";
            // Entry amount
            $sql = "SELECT COUNT(id) FROM $table";
            $amount = mysqli_fetch_all(mysqli_query($conn, $sql))[0][0];
            $html .= "<a>Кількість записів: $amount</a>";
            // Entry amount in last month (in 'ads')
            if ($table === "ads") {
                $date_array = getdate();
                $begin_date = date("Y-m-d", mktime(0, 0, 0, $date_array['mon'], 1, $date_array['year']));
                $end_date = date("Y-m-d", mktime(0, 0, 0, $date_array['mon']+1, 0, $date_array['year']));

                $sql = "SELECT COUNT(id) FROM ads
                        WHERE publication_date>='$begin_date' AND publication_date<='$end_date'";
                $amount = mysqli_fetch_all(mysqli_query($conn, $sql))[0][0];
                $html .= "<a>Кількість записів за останній місяць: $amount</a>";
            }
            // Last entry
            $sql = "SHOW COLUMNS FROM $table";
            $columns = mysqli_fetch_all(mysqli_query($conn, $sql));
            $sql = "SELECT * FROM $table ORDER BY id DESC LIMIT 1";
            $row = mysqli_fetch_all(mysqli_query($conn, $sql))[0];
            $text = "";
            foreach ($row as $k => $v) {
                $text .= "&nbsp;&nbsp;&nbsp;&nbsp;
                          '{$columns[$k][0]}': $v,<br>";
            }
            $text = rtrim($text,1);
            $html .= "<a>Останнім записом в таблиці є: {<br>$text}</a>";
            // Most connections (in 'statuses')
            if ($table === "statuses") {
                $sql = "SELECT s.val, COUNT(a.id) FROM statuses s, ads a
                        WHERE a.status_id = s.id
                        GROUP BY a.status_id
                        LIMIT 0,1";
                $row = mysqli_fetch_all(mysqli_query($conn, $sql))[0];
                $html .= "<a>Найбільше зв'язків у рядка: $row[0] ($row[1])</a>";
            }
            echo $html;
        }
        ?>
    </div>

</body>

<!-- Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>