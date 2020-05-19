<?php
require_once('db.php');
$query = 'SELECT max(article_date) as MaxArticleDate FROM articles';
$stm = $db->prepare($query);
$stm->execute();
$row = $stm->fetch(PDO::FETCH_ASSOC);
echo json_encode($row);