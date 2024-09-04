from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class LoginView(View):
    def get(self, request):

        if request.user.is_authenticated:

            return HttpResponseRedirect(reverse_lazy("home"))

        return render(request, "auth/login.html")

    def post(self, request):
        req = request.POST.dict()
        username = req.get("username")
        password = req.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy("home"))
        else:
            return render(
                request,
                "auth/login.html",
                {
                    "error_nouser": True,
                },
            )

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):

        logout(request)

        return HttpResponseRedirect(reverse_lazy("login"))
 
