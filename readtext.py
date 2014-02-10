#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************/
# Read Text Written in Python Ver:1.1                   2014.02.11 monotone-RK/
#*****************************************************************************/
import os
import sys
import datetime
import argparse
import subprocess


def readText(textfiles):
    readcnt = 0
    for textfile in textfiles:
        if not os.path.isfile(textfile):
            print "## Error! No such file: " + textfile
            break
        elif textfile == sys.argv[0]:
            print "## Error! This argument is a not text file!"
            print "## This is own file: " + textfile
            break
        readcnt += 1
        print "Text file: " + textfile
        print "Read count:", readcnt
        print "Date:", datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        tfile = open(textfile, "r")
        text = tfile.read()
        tfile.close()
        print "Contents"
        print "=" * 80
        print text,
        print "=" * 80
        sys.stdout.write("Now reading...")
        sys.stdout.flush()
        subprocess.call('say "%s"' % (text), shell=True)
        sys.stdout.write("Finish\n")
        sys.stdout.flush()
        print

argparser = argparse.ArgumentParser()
argparser.add_argument("-v", "--version", action="version",
                       version="Read Text Written in Python v1.1  last upated:2014.02.11")
argparser.add_argument("textfile", metavar="textfile", nargs="+",
                       help="text file you want to make be read by say command")
args = argparser.parse_args()

if __name__ == "__main__":
    try:
        readText(args.textfile)
    except:
        print "This script is halted"
        sys.exit()
