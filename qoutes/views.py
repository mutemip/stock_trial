from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StockForm
from .models import *


# Create your views here.
def home_view(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_9a73a6b8592d440791fadf66e892238f")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request, 'qoutes/home.html', {'api': api})
    else:
        return render(request, 'qoutes/home.html', {'ticker': "Enter ticker above ..."})


def about_view(request):
    return render(request, "qoutes/about.html", {})


def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock Added Successfully")
            return redirect('add_stock')
    else:
        stocks = Stock.objects.all()
        output = []
        for stocks_item in stocks:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(stocks_item) + "/quote?token=pk_9a73a6b8592d440791fadf66e892238f")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error"
        return render(request, 'qoutes/add_stock.html', {'stocks': stocks, 'output': output})


def delete(request, stocks_id):
    item = Stock.objects.get(pk=stocks_id)
    item.delete()
    messages.success(request, "Stock Has Been Deleted!")
    return redirect(delete_stock)

def delete_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'qoutes/delete_stock.html', {'stocks': stocks})

