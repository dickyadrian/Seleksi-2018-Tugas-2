<!DOCTYPE html>
<html>
<body>

<h1>Data Dashboard</h1>
<?php
$output = shell_exec('python visualize.py');
echo "</br>".$output;
?> 

</body>
</html>