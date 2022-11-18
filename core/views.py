from django.shortcuts import render

# Create your views here.
def cadastro (request):
    return render (request, 'cadastro.html') 
    
def login (request):
    return render (request, 'login.html')     

def index (request):
    return render (request, 'index.html')        

def produtos (request):
    return render (request, 'produtos.html')   

def detalhes_brinco (request):
    return render (request, 'detalhe_brinco.html')    

def detalhes_capa (request):
    return render (request, 'detalhe_capa.html')     