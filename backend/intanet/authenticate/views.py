
from django.shortcuts import render,HttpResponse



def test(request):
 
    return HttpResponse("""<h1 style="color:blue">Welcome to Intanet</h1>""",status=200) 