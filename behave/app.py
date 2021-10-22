from flask import Flask
app = Flask(__name__)

@app.route("/")
def hallo_wereld():  
	return '''<!DOCTYPE html>
<html lang="nl">
	<head data-pageid="p000_000_006">
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width minimum-scale=1.0 maximum-scale=1.0 user-scalable=no">
		
		<title>CMS 2.0</title>
		
		<script>
			if (window.devicePixelRatio > 1) { document.cookie='resolution='+Math.ceil(document.documentElement.clientWidth*window.devicePixelRatio*0.875)+'; path=/';
			} else { document.cookie='resolution='+document.documentElement.clientWidth+'; path=/'; }
		</script>
		
		<link rel="stylesheet" href="/site-assets/css/stylesheet.css">
		<link rel="stylesheet" href="/site-assets/css/s/gebruikersbeheer.css">
		
		<script src="/site-assets/js/xlsx.fortsa.min.js"></script>
		<script src="/site-assets/js/multipage.2.0.min.js"></script>
	
	</head>
	<body>
		<main id="page" data-anchor="backtothetop">
			<header id="header">
				
				<a class="mainmenu inactive" href="#mainmenu"></a>
				<a class="sidemenu inactive" href="#sidemenu"></a>
				
				<p>CMS 2.0</p>
				
				<nav id="sidemenu">
					<ul id="prepended-sidemenu"></ul>
				</nav>
				
				<nav id="mainmenu">
					<ul id="prepended-mainmenu"></ul>
				</nav>
				
			</header>
			
			<img id="testimage" src="/site-assets/css/imgs/testimage.jpg" width="1024" height="1" alt="">
			<div id="breadcrumb"><div class="content"><a href="/">Home</a> &rsaquo; dashboard</div></div>
			
			<section>
			
				<section id="content" >
					
					<article class="main-content" >
						
						<header>
							<h1 class="xl">Dashboard</h1>
						</header>
						
						<article class="main-column full-width" id="custom-content">
							<div id="appendtable"></div>
							
							
						</article>
						
						<section class="asides">
							<aside><p>Aside 1</p></aside>
						</section>
						
						<article class="main-column">
							<p><strong>This is a demo 1bbb.</strong><br />Click the hamburger icon to open the menu.</p>
							<p><strong>This is a demo.</strong><br />Click the hamburger icon to open the menu.</p>
						</article>
						
						<aside><p>Aside 2</p></aside>
						
						<footer>
							<p>Content footer</p>
							<button class="save" onclick="saveOpened()" disabled>Wijzigingen opslaan</button>
						</footer>
						
					</article>		
			
				</section>
				
			</section>
			
			<footer>
				<div id="navigation">
					<ul id="footermenu" class="dashboard">
						<li class="loading"><img src="/site-assets/css/imgs/loadingwhite.svg" width="30" height="30" alt="loading">Loading &hellip;</li>
					</ul>
				</div>
				<div id="liability">
					<a id="backtothetop" href="#" onclick="linkHandler('backtothetop'); return false;"></a>
				</div>
				<div id="copyright">
					<div class="content">
						<a class="popup" href="#copyright-popup">&copy;</a> <a href="https://houtdatwerkt.nl" target="_blank">Hout<em>datwerkt</em></a> &boxv; <a class="popup" href="#copyright-popup">copyright</a> &boxv; <a href="/meer-informatie/disclaimer/">disclaimer</a>
					</div>
				</div>
			</footer>
			
		</section>
		
		
						
	</body>
	
<!-- 	<script src="/site-assets/js/helper/blob.js"></script> -->
<!-- 	<script src="/site-assets/js/helper/fileSaver.js"></script> -->
	<script src="/site-assets/js/s/dashboard.js"></script>

</html>'''