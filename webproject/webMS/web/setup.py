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
    destination = os.path.join(os.getenv("WEB_INSTALL_DIR"), "web")
    print destination
    shutil.copy(pycFiles, destination)
    print "Success moved the file:   %s" % pycFiles
    
