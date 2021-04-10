#~ Shadow-Framework
#~ Coded by Shadow Hacker
#~ 2021 PRIV8 TOOL
#~ Good Luck :)
import requests,os
from colorama import Fore,init
init(autoreset=True)

g = Fore.GREEN
r = Fore.RED
b = Fore.RED
w = Fore.GREEN

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
banner = """
{}


 _____ _               _                     ______                                           _    
/  ___| |             | |                    |  ___|                                         | |   
\ `--.| |__   __ _  __| | _____      ________| |_ _ __ __ _ _ __ ___   _____      _____  _ __| | __
 `--. \ '_ \ / _` |/ _` |/ _ \ \ /\ / /______|  _| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
/\__/ / | | | (_| | (_| | (_) \ V  V /       | | | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
\____/|_| |_|\__,_|\__,_|\___/ \_/\_/        \_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
                                                                                                   
                                                                                                                                                                                            
 {}[{}+{}] Insta :  @Eoq.z
 {}[{}+{}] Github : https://github.com/eoqp

 {}=============================={}
 [{}1{}] Dork Maker
 [{}2{}] Dork Scanner
 [{}3{}] http_extract
 [{}4{}] IP From Domins
 [{}5{}] Cms Filter
 [{}6{}] Amazon Email Cheaker
 [{}7{}] Paypal Email Cheaker
 [{}8{}] Index Maker For Hackers 
 [{}9{}] Numscan2
 [{}10{}] Exract The Hidden Paths OF The Site 
 [{}11{}] SQLi SCANNER

"""
print(banner.format(g,b,g,w,r,b,g,r,g,r,g,r,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g))
tool = input("choose:")
if tool == "1":
	os.chdir("Tools/Tool1")
	os.system("python3 dorkmaker.py")
	
elif tool == "2":
	os.chdir("Tools/Tool2")
	os.system("python3 dorkscanner.py")
	
elif tool == "3":
	os.chdir("Tools/Tool3")
	os.system("python3 http_extract.py")
		
elif tool == "4":
	os.chdir("Tools/Tool4")
	os.system("python ipfromdomain.py ")
	
elif tool == "5":
	os.chdir("Tools/Tool5")
	os.system("python cms.py")
		
elif tool == "6":
	os.chdir("Tools/Tool6")
	os.system("python2 amazon.cheacker.py")
	
elif tool == "7":
	os.chdir("Tools/Tool7")
	os.system("python check.py")
	
	
elif tool == "8":
	os.chdir("Tools/Tool8")
	os.system("python2 index.py")
	
elif tool == "9":
	os.chdir("Tools/Tool9")
	os.system("python3 num.py")
	
elif tool == "10":
	os.chdir("Tools/Tool10")
	os.system("python3 BlackWeb.py")
	
elif tool == "11":
	os.chdir("Tools/Tool11")
	os.system("php sqli-mass-scanner.php")
