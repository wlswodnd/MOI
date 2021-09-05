from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Introduce( request ) :
    return render( request, "Introduce.html")

def Seoul( request ) :
    return render( request, "Seoul.html")

def Jeju( request ) :
    return render( request, "Jeju.html")

def Busan( request ) :
    return render( request, "Busan.html")

def Jeonju( request ) :
    return render( request, "Jeonju.html")

def Gyeongju( request ) :
    return render( request, "Gyeongju.html")

def information( request ) :
    return render( request, "information.html")