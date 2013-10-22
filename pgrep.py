#!/usr/bin/python

import sys
import os
import glob
#import re

if len(sys.argv) != 4:
    print "Usage: pgrep search_word directory file_name"
    exit()

#search_word = re.compile(sys.argv[1])
search_word = sys.argv[1]
directory = sys.argv[2]
file_name = sys.argv[3]

for root, dirs, files in os.walk(directory):
#    print os.path.join(root, "*." + file_name)
    for f in glob.glob(os.path.join(root, "*."+file_name)):
        with open(f) as fp:
            lines = fp.readlines()

        line_number = 0
        for line in lines:
            line_number += 1
            if search_word in line:
#            if search_word.match(line):
                print "%d:%s [%s]" % (line_number, line, os.path.abspath(f))

