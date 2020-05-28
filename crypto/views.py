from django.shortcuts import render
import json
import requests
# Create your views here.
def home(request):
    crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,ETC,EOS,BSV,LTC,OKB,BNB&tsyms=INR")
    crypto = json.loads(crypto_request.content)
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'crypto/home.html', {'crypto':crypto,'api':api})

def search(request):
    if request.method == "POST":
        cryptoval = request.POST["cryptovalue"]
        cryptoval = cryptoval.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + cryptoval + "&tsyms=INR")
        crypto = json.loads(crypto_request.content)
        return render(request, 'crypto/search.html', {"crypto":crypto})
    else:
        notfound = "Please enter the correct cryptocoin"
        return render(request, 'crypto/search.html', {"notfound": notfound})        