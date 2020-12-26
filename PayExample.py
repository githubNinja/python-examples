hours = input("Enter hours")
rate = input("Enter rate")
floatHrs = float(hours)
floatRate = float(rate)
floatPay = floatHrs * floatRate
print("float pay when hrs < 40::" + str(floatPay))
pay = 1
if floatHrs > 40:
    print("hrs are > 40 so pay rate is different")
pay = pay * 1.5 * floatRate
print("pay when hrs > 40 is::" + str(pay))

# % operator nice !!!
print("%s %s" % (pay, floatRate))
print("{}{}".format("Total Pay is", pay))
