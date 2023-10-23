#!/usr/bin/python3
''' module for log parsing '''


import sys
total = 0
counter = 0
sc_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
           '403': 0, '404': 0, '405': 0, '500': 0}


def print_data(total):
    ''' function to print statistics for input '''
    print('File size: {}'.format(total))
    for key, value in sorted(sc_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in sys.stdin:
        rline = line.split(" ")
        if len(rline) > 4:
            code = rline[-2]
            if code in sc_dict.keys():
                sc_dict[code] += 1
            filesize = int(rline[-1])
            total += filesize
            counter += 1
        if counter == 10:
            counter = 0
            print_data(total)
except Exception as ex:
    pass
finally:
    print_data(total)
