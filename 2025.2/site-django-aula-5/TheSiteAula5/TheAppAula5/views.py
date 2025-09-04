from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    # return HttpResponse("Alo mundo")
    return render(request, 'TheAppAula5/home.html')

def segundaPagina(request):
    return render(request, 'TheAppAula5/segundaPagina.html')
