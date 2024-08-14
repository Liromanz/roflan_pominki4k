from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home_page(request):
    return render(request, 'docsite/index.html')

@login_required
def getting_started_page(request):
    return render(request, 'docsite/1getting_started.html')