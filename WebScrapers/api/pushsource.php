<?php
require_once('db.php');
$src_id = $_POST["push_src_id"];
$src_name = $_POST["push_src_name"];
$src_alt_name = $_POST["push_src_alt_name"];
$src_logo = $_POST["push_src_logo"];
$src_is_ifcn_approved = $_POST["push_src_is_ifcn_approved"];
$src_address = $_POST["push_src_address"];
$src_is_active = $_POST["push_src_is_active"];
$src_country = $_POST["push_src_country"];
$src_supported_by = $_POST["push_src_supported_by"];
$src_language = $_POST["push_src_language"];
$src_added_date = $_POST["push_src_added_date"];

$sql = "INSERT INTO sources (
                            src_id,
							src_name,
							src_alt_name,
							src_logo,
							src_is_ifcn_approved,
							src_address,
							src_is_active,
							src_country,
							src_supported_by,
							src_language,
							src_added_date
                            )
		SELECT * FROM (SELECT ? as src_id,
                            ? as src_name,
                            ? as src_alt_name,
                            ? as src_logo,
							? as src_is_ifcn_approved,
                            ? as src_address,
                            ? as src_is_active,
                            ? as src_country, 
							? as src_supported_by,
							? as src_language,
                            ? as src_added_date) AS tmp
WHERE NOT EXISTS (
    SELECT src_address FROM sources WHERE src_address = ?
) LIMIT 1;";
$db->prepare($sql)->execute([$src_id,
                            $src_name,
                            $src_alt_name,
                            $src_logo,
							$src_is_ifcn_approved,
                            $src_address,
                            $src_is_active,
                            $src_country,
							$src_supported_by,
							$src_language,
                            $src_added_date,
							$src_name]);
return;