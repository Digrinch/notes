from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import SignUpForm


# Create your views here.
class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('tasks:index')
    template_name = 'users/signup.html'
