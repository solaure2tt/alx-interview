#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def validate_ip(s):
    """ verify if s is a valid IP address"""
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def verifyFormat(line):
    """ verify if a format of a current line is correct
        args:
          line: lins to verify the format
        return:
          0 if the format is not correct otherwise 1
    """
    if line is None:
        return 0
    lineSplit = line.split()
    """if len(lineSplit) != 6:
        return 0
    if validate_ip(lineSplit[0]) == False:
        return 0
    if lineSplit[1] != '-':
        return 0
    if isinstance(lineSplit[2], datetime.datetime) == False:
        return 0
    if lineSplit[3] != "GET /projects/260 HTTP/1.1":
        return 0
    status = [200, 301, 400, 401, 403, 404, 405, 500]
    if lineSplit[4] not in status:
        return 0
    if isinstance(lineSplit[-1], int) == False:
        return 0"""
    return 1


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
                print("File size: {}".format(nblines))
                for key, val in sorted(dict_sc.items()):
                    if val != 0:
                        print("{}: {}".format(key, val))
                nblines = 0
finally:
    print("File size: {}".format(nblines))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))
