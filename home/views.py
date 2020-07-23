from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils.http import is_safe_url, urlunquote

from datetime import datetime

from .forms import LoginForm


# Index_full just for example. That can be used too
def index_full(request):
    
    current_time = datetime.now()
    context = {
        'current_time': current_time
    }
    
    template = loader.get_template('home/index.html')
    text = template.render(context, request)
    
    return HttpResponse(text)


def index(request):    
    current_time = datetime.now()    
    return render(request, 'generic.html', locals())


def login_user(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        alogin = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(request, username=alogin, password=password)
        if user is not None:
            login(request, user)
    way = request.META.get('HTTP_REFERER')
    if way:
        way = urlunquote(way)
    if not is_safe_url(url=way, allowed_hosts=request.get_host()):
        way = reverse('home:index')
    return HttpResponseRedirect(way)

def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('home:index'))

# How to write cookies
# request.session['my-cookie'] = 'My Cookie Value'