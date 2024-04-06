# When more than one operator appears in an expression, the order of evaluation
# depends on the rules of precedence. For mathematical operators, Python follows
# mathematical convention. The acronym PEMDAS is a useful way to remember
# the rules:
# PEMDAS -> Parenthesis, exponentation ( multiplication), M -> Multiplication D -> Division and A -> Addition , S -> Subtraction
# Multiplication and Division have same precendence.


# Data types are int, str, float

this_is_an_int = 12
this_is_an_float = 123.45
this_is_an_string = "Hello"
print("{}{}{}{}{}{}".format(" 12 is", type(this_is_an_int), "\n 123.45 is::", type(this_is_an_float), "\n Hello is::",
                            type(this_is_an_string)))

# Empty dictionary declaration
empty_dict = dict()
