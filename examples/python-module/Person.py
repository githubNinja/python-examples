class Person:
    def __init__(self, name, addrZipCode):
        print('main !!')
        self.name = name
        self.addrZipCode = addrZipCode

    def getAddress(self):
        if self.addrZipCode == '61265':
            print(f"{self.addrZipCode} is Moline IL")
        elif self.addrZipCode == '23233':
            print(f"{self.addrZipCode} is Richmond VA")
        else:
            print(f"City is not located with zip code::{self.addrZipCode}")


person = Person('Tom', "61265")
print("python-module.addrZipCode is::", person.addrZipCode)
person.getAddress()