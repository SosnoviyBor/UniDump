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
        <a class="centered" href="index.php">На головну</a>

        <?php
        $url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
        $url_components = parse_url($url);
        parse_str($url_components['query'], $params);
        $status_id = $params["id"];
        $status = $params["status"];

        $sql = "SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_SCHEMA = 'backend_labs' AND TABLE_NAME = 'ads'";
        $columns = mysqli_fetch_all(mysqli_query($conn, $sql));

        // Get table data
        $sql = "SELECT * FROM ads WHERE status_id = $status_id";
        $data = mysqli_query($conn, $sql);

        if (mysqli_num_rows($data) > 0) {
            // Print the table!
            echo "
            <content class='table'>
                <h4 class='centered'>Пошук оголошень за статусом '$status'<br></h4>
                <table class='table table-striped table-sm'>
                    <thead>
                        <tr>";
    
            // Print column names
            foreach ($columns as $column) {
                echo "<th scope='col' class='centered'>$column[0]</th>";
            };
            echo "</tr><tbody>";
            // Print data rows
            foreach ($data as $row) {
                echo '<tr>';
                // Print individual values
                foreach($row as $val) {
                    echo "<td class='centered'>$val</td>";
                };
                echo "</tr>";
            };
    
            echo '
                </tbody>
                </thead>
            </table>
            </content>';
        } else {
            echo "<h4 class='centered'>На жаль, жодних даних зі статусом '$status' не було знайдено</h4>";
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