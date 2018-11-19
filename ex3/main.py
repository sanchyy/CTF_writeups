from bs4 import BeautifulSoup
import datetime
import re

nomHTML = "reto3.html"

#retorna la data
def date():
    dateNow = datetime.datetime.today().strftime('%Y-%m-%d')
    print("Date: " + dateNow)

def not_semic(href):
    return href and not re.compile("semic.es").search(href)

def not_blank(target):
    return target != "_blank"


def rule_6(soup):
    enlacesNoSemic = soup.find_all(href=not_semic, target=not_blank)
    if (len(enlacesNoSemic)  > 0):
        return True
    else:
        return False

def rule_2(soup):

    print("nothing")
    
def rule_5 (soup):
    cmnts = soup.find_all("comment")
    if len(cmnts) < 1:
        print("holi")
        return False, ""
    for c in cmnts:
        print(c)
        type(c)
    


with open(nomHTML) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
numh1 = soup.find_all('h1')


f = open("./" + nomHTML, "r")
lines = list(f)


numh1 = 0
for i in range(0, len(lines)):
    line = str(lines[i])
    soup = BeautifulSoup(line, 'html.parser')
    rule_5(soup)










def find_line(tag):
    f = open("./" + nomHTML, "r")
    lines = list(f)
    tagstr = "".join([str(item) for item in tag.contents])

    print(tagstr)
    for i in range(0, len(lines)):
        line = str(lines[i])
        if (i == 3):
            print(tagstr)
            print(line)


        #if (tagstr.find(line) != -1 or line.find(tagstr) != -1):
         #   print(i)
