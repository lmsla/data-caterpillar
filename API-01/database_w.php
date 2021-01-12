<?php
    $host = '192.168.56.102';
    $user = 'eason';
    $passwd = '671106';
    $database = 'stock_database';

    $connect = new mysqli($host, $user, $passwd, $database);
    if ($connect->connect_error){
        die("連線失敗" . $connect->connect_error);  // 顯示錯誤
    }

    $connect->query("SET NAMES 'utf8'");   // 顯示中文設定
?>