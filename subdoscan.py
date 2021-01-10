#python2.7
#Author : KimiHmei7 & Zeerx7
#recode boleh asal ngotak goblok. 

# <-- Import Module -->
import os
import json
import requests
from colorama import Fore, init
from multiprocessing.dummy import Pool
from multiprocessing.dummy import Pool as ThreadPool
init(autoreset=True)

def subdoscan(target):
  try:
    grab = requests.get('https://sonar.omnisint.io/subdomains/'+target)
    if 'null' in grab.text:
      print('{}[FAILED] {}'.format(Fore.RED, Fore.YELLOW+target))
    else:
      result = json.loads(grab.text)
      print "{}[GRABBED] {} | Total {} Subdomains".format(Fore.YELLOW, str(target), len(result))
      for domain in result: 
        open('grabbed.txt', 'a').write('http://' + domain + "\n")
      
  except:
      pass

banner = """

\t{}Subdomain Scanner 
\t{}https://github.com/AzhariKun/subdomer

""".format(Fore.WHITE, Fore.YELLOW)
print banner
target = open(raw_input(Fore.WHITE+'input list:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
Thread = raw_input(Fore.WHITE+'Thread :~# ')
pool = ThreadPool(int(Thread))
pool.map(subdoscan, target)
pool.close()
pool.join()