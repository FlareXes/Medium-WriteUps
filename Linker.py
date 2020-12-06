from bs4 import BeautifulSoup
import requests, urllib, os, argparse
import terminal_banner, termcolor, platform, datetime

op = ''

if platform.system() == 'Windows':
    os.system('cls')
if platform.system() == 'Linux':
    os.system('clear')


def create_url(query,count='10'):
    global url
    url = "https://medium.com/search/posts?q="+urllib.parse.quote(query)+"&count="+count
    

def medium():
    global query
    global op
    create_url(query, count)
    print("[+] Finding %s articles on medium..."%count)

    try:
        page = requests.get(url)
    except requests.ConnectionError:
        print("[-] Can't connect to the server. Check internet connection.")
        exit()

    soup = BeautifulSoup(page.content, 'html.parser')
    print("[+] FOUND")
    print("[+] Listing Acticles...")

    for divs in soup.find_all('div',class_='postArticle-content'):
        for anchors in divs.find_all('a'):
            for h3 in anchors.find_all('h3'):
                try:
                    op = "-"*70 + "\n" + h3.contents[0] + ": " + anchors['href'] + "\n"
                    print(op)
                except :
                    pass
    


argp = argparse.ArgumentParser(usage= "Linker.py -q QUERY -c [COUNT] -o [OUTPUT]")
argp.add_argument("-q","--query",required=True)
argp.add_argument("-c","--count")

parser = argp.parse_args()

query = parser.query
count = parser.count

if count == None: count = '10'

medium()