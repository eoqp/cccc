list = input('Enter Your List: ')
mark = open(list,'r')
http = open('http_saved','w')
https = open('https_saved','w')
def seperator():
  for line in mark:
    if line.startswith('http://'):
       http.write(line)
    else:
       https.write(line)
seperator()
print('...done')
