<!DOCTYPE html>
<html>
<body bgcolor="lightgrey">

<h1 align="center"><font face="Helvetica">Data Dashboard</font></h1>
<hr>
<?php
$output = shell_exec('python visualize.py');
echo $output;
?> 
<hr>
<p align="right"><font size="2"> Data from:</br>https://jobindo.com/index.php?lang=in&mod=search&location=9-328&num=2</br>Tanggal: 15 Mei 2018</font></p>
</body>
</html>