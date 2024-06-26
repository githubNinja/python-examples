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

# Empty dictionaries
alien = {'colour': 'green', 'x-coords': 12}
print('alien colour:{} and position:{}'.format(alien['colour'], alien['x-coords']))

alien['y-coords'] = '19'
alien['height'] = '5 feet 4 inches'
print('alien dictionary::{}'.format(alien))

# programming languages
fav_lang = {
    'sarah': 'C++',
    'Jim': 'Java',
    'Peter': 'Scala'
}

print('sarah\'s favourite_language is:{}'.format(fav_lang['sarah'].title()))
notFound = fav_lang.get('Kran')
print('lang for Kran::{}'.format(notFound))

# looping thru dictionary using for loop

for key, value in fav_lang.items():
    print('key:{} and value::{}'.format(key.title(), value.title()))
