<?php

$name = $_GET['name'];
$name = htmlspecialchars($name);
echo "Welcome $name!";

#solution xss
#No solution