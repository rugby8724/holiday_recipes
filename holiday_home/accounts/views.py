from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate

from . import forms


class Signup(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('holiday:home')
    template_name = 'accounts/signup.html'

    #Will auto sign in user after they create an account
    def form_valid(self, form):
        view = super(Signup, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
