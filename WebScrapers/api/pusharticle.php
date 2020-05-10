<?php
require_once('db.php');
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
$article_sync_date = $_POST["push_article_sync_date"];

$table = "articles";

$sql = "INSERT INTO $table (
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
                            article_sync_date
                            ) 
                    VALUES (
                            '$article_url',
                            '$article_title',
                            '$article_thumbnail',
                            '$article_date',
							'$article_subtitle',
                            '$article_content',
                            '$article_checked_by',
                            '$article_verdict',
							'$article_alt_verdict',
							'$article_site_id',
                            '$article_sync_date'
                            )";
							
$result = $db->query($sql);
$db->close();
return;