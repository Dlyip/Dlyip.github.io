<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="projects.css">
    <title> Contact Danessa </title>
    <link rel="shortcut icon" type ="Biomedical Engineering Favicon" href="favicon.png">
</head>
<header>
    <h1> Contact Me </h1>
</header>
<!--Three Bars-->
    <div id="threebars" class="sidenav">
      <img alt="logo" src="SidebarIcon.png">
      <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times</a>
          <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="http://aer.uci.design/">AER Website (Capstone Project)</a>
      <a href="projects.html">Team Projects</a>
      <a href="solidworks.html">SolidWorks Models</a>
      <a href="programming.html">Programming</a>
      <a href="presentations.html">Presentations</a>
      <a href="documents.html">Documents</a>
      <a href="contact.html">Contact Me</a>
    </div>
    <!--Three Bars Icon -->

    <span style="font-size:30px;cursor:pointer" onclick="openNav()"> &#9776; </span>

    <script>
        function openNav() {
            document.getElementById("threebars").style.display = "block";
        }
        function closeNav() {
            document.getElementById("threebars").style.display = "none";
        }
    </script>
    <!-- Three Bars End -->
<body>
<h3> Let's Connect! </h3>
  <form action="/contact-me.php" method="post" id="contact-form">
    <style>
        h2 {
            margin-bottom: 0px;
            padding-bottom: 0px;
        }
    </style>

    <h2>Contact me</h2>
    <p>Please fill in this form to leave a message for me.</p>

    <label for="fname"><b>First Name</b></label>
    <input type="text" placeholder="First Name" name="fname" id="fname" required> <br> <br>

    <label for="fname"><b>Last Name</b></label>
    <input type="text" placeholder="Last Name" name="lname" id="lname" required> <br> <br>

    <label for="email"><b>E-mail Address </b></label>
    <input type="text" placeholder="Email Address" name="email" id="email" required> <br> <br>

    <label for="email"><b>Company or Organization</b></label>
    <input type="text" placeholder="Company or Organization" name="company" id="company"> <br> <br>

    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="10" cols="70" required> Please type your inquiry here.
    </textarea>

    <p><input type="submit" value="Submit"/></p>

  </form>
	<?php

	$FirstName = addslashes($_POST['fname']);
    $LastName = addslashes($_POST['lname']);
    $Email = addslashes($_POST['email']);
    $Company = addslashes($_POST['company']);
    $Message = addslashes($_POST['message']);
    $GuestBook = fopen("messages.txt", "ab");
    if (is_writeable("messages.txt")){
        if (fwrite("From " . $FirstName . " " . $LastName . " " . "of company/organization" . $Company . ".  Wishes to send you this message:" $Message "\n"))
            echo "<p> Thank you for sending me a message! </p>";}
    fclose($GuestBook); ?>

<h4> Contact Info </h4>
<p>
    Email Me: <a href="mailto:dlyip@uci.edu">dlyip@uci.edu</a></br>
    Phone Number: <a href="tel:1-323-203-8737"> (323)-203-8737 </a></br>
    Connect on LinkedIn: </br> <a href="https://www.linkedin.com/in/danessa-yip/"> https://www.linkedin.com/in/danessa-yip/ </a>
</p>
</body>