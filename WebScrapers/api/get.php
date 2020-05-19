<?php
require_once('db.php');
$query = 'SELECT article_url FROM articles';
$stm = $db->prepare($query);
$stm->execute();
$row = $stm->fetch(PDO::FETCH_ASSOC);
echo json_encode($row);