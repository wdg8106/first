# Create your views here.
#test
from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import User
import random
import json

class UserForm(forms.Form):
    username = forms.CharField(label='userGRG:',max_length=100)
    password = forms.CharField(label='passwndGRG:',widget=forms.PasswordInput())
  
def regist(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            print password
            user = User()
            user.username = username
            user.password = password
            user.save()
            return render_to_response('success.html',{'username':user.password})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})
def login(request):
    data=None
    if request.method=="POST":
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                token=random.randint(100,10000)
                request.session["token"]=token
                data={"result":True,"token":token}
                #return HttpResponse(json.dumps(data),content_type="application/json")
                jsons=json.dumps(data)
                return render_to_response('success.html',{'username':username,'data':json})
            else:
                data={"result":False,"message":"error"}
                return HttpResponse(json.dumps(data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({{"result":False,"message":"error data"}}))
    else:
        uf = UserForm()
        return render_to_response('login.html',{'uf':uf})
def test(request):
    if request.method=="POST":
        jsonTest=request.POST['jsonTest']
        return HttpResponse(jsonTest)
    else:
        return HttpResponse(json.dumps({"message":"isn't POST"}))
        

