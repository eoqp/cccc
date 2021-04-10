import requests
import re
A = '\033[1;10m'
B = '\033[1;30m'
C ='\033[1;36m'
D =('='*40)
print(f"""{A}{D}
<>---<>---<>---<>---<>---<>---<>---<>---<>
[*] Find out hidden paths on the site [*]  
<>---<>---<>---<>---<>---<>---<>---<>---<>        
      >> Naplon ◕_◕ <<
 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |{C}
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| snap: tv-of  
                Telegram: naplon0 
<>---<>---<>---<>---<>---<>---<>---<> 
//Link must contain http or https\\
<>---<>---<>---<>---<>---<>---<>---<>    
{D}""")   
user = str(input('Enter the website link: '))
domains = user +"/robots.txt"

try:
    page = requests.get(domains,"html.parser").text
    hidden = re.findall("Disallow\: \S{1,}",page)

    for i in hidden:
        link = "[*]" + user + i[10:]
        print(link)
        fil = open("blacklink.txt", "a")
        fil.write("\n"+link)
        fil.close()
except:
    pass
