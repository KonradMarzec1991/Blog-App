from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm


class LoginUser(View):
    template_name = 'posts/login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.error(request, 'You typed wrong credentials. Please try again')
            return redirect('login')


class LogoutUser(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('home')


class RegisterUser(View):
    template_name = 'posts/register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            messages.success(request, 'You have registered yourself, now you can log in')
            return redirect('login')
        else:
            form = SignUpForm()
            messages.error(request, 'Wrong data - please fill fields again')
            return render(request, self.template_name, {'form': form})
