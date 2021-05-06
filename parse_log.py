import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)


def readlog(path):
    with open(path, "r", encoding="utf-8") as f:    
        f.readline()
        line = f.readline()
        while line:
            line = f.readline()
            newline = line.strip().split()
            if line != []:
                print(newline)


readlog("planning.log")
