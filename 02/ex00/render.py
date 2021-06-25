#!/usr/bin/env python3


import sys, os, re

def extract_data():
    res = 0
    if os.path.isfile("settings.py"):
        with open("settings.py", "r") as file:
            sett = file.read()
    if len(sys.argv) == 2:
        templ = sys.argv[1]
        check = re.search(r".template", templ)
        check = re.search(r".template", templ)
        if (check and templ.endswith(".template")):
            with open(templ, "r") as f:
                template = f.read()
                lines = sett.split('\n')
                res = template
                for line in lines:
                    str1 = line.split("=")[0].strip()
                    str2 = line.split("=")[1].strip().strip('"')
                    res = re.sub('\{' + str1 + '\}', str2, res)
    return res

def create_html(data):
    if data != 0:
        res = str(data)
        with open("myCV.html", "w") as HTML_file:
            HTML_file.write(res)

if __name__ == '__main__':
    data = extract_data()
    create_html(data)