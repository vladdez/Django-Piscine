import requests, sys
from bs4 import BeautifulSoup

def road():
    if (len(sys.argv)) != 2:
        exit("1 arguments is required")
    start = sys.argv[1]
    url = "https://en.wikipedia.org/wiki/" + start
    if start == 'Philosophy':
        print('0 roads from Philosophy to philosophy !')
    else:
        r = 1
        roads = [start]
        try:
            while True:
                r += 1
                req = requests.get(url)
                if req.status_code != 200:
                    exit("Server error")
                if req.text is None:
                    exit("No text")
                soup = BeautifulSoup(req.text, "html.parser")
                title = soup.find('title').string.split("-")[0].strip()
                if title == 'Philosophy':
                    break
                paragraphs = soup.find_all('div', {'class' : "mw-parser-output"})[0].find_all('p')
                nexturl = False
                for paragraph in paragraphs:
                    open_parenth = 0
                    for token in paragraph.contents:
                        if not nexturl: 
                            if ('(' in token):
                                open_parenth = 1
                            if (')' in token):
                                open_parenth = 0
                            if open_parenth != 1:
                                try:
                                    t = token['title']
                                    if t.startswith('Wiki') == False and t.startswith('Help:') == False:
                                        if t in roads:
                                            exit("It leads to an infinite loop !")
                                        else:
                                            nexturl = True
                                            url = t
                                            roads.append(t)
                                except:
                                    pass 
                url = "https://en.wikipedia.org/wiki/" + t
            for i in roads:
                print(i)
            print(r, 'roads from', start, 'to philosophy !')
        except:
            print("It's a dead end !")


if __name__ == '__main__':
    road()