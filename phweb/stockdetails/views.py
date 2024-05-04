from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests

from .Settings.development import APIURL


def index(request,symbol):
    headers = {"Content-Type": "application/json"}
    postData = { "stockdetails": { "symbol": symbol.upper()}}
    stockDetailsapi = APIURL+'/stocksdetails/'
    response = requests.post(stockDetailsapi, headers=headers, json=postData)
    stockData = {}
    for res in response.json():
        stockData = res

    template = loader.get_template("stockdetails/stockinfo.html")
    #print(response.json())
    context = {"stockinfo":stockData}
    #return HttpResponse(template.render(context,request))
    return render(request, "stockdetails/stockinfo.html", context)

# Create your views here.
