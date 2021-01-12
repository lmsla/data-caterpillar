<?php
    include 'database.php';

    $ID = $_POST['id'];
    $年度 = $_POST['年度'];
    $月份 = $_POST['月份'];
    $光電站名稱 = $_POST['光電站名稱'];
    $裝置容量 = $_POST['裝置容量'];
    $發電量 = $_POST['發電量'];
    $平均單位裝置容量每日發電量 = $_POST['平均單位裝置容量每日發電量'];

    $insertSql = "INSERT INTO 太陽光電發電量 (id, 年度, 月份 , 光電站名稱, 裝置容量, 發電量, 平均單位裝置容量每日發電量 ) VALUES('{$ID}', '{$年度}', '{$月份}', '{$光電站名稱}', '{$裝置容量}', '{$發電量}', '{$平均單位裝置容量每日發電量}')";
    
    $status = $connect->query($insertSql);

    if ($status){
        echo "新增成功";
    } else {
        echo "錯誤";
    }
?>

