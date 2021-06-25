import requests
import json, sys 
from dewiki import parser 

def wiki():
    if len(sys.argv) != 2:
        print("1 argument required")
    else:
        url = 'https://en.wikipedia.org/w/api.php'
        page = sys.argv[1].replace(" ", "_")
        PARAMS = {
            "action": "query",
            "titles": page,
            "format": "json",
            "prop" : "revisions", 
            "rvprop" : "content", 
            "redirects" : ""
                }
        req = requests.get(url=url, params= PARAMS)
        if req.ok != True:
            exit("Error" + req.status_code)
        revisions = json.loads(req.text)['query']["pages"]
        for a, val in revisions.items():
            rev = val.get('revisions')
            if rev is None:
                print("Information not found")
                exit(1)
        page_name = rev[0]['*']
        #res = dewiki.from_string(rev[0]['*'])
        res = parser.Parser().parse_string(page_name)
        with open(page+".wiki ", "w") as file:
            file.write(str(res))
        

if __name__ == '__main__':
    wiki()