from bs4 import BeautifulSoup
from bs4 import Comment

import datetime
import re
import urllib.request

sitemap = 0
googleThing = 0

nomHTML = "reto3.html"
taglist = ["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track",
           "wbr", "command", "keygen", "menuitem"]
#retorna la data
def date():
    dateNow = datetime.datetime.today().strftime('%Y-%m-%d')
    print("Date: " + dateNow)

def not_semic(href):
    return href and not re.compile("semic.es").search(href) and re.compile("http").search(href)


def not_blank(target):
    return target != "_blank"

def is_js(src):
    return src and re.compile(".js").search(src)

def is_css(href):
    return href and re.compile(".css").search(href)

def checkGoogle(line):
    regex = r"gtag\(\'config\', \'UA-\d{7}-1\'\)"
    regex2 = r"GTM-[a-zA-Z0-9_.-]{6}"
    regex3 = r"<!--"
    global googleThing

    matches3 = re.finditer(regex3, line)
    test = 0
    for matchNum, match in enumerate(matches3):
            test = test + 1
    if test == 0:
        matches = re.finditer(regex, line)
        matches2 = re.finditer(regex2, line)
        for matchNum, match in enumerate(matches):
            googleThing = googleThing + 1
        for matchNum, match in enumerate(matches2):
            if (match.group(0) != "GTM-XXXXXX"):
                googleThing = googleThing + 1

def checkSitemap(line):
    regex = r"sitemap.xml"
    matches = re.finditer(regex, line)
    for matchNum, match in enumerate(matches):
        global sitemap
        sitemap = sitemap + 1

def rule_6(soup):
    enlacesNoSemic = soup.find_all('a', href=not_semic, target=not_blank)
    if (len(enlacesNoSemic) > 0):
        return True
    else:
        return False

def rule_7(soup, jsnum):
    soupcontent = soup.find_all('script', src=is_js)
    jsnum += len(soupcontent)
    if (len(soupcontent) > 0):
        if (jsnum > 5):
            return True, jsnum
    return False, jsnum

def rule_8(soup, cssnum):
    soupcontent = soup.find_all('link', href=is_css)
    cssnum += len(soupcontent)
    if (len(soupcontent) > 0):
        if (cssnum > 5):
            return True, cssnum
    return False, cssnum

def rule_9(soup):
   enlaces = soup.find_all('a')
   if (len(enlaces) > 0):
       for i in enlaces:
           url = i.get('href')
           if url != "" and url != None:
               if url[0] == '/':
                   url = "https://semic.es" + url
                   try:
                       a=urllib.request.urlopen(url)
                       if a.getcode() == 404:
                           return True
                       else:
                           return False
                   except urllib.error.HTTPError:
                           return True
               else:
                   if url[0] == 'h':
                       try:
                           a=urllib.request.urlopen(url)
                           if a.getcode() == 404:
                               return True
                           else:
                               return False
                       except urllib.error.HTTPError:
                           return True
                       except:
                           return False
           else:
               return False
   else:
       return False

def rule_4(number_ocurrences):
    if (number_ocurrences == 0 or number_ocurrences > 1):
        return True
    else:
        return False

def rule_3(number_ocurrences):
    if (number_ocurrences == 0):
        return True
    else:
        return False


def rule_5 (soup):
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for c in comments:
        c = str(c)
        c = c.lstrip(' ')
        if c.find("TODO") == 0 and c.find("TODO") != -1:
            c = c.lstrip('TODO: ')
            return True, c
    s = str(soup)
    s = s.lstrip(' ')
    if s.find("//") == 0 and s.find("TODO: ") == 3:
        s = s.lstrip("// TODO: ")
        s = s.rstrip("\n")
        return True, s
    return False, ""


def rule_2(soup):
    lines = []
    h1dic = {}
    h1set = soup.find_all("h1")
    i = 0
    for h1 in h1set:
        h1dic[h1] = i
        i += 1
    h1set = set(h1set)
    articles = soup.find_all("article")
    sections = soup.find_all("section")
    for article in articles:
        h1sarticle = set(article.find_all("h1"))
        h1set -= h1sarticle
    for section in sections:
        h1ssection = set(section.find_all("h1"))
        h1set -= h1ssection
        
    if (len(h1set) > 0):
        min = -1
        for h1 in h1set:
            if min == -1 or h1dic[h1] < min:
                min = h1dic[h1]
        lines.append(min)

    articlesaux = soup.find_all("article")
    for articleaux in articlesaux:
        articleset = set(articleaux.find_all("h1"))
        articles = articleaux.find_all("article")
        sections = articleaux.find_all("section")
        for article in articles:
            h1sarticle = set(article.find_all("h1"))
            articleset -= h1sarticle
        for section in sections:
            h1ssection = set(section.find_all("h1"))
            articleset -= h1ssection

        if (len(articleset) > 0):
            min = -1
            for h1 in articleset:
                if min == -1 or h1dic[h1] < min:
                    min = h1dic[h1]
            lines.append(min)

    sectionsaux = soup.find_all("section")
    for sectionaux in sectionsaux:
        sectionset = set(sectionaux.find_all("h1"))
        articles = sectionaux.find_all("article")
        sections = sectionaux.find_all("section")
        for article in articles:
            h1sarticle = set(article.find_all("h1"))
            sectionset -= h1sarticle
        for section in sections:
            h1ssection = set(section.find_all("h1"))
            sectionset -= h1ssection

        if (len(sectionset) > 0):
            min = -1
            for h1 in sectionset:
                if min == -1 or h1dic[h1] < min:
                    min = h1dic[h1]
            lines.append(min)

    return lines


with open(nomHTML) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

h1lines = rule_2(soup)
print(h1lines)

f = open("./" + nomHTML, "r")
lines = list(f)

map_lines = {}

jsnum = 0
cssnum = 0

h1index = 0
b = False
print ("File: " + nomHTML)
date()
for i in range(0, len(lines)):
    line = str(lines[i])
    checkSitemap(line)
    checkGoogle(line)
    soup = BeautifulSoup(line, 'html.parser')


    if str(line).find('<!') != -1:
        b = True
    if str(line).find('-->') != -1:
        b = False

    #rule 2
    h1s = soup.find_all("h1")
    for h1 in h1s:
        if h1index not in h1lines:
            if i not in map_lines:
                map_lines[i] = []
            map_lines[i] += ['2']
        h1index += 1

    #rule 5
    rule5bool, comment = rule_5(soup)
    if (rule5bool):
        if i not in map_lines:
            map_lines[i] = []
        map_lines[i] += ['5 ' + comment]

    #rule 6
    if (rule_6(soup)):
        if i not in map_lines:
            map_lines[i] = []
        map_lines[i] += ['6']

    #rule 7
    jsbool, jsnum = rule_7(soup, jsnum)
    if (jsbool):
        if not b:
            if i not in map_lines:
                map_lines[i] = []
            map_lines[i] += ['7']

    #rule 8
    cssbool, cssnum = rule_8(soup, cssnum)
    if (cssbool):
        # print(line)
        if not b:
            # print(i)
            if i not in map_lines:
                map_lines[i] = []
            map_lines[i] += ['8']

    #rule 9
    if (rule_9(soup)):
        if i not in map_lines:
            map_lines[i] = []
        map_lines[i] += ['9']

    rule_5(soup)


if (rule_4(sitemap)):
    if 0 not in map_lines:
        map_lines[0] = []
    map_lines[0] += ['4']

if (rule_3(googleThing)):
    if 0 not in map_lines:
        map_lines[0] = []
    map_lines[0] += ['3']

for key, value in map_lines.items():
    strline = "Line " + str(key) + ": "
    num_rules = len(value)
    i = 0
    for rule in value:
        strline += rule
        if (i < num_rules-1):
            strline += ','
        ++i
    print(strline)

