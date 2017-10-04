from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.base import View


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return render(request,self.template_name)

    def post(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = "Username password not match"
            return render(request,self.template_name, {'error': error},status=401)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')