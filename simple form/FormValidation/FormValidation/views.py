from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import SignUpForm

def home(request):
    if request.method == 'GET':
        title = 'Welcome'
        form = SignUpForm()
        context = {
            "title":title,
            "form": form
        }
        return render(request, "home.html", context)

    if request.method == "POST":
        title = 'Welcome'
        form = SignUpForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['email']
            context = {
                "title":title,
                "form": form,
                "text": text
            }
        else:
            context = {
                "title":title,
                "form":form
            }
        return render(request, "home.html", context)
