from django.contrib import auth, messages
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib.auth import login, logout



# Create your views here.

def submit_login(request):
    if request.method != 'POST':
        return render(request, 'accounts/submit_login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        #messages.sucess(request,'sucesso!')
        return redirect('listar_contato')
    #messages.error(request, 'E-mail ou senha incorreta!')
    return redirect('submit_login')

