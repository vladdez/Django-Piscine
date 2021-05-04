import sys

def read_table():
    with open("periodic_table.txt", "r") as file:
        file = file.read().split('\n')
        tab = {}
        i = 0
        for i in file:
            if i != "":
                tmp = i.split(',')
                elem_pos = tmp[0].split('=')
                elem = elem_pos[0]
                number = tmp[1].split(':')
                small = tmp[2].split(':')
                molar = tmp[3].split(':')
                electron = tmp[4].split(':')
                position = elem_pos[1].split(':')
                tab[elem] = {
                    number[0] : number[1],
                    small[0] : small[1],
                    molar[0] : molar[1],
                    electron[0] : electron[1],
                    position[0] : position[1]
                }
    return tab

def create_table():
    tab = read_table()
    header = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<title>Periodic Table</title>\n<meta charset='utf-8'>\n<style>\ntable, th, tr, td \n{\nborder: 1px solid rgb(198, 35, 157);\nborder-collapse: collapse;\n}\n</style>\n</head>\n<body>\n<h2>Periodic Table</h2>\n<table>\n"
    body = ""
    quad = 0
    for key, val in tab.items():
        a = 0
        if (val[' position'] == "0"):
            s1 = "<tr>"
            body = body + s1
        if (int(val[' position']) != quad + 1):
            a = int(val[' position']) - 1 - quad
            for i in range(a):
                body = body + "<td></td>"
        if (val[' position'] != "17"):
            s1 = "<td><h4>" + str(key) + "</h4>"
            s2 = "<ul><li>" + str(val[' number']) + "</li></ul>"
            s3 = "<ul><li>" + str(val[' molar']) + "</li></ul>"
            s4 = "<ul><li>" + str(val[' small']) + "</li></ul>"
            body = body + s1 + s2 + s3 + s4 + "</td>"
        if (val[' position'] == "17"):
            s1 = "<td><h4>" + str(key) + "</h4>"
            s2 = "<ul><li>" + str(val[' number']) + "</li></ul>"
            s3 = "<ul><li>" + str(val[' molar']) + "</li></ul>"
            s4 = "<ul><li>" + str(val[' small']) + "</li></ul>"
            body = body + s1 + s2 + s3 + s4 + "</td></tr>"
        quad = int(val[' position'])

    res = header + body + "</table>\n</body>\n</html>"
    table_HTML = open("periodic_table.html", "w")
    table_HTML.write(res)
    table_HTML.close()

if __name__ == '__main__':
    create_table()