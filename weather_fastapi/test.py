from datetime import datetime

date = datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S")
print(date)
print(type(date))