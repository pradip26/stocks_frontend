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


    resultDetailsapi = APIURL + '/resultDetails/'
    resultpostData = {"resultinfo": {"symbol": symbol.upper(),"result_type": "all"}}
    resultData = requests.post(resultDetailsapi, headers=headers, json=resultpostData)
    resultDataJson = resultData.json()
    lastKeyData = list(resultDataJson)[-1]
    if 'profit_after_tax' in lastKeyData:
        profitAfterTax = lastKeyData['profit_after_tax']
    else:
        profitAfterTax = 0

    corpActionDetailsapi = APIURL + '/corpActions/'
    corpActionpostData = {"stockdetails": {"symbol": symbol.upper()}}
    corpActionData = requests.post(corpActionDetailsapi, headers=headers, json=corpActionpostData)
    corpActionDataJson = list(corpActionData.json())[:6]

    peersDetailsapi = APIURL + '/peersList/'
    peersPostData = {"stockdetails": {"industry": stockData['industry']}}
    peersData = requests.post(peersDetailsapi, headers=headers, json=peersPostData)
    peersDataJson = peersData.json()

    topStocksapi = APIURL + '/topScoresList/'
    topStockPostData = {}
    scoreData = requests.post(topStocksapi, headers=headers, json=topStockPostData)
    scoreDataJson = scoreData.json()

    stockScoreapi = APIURL + '/getScore/'
    scorepostData = { "stockdetails": { "symbol": symbol.upper()}}
    stockScoreData = requests.post(stockScoreapi, headers=headers, json=scorepostData)
    stockScoreDataJson = stockScoreData.json()

    print(stockScoreDataJson)

    #template = loader.get_template("stockdetails/stockinfo.html")
    #print(response.json())
    context = {"stockinfo":stockData,
               'profit_after_tax': profitAfterTax,
               'corpactions': corpActionDataJson,
               'peers': peersDataJson,
               'topstocks':scoreDataJson,
               'scoredata':stockScoreDataJson
               }
    #print(context)
    #return HttpResponse(template.render(context,request))
    return render(request, "stockdetails/stockinfo.html", context)

# Create your views here.
