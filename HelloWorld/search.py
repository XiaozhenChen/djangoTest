
from django.http import HttpResponse
from django.shortcuts import render_to_response
 

def search_form(request):
    return render_to_response('search_form.html')
 

def search(request):  
    request.encoding='ascii'
    if 'q' in request.GET:
        message = 'What u search is: ' + request.GET['q']
    else:
        message = 'u have submit'
    return HttpResponse(message)