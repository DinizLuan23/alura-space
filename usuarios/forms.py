from django import forms

class LoginForms(forms.Form):
   nome_login = forms.CharField( label='Nome de Login', required=True,max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Insira um nome' }) )
   senha = forms.CharField( label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Insira uma senha' }) )

class CadastroForms(forms.Form):
   nome_cadastro = forms.CharField( label='Nome de Cadastro', required=True,max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Insira um nome' }) )
   email = forms.EmailField( label='Email de Cadastro', required=True,max_length=100, widget=forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Insira um email' }) )
   senha = forms.CharField( label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Insira uma senha' }) )
   confirmar_senha = forms.CharField( label='Confirmar Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Confirme sua senha' }) )