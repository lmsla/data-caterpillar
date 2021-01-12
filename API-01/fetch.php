<?php
    include 'database_w.php';

    $fetchSql = "SELECT * FROM stock_date";  
    
    $status = $connect->query($fetchSql);

    // $num = mysqli_num_rows($status);  // 計算筆數
    // echo '共 : ' .$num. ' 筆資料';

    echo '<table border = "0" 
            cellspacing = "0"  
            style = "color: #555555 ; font-size: 16px ;">';   

        echo '<tr align="center" style="background-color: #fafafa">';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.股票代號.'</th>';
        echo '<th width="10%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.名稱.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.收盤價.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.漲跌.'</th>';
        echo '<th width="11%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.漲跌幅.'</th>';
        echo '<th width="11%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.成交量.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.開盤.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.最高.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.最低.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.昨收.'</th>'; 
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.日期.'</th>'; 
        echo '</tr>';

    while($row = $status->fetch_array()){
        echo '<tr align="center"  >';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['code'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['turnover'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['close_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['range'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['range'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['stock_count'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['open_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['high_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['low_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['close_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['close_price'].'</td>';
        echo '</tr>';

    }
    echo '</table>';

    $connect->close();
?>
