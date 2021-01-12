<?php
    include 'database.php';

    $ID = $_POST['id'];
    $年度 = $_POST['年度'];
    $月份 = $_POST['月份'];
    $光電站名稱 = $_POST['光電站名稱'];
    $裝置容量 = $_POST['裝置容量'];
    $發電量 = $_POST['發電量'];
    $平均單位裝置容量每日發電量 = $_POST['平均單位裝置容量每日發電量'];

    $updateSql = "UPDATE 太陽光電發電量 SET 
    年度 = '{$年度}',
    月份 = '{$月份}', 
    光電站名稱 = '{$光電站名稱}',
    裝置容量 = '{$裝置容量}',
    發電量 = '{$發電量}',
    平均單位裝置容量每日發電量 = '{$平均單位裝置容量每日發電量}' 
    WHERE id ='{$ID}'";
    
    $status = $connect->query($updateSql);

    if ($status){
        echo "修改成功";
    } else {
        echo "錯誤";
    }
?>
