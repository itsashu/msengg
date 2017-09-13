import os
from elementtree import ElementTree

def get_config_values(path=None):
    """parse RADSPEED config values"""  
    install_path=None
    if not path:
        install_path=os.getenv("WEB_INSTALL_DIR")

    if not install_path:

        raise IOError,"Environment variable WEB_INSTALL_DIR not defined"

    path=os.path.join(install_path,"conf","webappconfig.xml")

    et=ElementTree.parse(path)
    root=et.getroot()

    config={}

    for i in root:
        d={}
        for k in i:
            a={}
            if k.__len__() >0:
                for j in k:
                    a[j.tag]=j.text
                k.text=a
            d[k.tag]=k.text
        #config[i.tag]=dict((k.tag,k.text) for k in i)
        config[i.tag]=d

    return config

