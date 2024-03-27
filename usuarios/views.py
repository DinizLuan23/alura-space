from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(req):
   form = LoginForms()

   if req.method == 'POST':
      form = LoginForms(req.POST)

      if form.is_valid():
         nome = form['nome_login'].value()
         senha = form['senha'].value()

         usuario = auth.authenticate(req, username=nome, password=senha)

         if usuario is not None:
            auth.login(req, usuario)
            messages.success(req, f"{nome} Logado")
            return redirect('index')
         else:
            messages.error(req, "Login não efetuado 🥲")
            return redirect('login')
      else:
         messages.error(req, "Login não efetuado 🥲")
         return redirect('login')


   return render(req, 'usuarios/login.html', { 'form': form })

def cadastro(req):
   
   cadastro = CadastroForms()

   if req.method == 'POST':
      form = CadastroForms(req.POST)

      if form.is_valid():
         if form['senha'].value() != form['confirmar_senha'].value():
            messages.error(req, "Senhas divergentes 🥲")
            return redirect('cadastro')
         
         nome = form['nome_cadastro'].value()
         email = form['email'].value()
         senha = form['senha'].value()

         if User.objects.filter(username = nome).exists():
            messages.error(req, "Usuário já existe 🥲")
            return redirect('cadastro')
         
         usuario = User.objects.create_user(username=nome, email=email, password=senha)
         usuario.save()

         messages.success(req, f"{nome} foi cadastrado")
         return redirect('login')

   return render(req, 'usuarios/cadastro.html', { 'cadastro': cadastro })

def logout(req):
   auth.logout(req)
   messages.success(req, 'Logout Efetuado 👌')
   return redirect('login')