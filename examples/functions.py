def invokehellofunction():
    x = input("enter x")
    if int(x) > 100:
        print("this is a hello function !!")
    else:
        print("x is not greater than 100")
    return "hello is returned !!"


functionReturValue = invokehellofunction()
print("{} {}".format("return value from function::", functionReturValue))
