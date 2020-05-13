<?php
require_once('db.php');
$query = 'SELECT ifnull(article_date,"1900-01-01") as MaxArticleDate FROM articles order by article_date desc limit 1';
$stm = $db->prepare($query);
$stm->execute();
$row = $stm->fetch(PDO::FETCH_ASSOC);
echo json_encode($row);