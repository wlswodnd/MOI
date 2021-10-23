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

def map( request ) :
    return render( request, "map.html")

def Daegu( request ) :
    return render( request, "Daegu.html")

def Gangneung( request ) :
    return render( request, "Gangneung.html")

def Sokcho( request ) :
    return render( request, "Sokcho.html")

def Cheonan( request ) :
    return render( request, "Cheonan.html")

def Boryeong( request ) :
    return render( request, "Boryeong.html")

def Gwangju( request ) :
    return render( request, "Gwangju.html")

def Incheon( request ) :
    return render( request, "Incheon.html")

def Mokpo( request ) :
    return render( request, "Mokpo.html")

def ChunCheon( request ) :
    return render( request, "ChunCheon.html")

def Wonju( request ) :
    return render( request, "Wonju.html")