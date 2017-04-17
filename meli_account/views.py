from django.shortcuts import render
from vendors.meli.meli import Meli
from django.conf import settings
from .models import MeliAccount
from .forms import CopyForm
import logging
import time
from django.contrib.auth.decorators import login_required
import json
import requests
from util.meli_request_exception import MeliRequestExcetion


@login_required
def get_callback(request):
    meli = Meli(client_id=settings.MELI_CLIENT_ID, client_secret=settings.MELI_CLIENTE_SECRET)
    code = request.GET['code']
    user = meli.authorize(code=code, redirect_URI=settings.MELI_REDIRECT_URL+'meli_account/get_callback')
    
    account = MeliAccount()
    account.refresh_token = meli.refresh_token
    account.expires =  time.time() + meli.expires_in
    account.owner = request.user
    account.access_token = user
    
    
    param = {'access_token': user}
    
    req_usuario = meli.get("/users/me", param)
    if req_usuario.status_code != requests.codes.ok:
        raise MeliRequestExcetion('Erro ao capturar informações de usuário')
    
    info_usuario = req_usuario.json()
    account.nickname = info_usuario['nickname']
    account.save()
    
    #account.nickname = info_usuario.nickname
    #account.save()
    return render(request, 'add_account.html', {'puser' : meli.__dict__, 'usrml': info_usuario})

@login_required
def add_account(request):
    meli = Meli(client_id=settings.MELI_CLIENT_ID, client_secret=settings.MELI_CLIENTE_SECRET)
    url = meli.auth_url(redirect_URI=settings.MELI_REDIRECT_URL+'meli_account/get_callback')
    return render(request, 'add_account.html', {'url': url })
    
@login_required
def copy_account(request):
    copia = ''
    if request.method == 'POST':
        form = CopyForm(request.POST,logged_user = request.user)
        if form.is_valid():
            copia_from = form.cleaned_data['copy_from']
            copia_to = form.cleaned_data['copy_to']
    else:
        form = CopyForm(logged_user = request.user)
        #copia = form.cleaned_data['copy_to']
    return render(request, 'copy_account.html', {'form': form, 'user' : copia })

