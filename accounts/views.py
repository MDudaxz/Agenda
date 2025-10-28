from django.contrib import auth, messages
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.sucess(request,'sucesso!')
        return redirect('listar_contato')
    messages.error(request, 'E-mail ou senha incorreta!')
    return redirect('listar_contato')

