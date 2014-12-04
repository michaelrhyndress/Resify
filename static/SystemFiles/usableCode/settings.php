<?php
define ('DB_HOST', 'Resify.db.11290397.hostedresource.com');
define ('DB_NAME', 'Resify');
define ('DB_USERNAME', 'Resify');
define ('DB_PASSWORD', 'Fox6947!m');

	function getDatabaseConnection()
	{
		$dbh = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);
		return $dbh;
	}

?>