from django.shortcuts import render
from vendors.meli.meli import Meli
from django.conf import settings
from .models import MeliAccount
import logging
import pprint



def get_callback(request):
    meli = Meli(client_id=settings.MELI_CLIENT_ID, client_secret=settings.MELI_CLIENTE_SECRET)
    code = request.GET['code']
    user = meli.authorize(code=code, redirect_URI=settings.MELI_REDIRECT_URL+'meli_account/get_callback')
    
    account = MeliAccount()
    
    
    logger = logging.getLogger(__name__)
    pp = pprint.PrettyPrinter(indent=4)
    puser = pp.pprint(user)
    return render(request, 'add_account.html', {'puser' : meli.__dict__})

def add_account(request):
    meli = Meli(client_id=settings.MELI_CLIENT_ID, client_secret=settings.MELI_CLIENTE_SECRET)
    url = meli.auth_url(redirect_URI=settings.MELI_REDIRECT_URL+'meli_account/get_callback')
    return render(request, 'add_account.html', {'url': url })

