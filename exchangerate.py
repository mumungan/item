from forex_python.converter import CurrencyRates
from datetime import datetime
    
now = datetime.now()
c = CurrencyRates()

jpykrw = c.convert('JPY', 'KRW', 100, now)
usdkrw = c.convert('USD', 'KRW', 1, now)
usdjpy = c.convert('USD', 'JPY', 1, now)

print(int(jpykrw))
print(int(usdkrw))
print(int(usdjpy))