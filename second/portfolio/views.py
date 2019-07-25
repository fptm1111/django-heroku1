from django.shortcuts import render
from .models import Portfolio


def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})

def second(request): #new.html띄어주는 함수
    return render(request, 'second.html')