<?php
require_once('db.php');
$query = 'SELECT article_url FROM articles limit 1;';
$books_sql = mysqli_query($db, $query);
$books = array();
while($book = mysqli_fetch_array($books_sql)) {
    $books[] = $book;
}
$books = json_encode($books);