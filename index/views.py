from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

# def login( request ) :
#     return render( request, "login.html")
#
# def join( request ) :
#     return render( request, "join.html")

def information( request ) :
    return render( request, "information.html")

# def 게시판( request ) :
#     return render( request, "게시판.html")
#
# def 상세페이지( request ) :
#     return render( request, "상세페이지.html")
#
# def 수정( request ) :
#     return render( request, "수정.html")
#
# def 글쓰기( request ) :
#     return render( request, "글쓰기.html")

def Introduce( request ) :
    return render( request, "Introduce.html")