#weather = 65

weather = input("Enter weather::")
weather = int(weather)

if weather >=55 and weather <= 65:
    print("Weather is better than Spring")
elif weather > 65:
    print("Weather is like Summer")
else:
    print("Weather is like Winter")