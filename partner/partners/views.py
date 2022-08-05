from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from partners.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'signin.html'
    print("oooo")
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        print("yyyyy")
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            print('kerr')
            return HttpResponseRedirect("/")
        else:
            print(form.errors)
            return render(request, self.template_name, {'form':form})

