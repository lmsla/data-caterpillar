<?php
    include 'database.php';

    $tj  = "1 = 1";
    $tj1 = "1 = 1";
    $tj2 = "1 = 1";
    $年度 = "";
    
    if (!empty($_POST['id'])){
        $ID = $_POST['id'];
        $tj = "id = '{$ID}'";
    }
    
    if (!empty($_POST['年度'])){
        $年度 = $_POST['年度'];
        $tj1 = "年度 ='{$年度}'";
    }

    if (!empty($_POST['月份'])){
        $月份 = $_POST['月份'];
        $tj2 = "月份 = '{$月份}'";
    }
    
    $fetchSql = "SELECT * FROM 太陽光電發電量 WHERE {$tj} and {$tj1} and {$tj2}";  
    
    $status = $connect->query($fetchSql);

    $num = mysqli_num_rows($status);  // 計算筆數
    echo '共 : ' .$num. ' 筆資料';

    echo '<table border = "1" cellspacing = "1">';       // style = "border:1px #cccccc"
        echo '<tr align="center">';
        echo '<td>'.ID.'</td>';
        echo '<td>'.年度.'</td>';
        echo '<td>'.月份.'</td>';
        echo '<td>'.光電站名稱.'</td>';
        echo '<td>'.裝置容量.'</td>';
        echo '<td>'.發電量.'</td>';
        echo '<td>'.平均單位裝置容量每日發電量.'</td>';
        echo '</tr>';

    if ($status){
        while ($row = $status->fetch_array()){
            echo '<tr>';
            echo '<td align="center">'.$row['id'].'</td>';
            echo '<td align="center">'.$row['年度'].'</td>';
            echo '<td align="center">'.$row['月份'].'</td>';
            echo '<td>'.$row['光電站名稱'].'</td>';
            echo '<td align="right">'.$row['裝置容量'].'</td>';
            echo '<td align="right">'.$row['發電量'].'</td>';
            echo '<td align="right">'.$row['平均單位裝置容量每日發電量'].'</td>';
            echo '</tr>';
        }
        echo '</table>';
    }
    $connect->close();
?>