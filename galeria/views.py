from django.shortcuts import render

dados = {
   1: {
      "nome": "Nebulosa de Carina",
      "legenda": "webbtelescope.org/ NASA / James Webb"
   },
   2: {
      "nome": "Nebulosa de Carina",
      "legenda": "webbtelescope.org/ NASA / James Webb"
   }
}

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')