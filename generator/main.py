import requests
import os
from bs4 import BeautifulSoup
domains = []
URL = 'https://generator.email'

repeat = 3

for i in  range(repeat) :
  page = requests.get(URL)


  soup = BeautifulSoup(page.content, 'html.parser')

  results = soup.find(id="domainName2")
  if domains.__contains__(results['value']):
    1
  else:
    domains.append(results['value'])

print(domains)


# os.system('mkdir clone && cd clone')
stream = os.popen("git clone https://github.com/DPLYR-dev/disposable-emails-list-domains-spam clone")
output = stream.read()
# print(output)

print ("REPO CLONED")

for i in domains:
  hs = open("clone/domains.txt", 'a')
  hs.write(i+ "\n")
  hs.close()



streamo = os.system("cd clone && git add . ")

streamo = os.popen("cd clone && git commit -m 'Add new domains ex " + domains[0] + "'")
outputo = streamo.read()

print(outputo)

streamt = os.popen("cd clone && git push -u origin master")
outputt = streamt.read()
print(outputt)

os.system("rm -rf ./clone")