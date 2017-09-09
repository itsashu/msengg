#!/C:/tools/python23/python.exe
# $Id: buildengine.py 42 2007-11-22 19:37:40Z aaditya $

import os, sys, re

def build_project(name, config, build_command):
    """
    build one specific project returning the status of the build command
    """

    print "\n%s" % ("=" * 80)
    print "%s : %s : %s" % (name,config,build_command)
    cmd=os.popen(build_command)
    output=cmd.readlines()
    result=cmd.close()

    for line in output:
	if re.match(".*up-to-date.*",line,re.I):
	    print ">",line,

    #see if it was a failure, add to list if yesh
    if result and result!=0:
	for line in output:
	    print "| ", line,
    else:
	print "done"

    return result or 0
