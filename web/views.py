from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json
import collections

# Create your views here.
def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result = collections.OrderedDict()
        result['user']=username
        result['password']=password
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=UTF-8')
    else:
        return render_to_response('login.html')