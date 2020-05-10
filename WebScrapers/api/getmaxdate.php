<?php
require_once('db.php');
$query = 'SELECT IFNULL(max(article_date),"1900-01-01 00:00:00") as MaxArticleDate FROM articles';
$stm = $db->prepare($query);
$stm->execute();
$row = $stm->fetch(PDO::FETCH_ASSOC);
echo json_encode($row);