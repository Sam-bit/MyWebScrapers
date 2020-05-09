<?php
$dns = 'mysql:host=localhost;dbname=facts';
$user = 'root';
$password = '';
try{
 $db = new PDO ($dns, $user, $password);
 print('connected');
}catch( PDOException $e){
 $error = $e->getMessage();
 echo $error;
}