<?php
require_once('db.php');
$offset = $_POST["offset"];
$recordsPerPage = $_POST["records_per_page"];
$query = "select a.article_url,a.article_title,a.article_thumbnail,a.article_date,a.article_subtitle,a.article_checked_by,a.article_verdict,
a.article_alt_verdict,a.article_site_id, s.src_name From articles a inner join sources s on a.article_site_id = s.src_id order by a.article_date desc limit :offset, :recordsPerPage";
$stmt = $db->prepare($query);
$stmt->bindParam(':offset', $offset, PDO::PARAM_INT);
$stmt->bindParam(':recordsPerPage', $recordsPerPage, PDO::PARAM_INT);
$stmt->execute() or die(print_r($stmt->errorInfo(), true));
$row = $stmt->fetchall(PDO::FETCH_ASSOC);
echo json_encode($row, JSON_PRETTY_PRINT);