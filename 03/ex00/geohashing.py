import sys
from antigravity import geohash

def make_geo():
    if (len(sys.argv) != 4):
        print("3 arguments are required")
    else:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        datedow = sys.argv[3]
        return(geohash(x, y, datedow.encode('utf-8')))


if __name__ == '__main__':
    make_geo()