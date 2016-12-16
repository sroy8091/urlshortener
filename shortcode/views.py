from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
from .models import URL

class urlview(View):
    def get(self, request):
        return render(request, 'home.html', {})
