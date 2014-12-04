<?php
session_start(); # NOTE THE SESSION START
$_SESSION = array(); 

if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000,
        $params["path"], $params["domain"],
        $params["secure"], $params["httponly"]
    );
}

session_destroy();
# Ensure that the cookie is destructed by setting a date in the past
setcookie(session_name(), false, time() - 3600); 

//echo "Logged Out !";
// Note: Putting echo "Logged Out !" before sending the header could result in a "Headers already sent" warning and won't redirect your page to the login page - pointed out by @Treur - I didn't spot that one.. Thanks...
header("Location:../index.php");
exit(); # NOTE THE EXIT
?>
