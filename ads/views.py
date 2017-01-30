from django.shortcuts import render
from vendors.meli.meli import Meli


def index(request):
    meli = Meli(client_id=7330605392252389, client_secret="pJ0LqBVTy4zEURTeoIHfU83TzsRfmhGu")
    url = meli.auth_url(redirect_URI="https://cursosumn.com.br")
    return render(request,'teste.html', {'url': url})
