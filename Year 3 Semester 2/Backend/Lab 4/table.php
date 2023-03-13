<!DOCTYPE html>

<html>
<head>
    <meta charset="UTF-8">
    <title>Lab #4 | Tables</title>
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
        <h6 class="centered">
            <a href="index.php">Повернутись до головної сторінки</a>
        </h6>

        <?php
        $url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
        $url_components = parse_url($url);
        parse_str($url_components['query'], $params);
        $table = $params["table"];
        $orderby_col = ($params["orderby"]) ? $params["orderby"] : "id";
        $filter = $params["filter"];
        $sql_where = ($filter) ? "WHERE status_id=$params[filter]" : "";
        $html = "";

        if ($_SERVER['REQUEST_METHOD'] === 'POST' and $_POST["search"]) {
            if ($table === "ads") {
                $search = "WHERE adress LIKE '%$_POST[search]%'";
            } else if ($table === "statuses") {
                $search = "WHERE val LIKE '%$_POST[search]%'";
            }
        }
    
        // Get column names
        $sql = "SELECT COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = 'backend_labs' AND TABLE_NAME = '$table'";
        $columns = mysqli_fetch_all(mysqli_query($conn, $sql));

        // Get table data
        $sql = "SELECT * FROM $table $sql_where $search ORDER BY $orderby_col";
        $data = mysqli_query($conn, $sql);

        // Generate the table!
        $html = $html . "
            <content class='table'>
                <h4 class='centered'>Таблиця $table</h4>
                <form class='centered' action='table.php?table=$table' method='POST'>
                    <input type='text' id='search' name='search'>
                    <input type='submit' value='Пошук'></form>
                </from>
                <h6 class='centered'>Відсортортована за колонкою '$orderby_col'</h6>";
        if ($filter) {
            $html = $html . "<h6 class='centered'>Відфільтровано за status_id=$filter</h6>";
        }
        $html = $html . 
            "<table class='table table-striped table-sm'>
                <thead>
                    <tr>";

        // Print column names
        foreach ($columns as $column) {
            $html = $html . "
                <th scope='col' class='centered'>
                    <a href='/table.php?table=$table&orderby=$column[0]'>$column[0]</a>
                </th>";
        };
        // Add button for new field creation
        $html = $html . "
                <th scope='col' class='edit-link centered'>
                    <a href='dashboard.php?mode=new&table=$table'>New</a>
                </th>
            </tr>
            <tbody>";
        // Print data rows
        foreach ($data as $row) {
            $html = $html . '<tr>';
            // Print individual values
            $i = 0;
            foreach($row as $val) {
                $i++;
                // If table is 'statuses', then alter its content
                if ($table === "statuses" && $i === 2) {
                    $html = $html . "
                        <td class='centered'>
                            <a href='table.php?table=ads&filter=$row[id]'>$val</a>
                        </td>";
                    $i = 0;
                } else {
                    // Common behaviour
                    $html = $html . "<td class='centered'>$val</td>";
                }
            };
            $html = $html . "
                    <td class='edit-link centered'>
                        <a href='dashboard.php?mode=edit&table=$table&id=$row[id]'>Edit</a>
                    </td>
                </tr>";
        };

        $html = $html . '
                        </tbody>
                    </thead>
                </table>
            </content>';
        echo $html;
        ?>
    </div>

<!-- Table structure reference
<content class="table">
    <h4 class="centered">Table name</h4>
    <table class="table table-striped table-sm">
        <thead>
            <tr>
                <th scope="col" class="centered">Column name</th>
                <th scope="col" class="centered">Column name</th>
                <th scope="col" class="centered">Column name</th>
                <th scope="col" class="centered">Column name</th>
            </tr>

            <tbody>
                <tr>
                    <td class="centered">Data</td>
                    <td class="centered">Data</td>
                    <td class="centered">Data</td>
                </tr>
                <tr>
                    <td class="centered">Data</td>
                    <td class="centered">Data</td>
                    <td class="centered">Data</td>
                </tr>
            </tbody>
        </thead>
    </table>
</content>
-->

</body>

<!-- Bootstrap -->
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>