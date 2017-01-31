from django.shortcuts import render
from ..vendors.meli.meli import Meli
from django.conf import settings


def get_callback(request):
    code = request.GET['code']
    Meli.authorize(code=code, redirect_URI="http://somecallbackurl")

def add_account(request):
    meli = Meli(client_id=settings.MELI_CLIENT_ID, client_secret=settings.MELI_CLIENTE_SECRET)
    url = meli.auth_url(redirect_URI="https://cursosumn.com.br")
    return render(request, 'add_account.html', {'url': url})

