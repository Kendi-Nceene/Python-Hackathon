from datetime import datetime
date = datetime.now()
x = date.weekday()
t = date.today()
m = t.strftime("%Y-%m-%d")
if x >= 0 and x <= 4:
  print("Date:", m)
  print("Day:", date.strftime('%a'))
  print("Fare: 100")
elif x == 5:
  print ("Date:", m)
  print("Day:", date.strftime('%a'))
  print("Fare: 60") 
elif x == 6:
  print( "Date:", m)
  print("Day", date.strftime('%a'))
  print("Fare: 80")
