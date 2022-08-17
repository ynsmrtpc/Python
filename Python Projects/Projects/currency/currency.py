import requests

url = "http://data.fixer.io/api/latest?access_key=c97453d821e3dbe08b38cac7c7b403f4&format=1"
response = requests.get(url)

dataJson = response.json()
currency_try = dataJson["rates"]["TRY"]
currency_usd = dataJson["rates"]["USD"]
usdTotry = currency_try / currency_usd

print("Şu anki kura göre 1 USD = {}₺".format(round(usdTotry,2)))
print("Şu anki kura göre 1 EURO = {}₺".format(round(currency_try,2)))

miktar = int(input("Miktarı giriniz: "))
# selectCurrency = input("Dönüştürmek istediğiniz para birimini giriniz(EURO/USD):")


print("{} USD = {} TRY".format(miktar, round(miktar * usdTotry , 2)))
print("{} EURO = {} TRY".format(miktar, round(miktar * currency_try, 2)))


