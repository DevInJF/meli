from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls.base import reverse

from .forms import LoginForm
from ads.views import index

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if(request.POST.get('next',False)):
                    return redirect(request.POST['next'])
                else:
                    return redirect(reverse('ads:ads_list'))
            else:
                return render(request,'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
