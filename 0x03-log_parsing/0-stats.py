#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


nblines = 0
file_size = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}
try:
    for line in sys.stdin:
        if len(line.split()) > 2:
            lineSpl = line.split()
            nblines += 1
            file_size += int(lineSpl[-1])
            if lineSpl[-2] in dict_sc.keys():
                dict_sc[lineSpl[-2]] += 1
            if nblines == 10:
                print("File size: {}".format(file_size))
                for key, val in sorted(dict_sc.items()):
                    if val != 0:
                        print("{}: {}".format(key, val))
                nblines = 0
finally:
    print("File size: {}".format(file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))
