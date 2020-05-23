<?php
require_once('db.php');
$searchString = $_POST["search_string"] ?? '';
$from = $_POST["from"] ?? 1;
$to = $_POST["to"] ?? 1;

$query = "select rownum,article_url,article_title,article_thumbnail,article_date,article_subtitle,article_content,article_checked_by,article_verdict,article_site_id, src_name from (Select @tmp:=@tmp + 1 rownum,a.article_url,a.article_title,a.article_thumbnail,a.article_date,a.article_subtitle,a.article_content,a.article_checked_by,a.article_verdict,a.article_site_id, s.src_name From (select @tmp:=0) z,articles a inner join sources s on a.article_site_id = s.src_id where (a.article_content like :searchString or a.article_subtitle like :searchString or a.article_title like :searchString) and (trim(a.article_subtitle) <> '') ) temp where rownum between :from and :to order by article_date";
$stm = $db->prepare($query);
$stm->bindParam(':to', $to, PDO::PARAM_INT);
$stm->bindParam(':from', $from, PDO::PARAM_INT);
$stm->bindValue(':searchString', "%{$searchString}%");
$stm->execute();
$row = $stm->fetch(PDO::FETCH_ASSOC);
echo json_encode($row);