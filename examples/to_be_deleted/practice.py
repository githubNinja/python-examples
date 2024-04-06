# conditional
# name = input("Enter name::")
name = "Peter"
if name == "Peter":
    print("name matched !! and It's:", name)
elif name != "Peter":
    print("name is something else")

# dictionaries

movies = {'comedy': 'abc_comedy_movie', 'action': 'IronMan3', 'family': 'HomeAlone3'}
movieName = movies['comedy'].title()
print('Action movie is:{}', format(movieName))


def print_dictionary(dict_coll):
    for key, value in dict_coll.items():
        print('dictionary key :{} and dictionary type:{}'.format(key.title(), value.title()))


# printMovies()


# Modify dictionary
d = dict()
dictionary = {'a': '1', 'b': '2', 'c': '3'}
print_dictionary(dictionary)
# Updating dictionary
dictionary.update({'c': 'value is 3'})
print_dictionary(dictionary)
