<!DOCTYPE html>

<html>
<head>
    <meta charset="UTF-8">
    <title>Lab #4 | Home</title>
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
        <div class="centered">
            <h1>Можливо дешборд?</h1>
            <h4>Список таблиць</h4>

            <?php
            // Get table list
            $sql= "SHOW TABLES";
            $tables = mysqli_fetch_all(mysqli_query($conn, $sql));

            // List tables
            $n = 0;
            foreach ($tables as $table) {
                $table = $table[0];
                $n++;
                $html = "
                    <h6 class='centered'>
                        <a href='table.php?table=$table'>$n. $table</a>
                    </h6>";
                echo $html;
            }
            ?>
            <br>
            <h4><a href="stats.php">Статистика</a></h4>
        </div>
    </div>

</body>

<!-- Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>