# 2016-07-15 Vivek $
# PYTHON MODULE IMPORT
from django.conf import settings
import datetime
import logging as log
import os
import logging.handlers
    
def setLogObj():
    logLevel=20
    logFolderDir=os.path.join(os.getenv("WEB_INSTALL_DIR"),"log")
    if os.path.exists(logFolderDir):
        pass
    else:
        os.mkdir(logFolderDir)
    log.basicConfig ( level=logLevel,
                          format="%(asctime)s - [%(lineno)4d] [%(levelname)-5s] %(message)s [%(filename)s]", 
                          datefmt='%a, %d %b %Y %H:%M:%S',
                          filename=os.path.join(logFolderDir,"webui.log"),                                                    
                          filemode='a+')
    
    return True

statusLogLevel = setLogObj()