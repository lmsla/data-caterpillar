<?php
    $host = 'localhost';
    $user = 'root';
    $passwd = 'root';
    $database = 'mysql01';

    $connect = new mysqli($host, $user, $passwd, $database);
    if ($connect->connect_error){
        die("連線失敗" . $connect->connect_error);  // 顯示錯誤
    }

    $connect->query("SET NAMES 'utf8'");   // 顯示中文設定
?>