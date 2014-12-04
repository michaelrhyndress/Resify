<?php session_start(); ?>
<?php
define("PBKDF2_HASH_ALGORITHM", "sha256");
define("PBKDF2_ITERATIONS", 1000);
define("PBKDF2_SALT_BYTE_SIZE", 24);
define("PBKDF2_HASH_BYTE_SIZE", 24);

define("HASH_SECTIONS", 4);
define("HASH_ALGORITHM_INDEX", 0);
define("HASH_ITERATION_INDEX", 1);
define("HASH_SALT_INDEX", 2);
define("HASH_PBKDF2_INDEX", 3);

function create_hash($password)
{
    // format: algorithm:iterations:salt:hash
    $salt = base64_encode(mcrypt_create_iv(PBKDF2_SALT_BYTE_SIZE, MCRYPT_DEV_URANDOM));
    return PBKDF2_HASH_ALGORITHM . ":" . PBKDF2_ITERATIONS . ":" .  $salt . ":" . 
        base64_encode(pbkdf2(
            PBKDF2_HASH_ALGORITHM,
            $password,
            $salt,
            PBKDF2_ITERATIONS,
            PBKDF2_HASH_BYTE_SIZE,
            true
        ));
}

function validate_password($password, $correct_hash)
{
    $params = explode(":", $correct_hash);
    if(count($params) < HASH_SECTIONS)
       return false; 
    $pbkdf2 = base64_decode($params[HASH_PBKDF2_INDEX]);
    return slow_equals(
        $pbkdf2,
        pbkdf2(
            $params[HASH_ALGORITHM_INDEX],
            $password,
            $params[HASH_SALT_INDEX],
            (int)$params[HASH_ITERATION_INDEX],
            strlen($pbkdf2),
            true
        )
    );
}

// Compares two strings $a and $b in length-constant time.
function slow_equals($a, $b)
{
    $diff = strlen($a) ^ strlen($b);
    for($i = 0; $i < strlen($a) && $i < strlen($b); $i++)
    {
        $diff |= ord($a[$i]) ^ ord($b[$i]);
    }
    return $diff === 0; 
}


function pbkdf2($algorithm, $password, $salt, $count, $key_length, $raw_output = false)
{
    $algorithm = strtolower($algorithm);
    if(!in_array($algorithm, hash_algos(), true))
        trigger_error('PBKDF2 ERROR: Invalid hash algorithm.', E_USER_ERROR);
    if($count <= 0 || $key_length <= 0)
        trigger_error('PBKDF2 ERROR: Invalid parameters.', E_USER_ERROR);

    if (function_exists("hash_pbkdf2")) {
        // The output length is in NIBBLES (4-bits) if $raw_output is false!
        if (!$raw_output) {
            $key_length = $key_length * 2;
        }
        return hash_pbkdf2($algorithm, $password, $salt, $count, $key_length, $raw_output);
    }

    $hash_length = strlen(hash($algorithm, "", true));
    $block_count = ceil($key_length / $hash_length);

    $output = "";
    for($i = 1; $i <= $block_count; $i++) {
        // $i encoded as 4 bytes, big endian.
        $last = $salt . pack("N", $i);
        // first iteration
        $last = $xorsum = hash_hmac($algorithm, $last, $password, true);
        // perform the other $count - 1 iterations
        for ($j = 1; $j < $count; $j++) {
            $xorsum ^= ($last = hash_hmac($algorithm, $last, $password, true));
        }
        $output .= $xorsum;
    }

    if($raw_output)
        return substr($output, 0, $key_length);
    else
        return bin2hex(substr($output, 0, $key_length));
}


function is_valid_email($email, $test_mx = false)  
{  
    if(preg_match("/^([_a-z0-9-]+)(\.[_a-z0-9-]+)*@([a-z0-9-]+)(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/i", $email))  
        if($test_mx)  
        {  
            list($username, $domain) = explode("@", $email);  
            return getmxrr($domain, $mxrecords);  
        }  
        else  
            return true;  
    else  
        return false;  
}


function is_valid_username($username)
{
	if(preg_match("/[A-Za-z0-9]+/", username) && strlen(username) >= 2 && strlen(username) <= 64){
		return true;
	}
	else
		return false;
}

function NewGuid() { 
	$s = strtoupper(md5(uniqid(rand(),true))); 
	$guidText = 
	substr($s,0,8) . '-' . 
	substr($s,8,4) . '-' . 
	substr($s,12,4). '-' . 
	substr($s,16,4). '-' . 
	substr($s,20); 
	return $guidText;
}

function sendTo($to, $Guid){
	$subject = "Do Not Reply : Resify Email Verification";
	$body = "Welcome to Resify! Enter <b>" .$Guid. "</b> into the verification box on the website or click on the following link to finish your registration. <br /><br /> <b> <a href='http://www.bidonmoving.com/Resify/SystemFiles/Validate.php?code=".$Guid."'>Verify My Account</a></b>.<br /><br /> If you did not initiate this request then delete it from your inbox and disregard it. To view Resify, or create a free account, follow this link <a href='http://www.bidonmoving.com/Resify'>http://www.bidonmoving.com/Resify</a>";
	$headers = "From: Resify Support\r\n";
	$headers .= "Reply-To: michaelrhyndress@gmail.com\r\n";
	$headers .= "Return-Path: michaelrhyndress@gmail.com\r\n";
	$headers .= "X-Mailer: PHP5\n";
	$headers .= 'MIME-Version: 1.0' . "\n";
	$headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
	if(@mail($to,$subject,$body,$headers)){
		header('Location:http://bidonmoving.com/Resify/index.php?auth=v#slick-popup');
		exit();
	}
	else{
		header('Location: http://bidonmoving.com/Resify/index.php?auth=error#slick-popup');
		exit();
	}
}

//********************************************************** REGISTER START
if($_POST["type"] == 'Register'){
	//Get Post Date
	$Guid = NewGuid(); //Random Number
	$passCheck=0;
	$username= $_POST['username'];
	$email= $_POST['email'];
	$password= $_POST['password'];
	$passwordRepeat = $_POST['passwordRepeat'];
	$profileVisibility= $_POST['profileVisibility'];
	$othersContact= $_POST['othersContact'];
	$newsletterSignup = $_POST['newsletterSignup'];
	$termsAgree = $_POST['termsAgree'];

	//SET CHECKBOX VALUES TO BINARY
	
	if($termsAgree == "on"){
		$termsAgree = 1;
	}
	else{
		$termsAgree = 0;
	}
	
	if($profileVisibility == "on"){
		$profileVisibility = 1;
	}
	else{
		$profileVisibility = 0;
	}
	
	if($othersContact == "on"){
		$othersContact = 1;
	}
	else{
		$othersContact = 0;
	}
	
	if($newsletterSignup == "on"){
		$newsletterSignup = 1;
	}
	else{
		$newsletterSignup = 0;
	}

	if(strlen($password) < 6){
		header('Location: http://bidonmoving.com/Resify/index.php?error=invalid-p#slick-popup');
		exit();
	}
	
	if($password === $passwordRepeat){
		$passCheck = 1;
	}
	else{
		$passCheck = 0;
	}
	//SANITIZE EMAIL
	if(!is_valid_email($email, true)){
		header('Location: http://bidonmoving.com/Resify/index.php?error=invalid-e#slick-popup');
		exit();
	}
	
	//SANITIZE USERNAME
	if(!is_valid_username($username)){
		header('Location: http://bidonmoving.com/Resify/index.php?error=invalid-u#slick-popup');
	}

	//SANITIZE PASSWORD
	if($passCheck == 0){
		header('Location: http://bidonmoving.com/Resify/index.php?error=invalid-p#slick-popup');
		exit();
	}
	else{
		$Hashed = create_hash($password);
	}
	//Make terms of agreement be filled out
	if($termsAgree == 1){
		$termsAgree = 1;
	}
	else{
		header('Location: http://bidonmoving.com/Resify/index.php?error=invalid-t#slick-popup');
		exit();
	}
	require_once('usableCode/settings.php');
	$conn = getDatabaseConnection();
	if (mysqli_connect_errno()) {
	    printf("Connect failed: %s\n", mysqli_connect_error());
	}

	if($result = $conn->query("SELECT email, username FROM members WHERE email = '$email' OR username = '$username'")){
		 $row_cnt = $result->num_rows;
	}
	if ($row_cnt !== 0){ 
	    header('Location: http://bidonmoving.com/Resify/index.php?error=invalid-z#slick-popup');
		exit();
	}
	
	else{
		$raw_email=$email;
		$raw_GUID=$Guid;
		$username ="'" . $conn->real_escape_string($username). "'";
		$email ="'" . $conn->real_escape_string($email). "'";
		$Hashed ="'" . $conn->real_escape_string($Hashed). "'";
		$profileVisibility ="'" . $conn->real_escape_string($profileVisibility). "'";
		$newsletterSignup ="'" . $conn->real_escape_string($newsletterSignup). "'";
		$termsAgree ="'" . $conn->real_escape_string($termsAgree). "'";
		$Guid ="'" . $conn->real_escape_string($Guid). "'";
		
		$sql="INSERT INTO members (username, email, password, is_public, allow_contact, get_news, agree_to_terms, emailVerify) VALUES ($username, $email, $Hashed, $profileVisibility, $othersContact, $newsletterSignup, $termsAgree, $Guid)";
		if($conn->query($sql) === false){
			trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);
		}
		else{
			$sql="INSERT INTO additionalInfo (userName) VALUES ($username)";
			$conn->query($sql);
			sendTo($raw_email, $raw_GUID);
		}
	}
} //END REGISTER
//********************************************************** REGISTER END


//********************************************************** LOG IN START
if($_POST["type"] == 'LogIn'){
	$username= $_POST['username'];
	$password= $_POST['password'];
	$logInType = 'none';
	$userPermission = null;
	require_once('usableCode/settings.php');
	$conn = getDatabaseConnection();
	
	if(is_valid_email($username, true) === true){ //if EMAIL
		$logInType = "email";
		if($result = $conn->query("SELECT username,password, permissions FROM members WHERE email = '$username'")){
		 	$row_cnt = $result->num_rows;
			 while($row = $result->fetch_row()){
				 $loginUser=$row[0];
				 $Hash=$row[1];
				 $userPermission=$row[2];
			 }
		 }
	}
	
	else if(is_valid_username($username) === true){ //if UserName
		$logInType = "username";
		if($result = $conn->query("SELECT password, permissions FROM members WHERE username = '$username'")){
		 	$row_cnt = $result->num_rows;
			 while($row = $result->fetch_row()){
				 $loginUser=$username;
				 $Hash=$row[0];
				 $userPermission=$row[1];
			 }
		 }
	}

	if (isset($loginUser)){ 
		$isValid = validate_password($password, $Hash);
		if($isValid == 1 && $userPermission !== null){
			$_SESSION['user'] = $loginUser;
			$_SESSION['perm'] = $userPermission;
			header('Location: http://bidonmoving.com/Resify/');
			exit();
		}
		else{
			if($userPermission === null){
				header('Location: http://bidonmoving.com/Resify/index.php?login=error-null#slick-popup');
				exit();
			}
			else{
				header('Location: http://bidonmoving.com/Resify/index.php?login=error-p#slick-popup');
				exit();
			}
		}
	}
	else{
		 header('Location: http://bidonmoving.com/Resify/index.php?login=error-l#slick-popup');
		 exit();
	}
} //END LOGIN
//********************************************************** LOG IN END



//********************************************************** RESET START
if($_POST["type"] == 'Reset'){
	require_once('usableCode/settings.php'); //MAKE SURE EMAIL IS A USER
	$conn = getDatabaseConnection();
	$Guid = NewGuid(); //Random Number
	$email= $_POST['email'];
	if(is_valid_email($email, true) === true){ //if EMAIL
		$query="UPDATE members SET emailVerify='$Guid' WHERE email='$email'" or die("Error in the consult.." . mysqli_error($conn));
		if($conn->query($query) === false){
			trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);	
		}
		else{
			sendTo($email, $Guid);//Mail Verify
		}
	}
	else{
		header('Location: http://bidonmoving.com/Resify/index.php?error=invalid-e#slick-popup');
		exit();
	}
} //END RESET
//********************************************************** RESTART END



//********************************************************** CODE VERIFY
if($_POST["type"] == 'Verify' || $_GET['code']){
	$code = $_GET['code'];
	if($_POST['code'] || (isset($code))){  //IF CODE IS GIVEN
		require_once('usableCode/settings.php');
		$conn = getDatabaseConnection();
		if(empty($code)){
			$code = $_POST['code'];
		}
		if($result = $conn->query("SELECT email, permissions FROM members WHERE emailVerify = '$code'")){
			 $row_cnt = $result->num_rows;
			 while($row = $result->fetch_row()){
				 $email=$row[0];
				 $userPerm=$row[1];
			 }
		}
		if ($row_cnt != 1){ 
			header('Location: http://bidonmoving.com/Resify/index.php?auth=error#slick-popup');
			exit();
		}
		else{
			if($userPerm === null){
				$permSQL = "permissions='1'";
			}
			else{
				$permSQL = "permissions='".$userPerm."'";
			}
			$_SESSION['user']= $email;
			$query="UPDATE members SET emailVerify = '', ". $permSQL ." WHERE email='$email'"  or die("Error in the consult.." . mysqli_error($conn));;
			if($conn->query($query) === false){
				trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);
			}
			else{
				header('Location:http://bidonmoving.com/Resify/index.php');
				exit();
			}
		}
	} //END IF CODE GIVEN
	else{  //IF EMAIL GIVEN
		$email= $_POST['email'];
		require_once('usableCode/settings.php'); //MAKE SURE EMAIL IS A USER
		$conn = getDatabaseConnection();
		if($result=$conn->query("SELECT email FROM members WHERE email = '$email'")){
			$row_cnt = $result->num_rows;
		}
		if ($row_cnt == 0){    //NOT A USER!!!
			header('Location: http://bidonmoving.com/Resify/index.php?auth=error#slick-popup');
			exit();
		}
		else{ //EMAIL IS A USER!!!
			//////////////////////////
			$Guid = NewGuid(); //Random Number
			$query="UPDATE members SET emailVerify='$Guid' WHERE email='$email'" or die("Error in the consult.." . mysqli_error($conn));
			if($conn->query($query) === false){
				trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);	
			}
			else{
			//Mail Verify
				sendTo($email, $Guid);
			}
		}
	}
}
//********************************************************** END CODE VERIFY

?>