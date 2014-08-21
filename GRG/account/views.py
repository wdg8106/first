# Create your views here.
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import User

class UserForm(forms.Form):
    username = forms.CharField(label='userGRG:',max_length=100)
    passworld = forms.CharField(label='passwndGRG:',widget=forms.PasswordInput())
  
def regist(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            user = User()
            user.username = username
            user.passworld = passworld
            user.save()
            return render_to_response('success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})