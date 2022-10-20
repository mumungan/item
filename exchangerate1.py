from currency_converter import CurrencyConverter
c = CurrencyConverter()
jpykrw = int(c.convert(100,'JPY','KRW'))
usdkrw = int(c.convert(1,'USD','KRW'))
usdjpy = int(c.convert(1,'USD','JPY'))
print(jpykrw)
print(usdkrw)
print(usdjpy)
