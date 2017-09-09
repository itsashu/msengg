import os
from elementtree import ElementTree

def get_config_values(path=None):
    """parse RADSPEED config values"""  
    install_path=None
    if not path:
        install_path=os.getenv("RAD_INSTALL_DIR")

    if not install_path:

        raise IOError,"Environment variable RAD_INSTALL_DIR not defined"

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

#def get_passwordControl_parameter_Obj():
#    install_path=os.getenv("MED_INSTALL_DIR")    
#    if not install_path:
#
#        return None
#    path=os.path.join(install_path,"conf","webappconfig.xml")
#
#    et=ElementTree.parse(path)
#    root=et.getroot()
#    passwordControlObj=root.find("PasswordControl")
#    return passwordControlObj

#def get_parser_config_values():
#    """parse RADSPEED config values"""
#    install_path=os.getenv("MED_INSTALL_DIR")
#    if not install_path:
#       
#        return None
#
#    path=os.path.join(install_path,"conf","ParserConfig.xml")
#
#    et=ElementTree.parse(path)
#    root=et.getroot()
#
#    config={}
#
#    for i in root:
#        config[i.tag]=dict((k.tag,k.text) for k in i)
#
#    return config


def get_event_consumer_config_values():
   """ to parse EVENT CONSUMER CONFIG VALUES """
   
   install_path=os.getenv("RAD_INSTALL_DIR")
   
   if not install_path:

       return None

   path=os.path.join(install_path,"conf","eventconsumer.xml")

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


#def get_plugIn_parameter_Obj():
#
#    install_path=os.getenv("MED_INSTALL_DIR")    
#    if not install_path:
#       
#        return None
#    path=os.path.join(install_path,"conf","webappconfig.xml")
#
#    et=ElementTree.parse(path)
#    root=et.getroot()
#    plugInObj=root.find("STUDYLISTPLUGIN")
#    return plugInObj

#def get_favoriteSearch_config_value():
#    install_path=os.getenv("MED_INSTALL_DIR")    
#    if not install_path:
#       
#        return None   
#    path=os.path.join(install_path,"conf","FavoriteSearch.xml")
#    et=ElementTree.parse(path)
#    root=et.getroot()    
#    config={}
#    SearchList=[]
#    for i in root:
#        d={}
#        config={}
#        for k in i:
#            a=[]
#            if k.__len__() >0:
#                for j in k:
#                    a.append(j.text)
#                k.text=a
#            d[k.tag]=k.text
#        #config[i.tag]=dict((k.tag,k.text) for k in i)
#        config[i.tag]=d
#        SearchList.append(config)
#    #for key in SearchList:
#    #    print key
#    return SearchList
 