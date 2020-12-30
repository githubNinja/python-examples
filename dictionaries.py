# dictionary is a collection of key value pairs.
keyValuePair = {'color': 'green', 'place': 'Chicago'}
print('{}{}'.format('color is::', keyValuePair['color']))
# Changing the value of dictionary key
keyValuePair['place'] = 'Orlando'
print('{}{}'.format('modified place  is::', keyValuePair['place']))

# Remove a keyValue pair
del keyValuePair['place']
print('{}{}'.format('modified place  is::', keyValuePair))

# get a value if not exist then substitue with a default value
get = keyValuePair.get('place', 'Chicago')
print('{}{}'.format('new key value pair is::', get))

# set a value
keyValuePair.setdefault('place', 'Orlando')
print('{}{}'.format('setting a new key value pair is::', keyValuePair))