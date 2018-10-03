name = input('Please Enter your name : ')
age = input('Please enter your age: ')


def name_and_age_():
    print(name + " " + age)


def any_argument(arg1, arg2):
    print(arg1 + " " + arg2)


def age_in_decades(age):
    to_be_eval_age = int(age) / 10
    return int(to_be_eval_age)


name_and_age_()
print(age_in_decades(age))