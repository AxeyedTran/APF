__Author__ = "Axeyed Tran"
__Version__ = "1.2"
#=====Setting=====#
import os, requests, threading, argparse
os.system("cls" if os.name == "nt" else "clear")
#=====Argument=====#
kali = argparse.ArgumentParser() 
kali.add_argument("-u", help="target url", dest='target')
kali.add_argument("--path", help="custom path prefix", dest='prefix')
kali.add_argument("--type", help="set the type i.e. html, asp, php", dest='type')
kali.add_argument("--fast", help="uses multithreading", dest='fast', action="store_true")
args = kali.parse_args() 
target = args.target 
#=====Banner=====#
print ('''
\033[1;97m             _           _         _____                 _    _____ _           _   
\033[1;96m    /\      | |         (_)       |  __ \               | | |  ____(_)         | |    
\033[1;92m   /  \   __| |_ __ ___  _ _ __   | |__) |_ _ _ __   ___| | | |__   _ _ __   __| | ___ _ __
\033[1;93m  / /\ \ / _` | '_ ` _ \| | '_ \  |  ___/ _` | '_ \ / _ \ | |  __| | | '_ \ / _` |/ _ \ '__| 
\033[1;97m / ____ \ (_| | | | | | | | | | | | |  | (_| | | | |  __/ | | |    | | | | | (_| |  __/ |
\033[1;96m/_/    \_\__,_|_| |_| |_|_|_| |_| |_|   \__,_|_| |_|\___|_| |_|    |_|_| |_|\__,_|\___|_|
\033[1;92m        @AxeyedTran                                                Version 1.2                                                            
''')
print ('\033[1;97m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
#=====Target Website=====#
try:
    target = target.replace('https://', '')
except:
    print('\033[1;91m[!] -u Argument Is Not Supplied. Type python APF.py -h For Help\033[1;97m')
    exit()
target = target.replace('http://', '')
target = target.replace('/', '')
target = 'http://' + target 
if args.prefix != None:
    target = target + args.prefix
try:
    r = requests.get(target + '/axeyed.txt') 
    if '<html>' in r.text: 
        print('\033[1;91m[!] axeyed.txt Not Found\n')
    else: 
        print('\033[1;91m[!] axeyed.txt Found. Check For Any Interesting Entry\n')
        print(r.text)
except:
    print('\033[1;91m[-] axeyed.txt Not Found\n')
print ('\033[1;97m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
#=====Scan=====#
def scan(links):
    for link in links:
        link = target + link 
        r = requests.get(link) 
        http = r.status_code 
        if http == 200: 
            print('\033[1;97m[*] Admin Panel Found: %s'% link)
        elif http == 404: 
            print ('\033[1;97m[*] %s'% link)
        elif http == 302:
            print ('\033[1;97m[*] Potential EAR Vulnerability Found : ' + link)
        else:
            print ('\033[1;97m[*] %s'% link)
#=====Get Path=====#
paths = [] 
def get_paths(type):
    try:
        with open('list-scan.txt','r') as wordlist:
            for path in wordlist: 
                path = str(path.replace("\n",""))
                try:
                    if 'asp' in type:
                        if 'html' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'php' in type:
                        if 'asp' in path or 'html' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'html' in type:
                        if 'asp' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                except:
                    paths.append(path)
    except IOError:
        print('\033[1;91m[!] Wordlist Not Found!')
        exit()
#=====Run=====#
if args.fast == True: 
    type = args.type 
    get_paths(type) 
    paths1 = paths[:len(paths)/2] 
    paths2 = paths[len(paths)/2:] 
    def part1():
        links = paths1 
        scan(links) 
    def part2():
        links = paths2 
        scan(links) 
    t1 = threading.Thread(target=part1) 
    t2 = threading.Thread(target=part2)
    t1.start()
    t2.start()
    t1.join() 
    t2.join()
else:
    type = args.type
    get_paths(type)
    links = paths
    scan(links)