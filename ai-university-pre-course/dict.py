dictionary = {
    "Tennis": "Agassi",
    "Cricket": "Sachin",
    "Football": "Pele",
    "Cricket": "Kranthi"
}
print("dictionary:", dictionary.get("Cricket"))
dictionary["Football"] = "Maradona"
print("dictionary keys:", dictionary.values())

for dictElement in dictionary:
    print("dictElement::{}".format(dictElement))
