from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template("stockdetails/stockinfo.html")
    context = {}
    return HttpResponse(template.render(context,request))
    #return render(request, "stockdetails/stockinfo.html", context)

# Create your views here.
