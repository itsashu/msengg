import parseconfig
from logconf import *
from django.shortcuts import get_object_or_404, render,resolve_url

log.info("controller start up")

radconfig=parseconfig.get_config_values()
log.info("Config:%s" , radconfig)

def home(request):
    """ This function loads home page."""
    return render(request, "homepage.html")

def catalog(request):
    """ This function loads home page."""
    return render(request, "catalog.html")

def index(request,some_data):
    """ This function handles redirection of user to their profiles based on login. """

    return HttpResponseRedirect('/home')