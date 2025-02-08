# Here's some code before using ruff. I made it messy on purpose.

# import os, sys, math, random


# def main():
#     print("Hello from hello-world!")


# if __name__ == "__main__":
#     main()

# new_useless_dict = { 1 :"meow meow meow" ,
#   2  :   "this is a dictionary",
#         3   :  "blah blah blah"
# , 4  :   "buba"
# ,   5:    "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
#         ,6:"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#                 }


# def  extra_spaces(    ):
#   print  (    "I added extra spaces here."   )

#    x   =    42

# def    bad_function  (  x   )  :
#   y=x +   20
#      print ( "Result is: ",y  )


# def bad_one_liner (    ):return[ x  ^  33 for x in range (   10 )if x%2==0]


# Here's the code after using ruff check and ruff format
def main():
    print("Hello from hello-world!")


if __name__ == "__main__":
    main()

new_useless_dict = {
    1: "meow meow meow",
    2: "this is a dictionary",
    3: "blah blah blah",
    4: "buba",
    5: "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",
    6: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
}


def extra_spaces():
    print("I added extra spaces here.")


x = 42


def bad_function(x):
    y = x + 20
    print("Result is: ", y)


def bad_one_liner():
    return [x ^ 33 for x in range(10) if x % 2 == 0]
