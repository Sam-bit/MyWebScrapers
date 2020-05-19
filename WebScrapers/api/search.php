<?php
require_once('db.php');
$searchString = $_POST["search_string"];
$query = '"Select a.article_url,a.article_title,a.article_thumbnail,a.article_date,a.article_subtitle,a.article_content,a.article_checked_by,a.article_verdict,a.article_site_id, s.src_name From articles a inner join sources s on a.article_site_id = s.src_id where (a.article_content like '%$searchString%' or a.article_subtitle like '%$searchString%' or a.article_title like '%$searchString%') and (trim(a.article_subtitle) <> '') order by a.article_date desc");';
$stm = $db->prepare($query);
$stm->execute();
$row = $stm->fetch(PDO::FETCH_ASSOC);
echo json_encode($row);