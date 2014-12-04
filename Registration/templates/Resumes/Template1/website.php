<?php session_start();
$userName=$_SESSION['user'];
$userName=$_GET['user'];
if($userName=="michaelrhyndress"){
	$userName='support';
}

$sql="SELECT firstName, lastName, facebook, twitter, linkedIn, title, position, email, phone FROM additionalInfo WHERE userName='". $userName. "'";
require_once('../../usableCode/settings.php');
$conn = getDatabaseConnection();
if($result=$conn ->query($sql)){
	while($row = $result->fetch_row()){
		$fullName = $row[0] . " " . $row[1];
		$facebook = $row[2];
		$twitter = $row[3];
		$linkedIn = $row[4];
		$title = $row[5];
		$position = $row[6];
		$email = $row[7];
		$phone = $row[8];
	}
}

?>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title><?php echo $fullName;?></title>
	<link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.css" rel="stylesheet">
	<link href='http://fonts.googleapis.com/css?family=PT+Sans+Narrow' rel='stylesheet' type='text/css'>
	<link rel="shortcut icon" href="http://www.bidonmoving.com/Resify/Logo/Res_logo_NoCircle_Red.png">
	<!-- Skill Bars -->
	<link href='skillBars.css' rel='stylesheet' type='text/css'>
	<!-- Flat Layout -->
	<link href='flatLayout.css' rel='stylesheet' type='text/css'>
	<!-- MOBILE -->
	<link href='mobile.css' rel='stylesheet' type='text/css'>
	<!-- PRINT -->
	<link href='print.css' rel='stylesheet' type='text/css'>
			
	<script>
	window.onload = function() {
		var element = document.getElementById('right-content');
		var is_chrome = navigator.userAgent.indexOf('Chrome') > -1;
		var is_safari = navigator.userAgent.indexOf("Safari") > -1;
		if ((is_chrome)&&(is_safari)) {is_safari=false;}
		if(is_chrome){
			element.className += " " + 'chrome';
		}
		if(is_safari){
			element.className += " " + 'safari';
		}
		
	};

	</script>

</head>
<body>
	<div class="page">
		<div class="content">
			<div class="rectangle">
				<h2><?php echo $fullName; ?></h2>
			</div>
			<div class="triangle-l"></div> <!-- Left triangle -->
			<div class="triangle-r"></div> <!-- Right triangle -->
			<div class="info">
				<div class="job-title">
					<h2><?php echo $title;?>
						<div class="socials">
							<?php if(isset($facebook)){ ?>
								<!-- FACE BOOK -->
								<a class="btn btn-default" href="<?php echo $facebook; ?>" target="_blank">
									<i class="fa fa-facebook fa-lg fb"></i>
								</a>
								<!-- END FACE BOOK -->
							
							<?php 
							} //END FACEBOOK
							
							if(isset($twitter)) {
							?>
								<!-- TWITTER -->
								<a class="btn btn-default" href="<?php echo $twitter; ?>" target="_blank">
									<i class="fa fa-twitter fa-lg tw"></i>
								</a>
								<!-- END TWITTER -->
							<?php
							} //END TWITTER
							
							if(isset($linkedIn)) {
							?>
								<!-- Linked in-->
								<a class="btn btn-default" href="<?php echo $linkedIn; ?>" target="_blank">
								   <i class="fa fa-linkedin fa-lg in"></i>
								</a>
								<!-- END LINKED IN-->
							<?php 
							} 
							?>
							
						</div>
					</h2> <!-- JOB TITLE -->
				</div>
				<br />
				<br />
				<div class="left-content">
					
					<div class="available">
						<h2 class="left-head" style="width:200px;"><i class="fa fa-bell"></i> Availability</h2>
						<hr id="left">
						<br>
						<h4 class="info">Position</h4> <!-- Years attended -->
						<h3><?php echo $position; ?></h3> <!-- Name -->
						<br>
						<h4 class="info">Email</h4> <!-- Years attended -->
						<h3><?php echo $email; ?></h3>
						<br>
						<h4 class="info">Phone</h4> <!-- Years attended -->
						<h3><?php echo $phone; ?></h3>
					</div>
					
					<br><br>
					<br><br>
					
					<!-- WITH PHP SWITCH TO BE LEFT RIGHT COLUMNS-->
					<div class="skills">
						<h2 class="left-head"><i class="fa fa-tasks"></i> Skill Set</h2>
						<hr id="left">
						
						<div class="progress-bars">
							<?php
								$sql="SELECT skill, value FROM skillSet WHERE userName='". $userName. "'";
								if($result=$conn ->query($sql)){
									while($row = $result->fetch_row()){
										$skill = $row[0];
										$value = $row[1];
							?>
							<br>
								<div class="meterText" id="left-col"><?php echo $skill;?></div>
								<div class="meter" title="<?php echo $skill . ": " .$value;?>%">
									<span style="width: <?php echo $value;?>%"></span>
								</div>
						
							<?php
								 	} //end While
								} //end If
							?>
							
						</div>
					</div>
					<br><br>
					<br><br>
					<div class="accomplishment">
						<h2 class="left-head"><i class="fa fa-check-circle-o"></i> Accomplishments</h2>
						<hr id="left">
						
						<?php
							$sql="SELECT content, date FROM accomplishments WHERE userName='". $userName. "'";
							if($result=$conn ->query($sql)){
								while($row = $result->fetch_row()){
									$content = $row[0];
									$date = $row[1];
						?>
						<br>
						
						<div class="accomplishment-text">
							<h4 class="date"><?php echo $date;?></h4> <!-- Years worked -->
							<h3 class="accomplishment-content"><?php echo $content;?></h3> <!-- content -->
						</div>
						
						<br><br>
						<?php
							 	} //end While
							} //end If
						?>
						
					<br><br>
				</div> <!-- END left content -->
				
				<div id="right-content" class="right-content">
					<div class="personal">
						<h2 class="right-head" id="personalHead"><i class="fa fa-user"></i> Personal Statement</h2>
						<hr id="right">
						<?php
							$sql="SELECT content FROM statement WHERE userName='". $userName. "'";
							if($result=$conn ->query($sql)){
								while($row = $result->fetch_row()){
									$content = $row[0];
								}
							}
						?>
						<p id="right" class="personal"><?php echo $content; ?></p>
					</div>
					
					<br><br>
					<br><br>
					
					<div class="school">
						<h2 class="right-head" id="schoolHead"><i class="fa fa-graduation-cap"></i> Education</h2>
						<hr id="right">
						
						<?php
							$sql="SELECT school, status, date, address FROM education WHERE userName='". $userName. "'";
							if($result=$conn ->query($sql)){
								while($row = $result->fetch_row()){
									$school = $row[0];
									$status = $row[1];
									$date = $row[2];
									$address = $row[3];
						?>
						<br>
						<div class="school-text">
							<h4 class="date"><?php echo $status;?>:<br><?php echo $date;?></h4> <!-- Years attended -->
							<h3><?php echo $school; ?></h3> <!-- Name -->
							<h4><?php echo $address; ?></h4> <!-- ADDRESS -->
						</div>
						
						<br><br>
						<?php
							 	} //end While
							} //end If
						?>

						<br><br>
						
						<div class="employment">
							<h2 class="right-head" id="employmentHead"><i class="fa fa-briefcase"></i> Employment</h2>
							<hr id="right">
							
							<?php
								$sql="SELECT title, employer, date, content FROM jobHistory WHERE userName='". $userName. "'";
								if($result=$conn ->query($sql)){
									while($row = $result->fetch_row()){
										$title = $row[0];
										$employer = $row[1];
										$date = $row[2];
										$content = $row[3];
							?>
							<br>					
							<div class="employment-text">
								<!-- Years worked -->
								<h4 class="date"><?php echo $date; ?></h4>
								<!-- Job title -->
								<h3><?php echo $title; ?></h3>
								<!-- EMPLOYER -->
								<h4><?php echo $employer; ?></h4> 
								<!-- Job Description -->
								<p><?php echo $content; ?></p>
							</div>
							<br><br>
						<?php
							 	} //end While
							} //end If
						?>
						<br><br>
						
					</div>
				</div> <!-- END right content -->
				
			</div> <!-- END info-->
		</div>
		<div class="footer">2014 &copy; Résify</div>
	</div>
</body>
</html>