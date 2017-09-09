import py_compile
import os
import glob
import shutil 

currentDir= os.getcwd()

for f in glob.glob(currentDir + '\\*.py'):
    py_compile.compile(f)
    #shutil.copy(pycFiles, dir)
    print "Success compile the file:   %s" % f

for pycFiles in  glob.glob(currentDir + '\\*.pyc'):
    print pycFiles
    destination = os.path.join(os.getenv("WEB_INSTALL_DIR"), "webMS")
    print destination
    shutil.copy(pycFiles, destination)
    print "Success moved the file:   %s" % pycFiles

apachePath=os.path.join(currentDir , "apache")
#for f in glob.glob(apachePath + '\\*.py'):
#    py_compile.compile(f)
#    #shutil.copy(pycFiles, dir)
#    print "Success compile the file:   %s" % f
    
for pycFiles in  glob.glob(apachePath + '\\*.py'):
    print pycFiles
    destination = os.path.join(os.getenv("WEB_INSTALL_DIR"), "webMS" , "apache")
    print destination
    shutil.copy(pycFiles, destination)
    print "Success moved the apache file:   %s" % pycFiles

  
os.chdir('..')
py_compile.compile("manage.py")
for pycFiles in  glob.glob(os.getcwd() + '\\*.pyc'):
    destination = os.getenv("WEB_INSTALL_DIR")
    shutil.copy(pycFiles, destination)
