<div style="margin-bottom: 10px; margin-left: 10px; font-size: 18px ;"><b>成交資訊</b></div>

<?php
    include 'database_w.php';

    $id = $_POST['id'];
    $code = $_POST['code'];

    $fetchSql = "SELECT * FROM stock_date WHERE id = '{$id}'";

    // $fetchSql = "SELECT * FROM 太陽光電發電量s WHERE id = '{$ID}'";  
    
    $status = $connect->query($fetchSql);

    echo '<table border = "0" 
            cellspacing = "0"  
            style = "color: #555555 ; font-size: 15px ;">';   

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
        // echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.日期.'</th>'; 
        echo '</tr>';

    while($row = $status->fetch_array()){
        echo '<tr align="center"  >';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['code'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['name'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['close_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['range'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['range'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['stock_count'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['open_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['high_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['low_price'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['close_price'].'</td>';
        // echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['date'].'</td>';
        echo '</tr>';

    }
    echo '</table>';

    $connect->close();
?>


<br><br>
<div style="margin-bottom: 10px; margin-left: 10px; font-size: 18px ;"><b>基本資料/財報資訊</b></div>

<?php
    include 'database_w.php';

    $ID = $_POST['id'];

    $fetchSql = "SELECT * FROM 上市公司基本資料 WHERE id = '{$id}'";  
    
    $status = $connect->query($fetchSql);

    echo '<table border = "0" 
            cellspacing = "0"  
            style = "color: #555555 ; font-size: 15px ;">';   

        echo '<tr align="center" style="background-color: #fafafa">';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.股票代號.'</th>';
        echo '<th width="10%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.公司名稱.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.產業別.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.統一編號.'</th>';
        echo '<th width="11%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.公司網址.'</th>';
        echo '<th width="11%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.公司電話.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.董事長.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.總經理.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.成立日期.'</th>';
        echo '<th width="9%" style="padding: 8px; border-top: 1px #cccccc solid ; border-bottom: 1px #cccccc solid ; ">'.上市日期.'</th>'; 
        echo '</tr>';

    while($row = $status->fetch_array()){
        echo '<tr align="center"  >';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['code'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['name'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['industry'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['營利事業統一編號'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['網址'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['總機電話'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['董事長'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['總經理'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['成立日期'].'</td>';
        echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['上市日期'].'</td>';
        // echo '<td style="padding: 7px; border-bottom: 1px #cccccc solid ; ">'.$row['上市日期'].'</td>';
        echo '</tr>';

    }
    echo '</table>';

    $connect->close();
?>