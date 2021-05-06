import logging
import collections
import math
import datetime
import sys

logging.basicConfig(filename='example2.log', level=logging.DEBUG)
arg = sys.argv[1]
hours, matters, minutes = [], [], []


def open_file(arg):
    with open(arg) as f:
        lines = f.read().strip()
        for line in lines.split("\n"):
            if line != "":
                hours.append(line[0:11])
                matters.append(line[12:])
    return hours


def times(hours):
    hours = open_file(arg)
    for hour in hours:
        hour = hour.split("-")
        time1 = datetime.datetime.strptime(hour[0], "%H:%M")
        time2 = datetime.datetime.strptime(hour[1], "%H:%M")
        time = time2 - time1
        logging.info(time.seconds//60)
    return time.seconds//60


# for hour in hours:
#     hour = hour.split("-")
#     time1 = hour[0]
#     time2 = hour[1]
#     test = datetime.datetime(time2 - time1)
#     minutes.append((int(time2[0:2])-int(time1[0:2]))*60 + (int(time2[3:5])-int(time1[3:5])))
#     logging.info(test)
#     logging.info(minutes)

res = 0
for minute in minutes:
    res += minute
# print(res)
result = list(zip(minutes, matters))
# print(result[1][1])
results = {}
resz = 0
res1 = ""
# for minute, matter in result:
#     results[matter] = resz
#     results = dict(sorted(results.items()))
#     logging.info(results)
#     if matter in results:
#         logging.info(minute)
#         logging.info(matter)
#         res1 += str(minute)
#         results[matter] = res1
#         logging.info(results)


# print(results)
# if __name__ == '__main__':

