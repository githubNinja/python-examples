# A list is mutable.


course = ['data science', 'machine learning', 'html', ['java', 'c++', 'Go']]
#Slice
print("Slice ::{}".format(course[:3]))

#All elements:
print("All Elements ::{}".format(course))

complete_list = course[:4]
print("Slice::{}".format(complete_list))

complete_list[2] = 'React'
print("complete_list now::{}".format(complete_list))

print("2nd index element::{}".format(complete_list[2]))
course.remove("html")

print("All Elements after removal::{}".format(course))

universities = ['UT', 'UIC', 'Western Illinois']

concatenate_lists = course + universities
print("list concatenation::{}".format(concatenate_lists))

# Removing elements from list
print("List after removed element::{}".format(concatenate_lists))


# Pop element
concatenate_lists.pop()
print("List after pop::{}".format(concatenate_lists))