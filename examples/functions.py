def invokehellofunction():
    x = input("enter x")
    if int(x) > 100:
        print("this is a hello function !!")
    else:
        str = "hello"
        print(str + " x is not greater than 100")
    return "hello is returned !!"


functionReturValue = invokehellofunction()
print("{} {}".format("return value from function::", functionReturValue))

print("does this print ever :::")