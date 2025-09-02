from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    # return HttpResponse("Alo mundo")
    return render(request, 'TheApp/home.html')

def segundaPagina(request):
    return render(request, 'TheApp/segundaPagina.html')
