# i have creared this

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {"name":"raman dahiya","place":"shamli"}
    return  render(request,'index.html')

def about(request):
    return HttpResponse("this is about page")

def remove(request):
    rdxtext = request.GET.get('text','defaultvaluerdx')
    datasend = {"texts" :rdxtext}
    # return HttpResponse(rdxtext)
    return render(request,'result.html',datasend)