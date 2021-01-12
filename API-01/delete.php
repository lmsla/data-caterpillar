<?php
    include 'database.php';

    $ID = $_POST['id'];

    $deleteSql = "DELETE FROM 太陽光電發電量 WHERE id = '{$ID}'";  
    
    $status = $connect->query($deleteSql);

    if ($status){
        echo "刪除成功";
    } else {
        echo "錯誤";
    }
?>