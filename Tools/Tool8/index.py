
mess = """======================================================                           
$$$$$$\ $$\   $$\ $$$$$$$\  $$$$$$$$\ $$\   $$\       $$\      $$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\        
\_$$  _|$$$\  $$ |$$  __$$\ $$  _____|$$ |  $$ |      $$$\    $$$ |$$  __$$\ $$ | $$  |$$  _____|$$  __$$\       
  $$ |  $$$$\ $$ |$$ |  $$ |$$ |      \$$\ $$  |      $$$$\  $$$$ |$$ /  $$ |$$ |$$  / $$ |      $$ |  $$ |      
  $$ |  $$ $$\$$ |$$ |  $$ |$$$$$\     \$$$$  /       $$\$$\$$ $$ |$$$$$$$$ |$$$$$  /  $$$$$\    $$$$$$$  |      
  $$ |  $$ \$$$$ |$$ |  $$ |$$  __|    $$  $$<        $$ \$$$  $$ |$$  __$$ |$$  $$<   $$  __|   $$  __$$<       
  $$ |  $$ |\$$$ |$$ |  $$ |$$ |      $$  /\$$\       $$ |\$  /$$ |$$ |  $$ |$$ |\$$\  $$ |      $$ |  $$ |      
$$$$$$\ $$ | \$$ |$$$$$$$  |$$$$$$$$\ $$ /  $$ |      $$ | \_/ $$ |$$ |  $$ |$$ | \$$\ $$$$$$$$\ $$ |  $$ |      
\______|\__|  \__|\_______/ \________|\__|  \__|      \__|     \__|\__|  \__|\__|  \__|\________|\__|  \__|      
                                                                                                                 
                                                                                                                 
                                                                                                                 
$$$$$$$$\  $$$$$$\  $$$$$$$\        $$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\   $$$$$$\         
$$  _____|$$  __$$\ $$  __$$\       $$ |  $$ |$$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ $$  __$$\        
$$ |      $$ /  $$ |$$ |  $$ |      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |$$ /  \__|       
$$$$$\    $$ |  $$ |$$$$$$$  |      $$$$$$$$ |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |\$$$$$$\         
$$  __|   $$ |  $$ |$$  __$$<       $$  __$$ |$$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$<  \____$$\        
$$ |      $$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |$$\   $$ |       
$$ |       $$$$$$  |$$ |  $$ |      $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |\$$$$$$  |       
\__|       \______/ \__|  \__|      \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__| \______/        
                                                                                                                 
                                                              
(+) Code By: MR SHADOW

Instagram:  @eoq.z
======================================================"""

print mess
title = raw_input("Enter the title: ")
heading = raw_input("Enter the heading text: ")
imagelink = raw_input("Enter the principal image location: ")
bgimage = raw_input("Enter the background image (Optional): ")
message = raw_input("Enter the message(Use <br> to step a line under): ")
textcolor = raw_input("Enter the font color (e.g. white): ")
youtubeid = raw_input("Enter the youtube ID: ")


#Open the index
fo = open("index.html","w")

messagescript1 = """<html><head><title>"""

messagescript2 = title

messagescript3 = """</title></head>
<body>
<br>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Anton' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Josefin Sans' rel='stylesheet' type='text/css'>
<body bgcolor="#000000" background ="""

messagescript4 = bgimage

messagescript5 = """><div class='CenterDiv'>
<center>
<h1><center><font color=\"red\" face=Orbitron>"""

messagescript6 = heading

messagescript7 = """<h1></font>
<img src=""" 

messagescript8 = imagelink

messagescript9 = """ width=450px height=340px>
<body onload="init()"></body>
<body>
<div id="bulle"></div>"""

messagescript10 = """
<script language=\"JavaScript\">
var i=0
var j=0
var texteNE, affiche
var texte=\"<br><br><br><br><br><font face=Orbitron color="""

messagescript11 = textcolor

messagescript12 = """ size=4>"""

messagescript13 = message 

messagescript14 = """<br><br></font><br></b></div>\"
var ie = (document.all);
var ne = (document.layers); 
function init(){
texteNE='';
machine_a_ecrire();
}
function machine_a_ecrire(){
texteNE=texteNE+texte.charAt(i)
affiche='<font face=Orbitron size=1 color=#ffffff><strong>'+texteNE+'</strong></font>'
if (texte.charAt(i)=="<") {
j=1
}
if (texte.charAt(i)==">") {
j=0
}
if (j==0) {
if (document.getElementById) { // avec internet explorer
document.getElementById("bulle").innerHTML = affiche;
}
}
if (i<texte.length-1){
i++
setTimeout("machine_a_ecrire()",70)
}
else
return
}
</script><font face="Orbitron" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b>
<img style="position:fixed;bottom:0px;z-index:1000;right:-10px;"  src="https://3.bp.blogspot.com/-703X8prgI3k/WftGH0TDuvI/AAAAAAAAALE/Sh4VPTgMXoI7MBuperIn-uIVsA9et5z5wCLcBGAs/s1600/ninja.gif" type="image/gif" width="150"></a></body>
<!-- CSS --><style>
.CenterDiv{width:650px;border:1px #ff0000 solid;padding:5px;margin:0px auto; background: url('http://i.imgur.com/sDbaMsW.gif');}
</style>
<br>
<br>
<br>
<iframe width="0" height="0" src="http://www.youtube.com/v/"""

messagescript15 = youtubeid

messagescript16 = """&autoplay=1" frameborder="0"></iframe>"""


fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)

print "\The page has been generated as: index.html"

fo.close()
