#!/C:/tools/python23/python.exe
# $Id: rebuild-all-release.py 14108 2016-10-18 12:02:44Z vivek $
#
# Python script for building projects in RadSpeed

import os
import sys
from buildengine import *

build_configs = [ 'Release' ]

#format is 
#   build_order:{'name':'project name', 'path':'solution_path_relative_to_RadSpeed_dir'}
solutions = {
		
    100: {'name':'web',          'command':'echo %s %s && cd webMS/web && cmd /c call build-web.bat', 'path': 'build','type':'C++'} ,
    101: {'name':'setting',          'command':'echo %s %s && cd webMS/webMS && cmd /c call build-setting.bat', 'path': 'build','type':'C++'} ,   
    }
#list of projects which failed
failures={}

# we want to do builds in order
buildid_list=list(solutions)
buildid_list.sort()

print "== Re - Building projects for ", build_configs, "\n"


exit_loop=0

#now do builds
#for each project id
for id in buildid_list:
#    print "=== Doing %s builds ===" % (config)

    if exit_loop==1:
        break

    fail_list=[]
    #by config
    for config in build_configs:

        if exit_loop==1:
            break

        #for convenience
	type=solutions[id]['type']
        name=solutions[id]['name']
        path=solutions[id]['path']
        command=solutions[id]['command']

        if type == "C++":
	    config_path = '"'+config +'|Win32'+'"'
            build_command = command % (config_path,path)
	else :
	    build_command = command % (config,path)
	result=build_project(name, config, build_command)
	
        #see if it was a failure, add to list if yesh
        if result and result!=0:
            print '\n === ERROR: building %s failed === ' % (name)
            fail_list.append(id)
            inp=raw_input("(c)ontinue or (a)bort?")
            if inp=='a' :
                exit_loop=1
                #sys.exit(0)
            if inp=='c':
                continue

    if fail_list:
        failures[config]=fail_list

#print a list of failures, sorted by config
print "\n\n"
for config in failures:
    fail_list=failures[config]
    print '%s:' % (config)
    for fail in fail_list:
    	build_command = 'devenv.com /build %s %s' % (config,solutions[fail]['path'])
        print '   FAILED: %s : %s' % (solutions[fail]['name'],build_command)

inp=raw_input("press enter to continue")

