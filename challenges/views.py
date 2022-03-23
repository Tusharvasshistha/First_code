from logging import exception
import re
from urllib import response
from django.shortcuts import render
from django.http import  HttpRequest, HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
Monthly_challengess = {
    "jan" : "hello jan",
    "feb" : "hello feb",
    "march" : "hello march",
    "april" : "hello april",
    "may" : "hello may",
    "june" : "hello june",
    "july" : "hello july",
    "aug" : "hello aug",
    "sept" : "hello sept",
    "oct" : "hello oct",
    "nov" : "hello nov",
    "dec" : "hello dec"
}

def index(request):
    ##list_items=""
    Monthsss = list(Monthly_challengess.keys())
    ##for month in Monthsss:
        ##cap_mon = month.capitalize()
        ##mon_path = reverse("challenges-tushar",args=[month])
        ##list_items += f"<li><a href=\"{mon_path}\">{cap_mon}</a></li>"
    ##response_data = f"<ul>{list_items}</ul>"
    ##return HttpResponse(response_data)
    return render(request,"challenges/index.html",{
        "months" : Monthsss
    })

def Monthly_challenges__number(request, months):
    Monthss = list(Monthly_challengess.keys())
    if months > len(Monthss):
        return HttpResponseNotFound ("invalid month")
    forward_month = Monthss[months - 1]
    redirect_path = reverse("challenges-tushar", args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def Monthly_challenges(request,months):
    try:
        challenges_text = Monthly_challengess[months]
        return render(request,"challenges/challenge.html",{
            "text" : challenges_text,
            "month_name": months.capitalize()
        })
    except:
        return HttpResponseNotFound("Not a month")