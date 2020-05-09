<?php
require_once('db.php');
$query = 'SELECT article_content FROM articles where id = 9';
$stm = $db->prepare($query);
$stm->execute();
$row = $stm->fetch(PDO::FETCH_ASSOC);
echo json_encode($row);