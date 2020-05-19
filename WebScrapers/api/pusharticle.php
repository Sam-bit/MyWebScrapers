<?php
require_once('db.php');
$insert_option = $_POST["insert_option"];
$article_url = $_POST["push_article_url"];
$article_title = $_POST["push_article_title"];
$article_thumbnail = $_POST["push_article_thumbnail"];
$article_date = $_POST["push_article_date"];
$article_subtitle = $_POST["push_article_subtitle"];
$article_content = $_POST["push_article_content"];
$article_checked_by = $_POST["push_article_checked_by"];
$article_verdict = $_POST["push_article_verdict"];
$article_alt_verdict = $_POST["push_article_alt_verdict"];
$article_site_id = $_POST["push_article_site_id"];
$article_is_pushed = $_POST["push_article_is_pushed"];

$table = "articles";

if($insert_option == 'INSERT_UNIQUE'){
$sql = "INSERT INTO articles (
                            article_url,
                            article_title,
                            article_thumbnail,
                            article_date,
							article_subtitle,
                            article_content,
                            article_checked_by,
                            article_verdict,
							article_alt_verdict,
                            article_site_id,
                            article_is_pushed
                            )
		SELECT * FROM (SELECT ? as article_url,
                            ? as article_title,
                            ? as article_thumbnail,
                            ? as article_date,
							? as article_subtitle,
                            ? as article_content,
                            ? as article_checked_by,
                            ? as article_verdict, 
							? as article_alt_verdict,
							? as article_site_id,
                            ? as article_is_pushed) AS tmp
WHERE NOT EXISTS (
    SELECT article_url FROM articles WHERE article_url = ?
) LIMIT 1;";
$db->prepare($sql)->execute([$article_url,
                            $article_title,
                            $article_thumbnail,
                            $article_date,
							$article_subtitle,
                            $article_content,
                            $article_checked_by,
                            $article_verdict,
							$article_alt_verdict,
							$article_site_id,
                            $article_is_pushed,
							$article_url]);
//$result = $db->query($sql);
}
else
{
$sql = "INSERT INTO articles (
                            article_url,
                            article_title,
                            article_thumbnail,
                            article_date,
							article_subtitle,
                            article_content,
                            article_checked_by,
                            article_verdict,
							article_alt_verdict,
                            article_site_id,
                            article_is_pushed
                            )
		VALUES (?,?,?,?,?,?,?,?,?,?,?)";
		$db->prepare($sql)->execute([$article_url,
                            $article_title,
                            $article_thumbnail,
                            $article_date,
							$article_subtitle,
                            $article_content,
                            $article_checked_by,
                            $article_verdict,
							$article_alt_verdict,
							$article_site_id,
                            $article_is_pushed
							]);
//$result = $db->query($sql);
}						
return;