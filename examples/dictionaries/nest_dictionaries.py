fav_lang = {
    'sarah': ['C++', 'Go'],
    'Jim': ['Java'],
    'Peter': ['Scala', 'Java', 'R'],
}

for name, languages in fav_lang.items():
    for langs in languages:
        if len(langs) > 1:
            print("{} favourite languages  are:{} and length is::{}".format(name, langs, len(languages)))
        else:
            print("{} favourite lang is:{}".format(name, languages))