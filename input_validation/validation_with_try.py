"""
author: Alex Kelso
program: validation_with_try
date: 9/22/2020

program purpose: learn how to use input try
"""
NUMBER_TESTS = 3


def average(score1, score2, score3):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    return float((score1 + score2 + score3) / NUMBER_TESTS)


if __name__ == '__main__':
    first_name = input('What\'s your first name?: ')
    last_name = input('What\'s your last name?: ')
    age = input('How old are you?: ')

    score_one = input("Enter 1st Score: ")
    score_two = input("Enter 2nd Score: ")
    score_three = input("Enter 3rd Score: ")
    try:
        average_scores = average(int(score_one), int(score_two), int(score_three))
    except ValueError:
        print("Please Enter Accepted Values.")
    else:
        print('{} {}, Age: {}, Average Grade: {}'.format(first_name, last_name, age, average_scores))
