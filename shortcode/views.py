from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
# Create your views here.
from .models import URL
from .forms import SubmitUrlForm

class urlredirect(View):
    def get(self, request, short):
        obj = URL.objects.get(short=short)
        # return HttpResponse("This is the url: {i}".format(i=obj))
        return HttpResponseRedirect(obj)


class urlview(View):
    def get(self, request):
        form = SubmitUrlForm()
        context = {
            "title": "Url Shortener",
            "form": form
        }
        return render(request, 'home.html', context)

    def post(self, request):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Url Shortener",
            "form": form
        }
        template = "home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = URL.objects.get_or_create(url=new_url)
            context = {
                "obj": obj,
                "created": created,
            }
            if created:
                template = "success.html"
            else:
                template = "already_exists.html"

        return render(request, template ,context)
