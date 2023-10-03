"""Functions module.

Stores the functions used in the quiz.
"""

import csv
import random
import constant


def introduce_the_game():
    intro = """
    Welcome to playing this quiz. There are three (3), 
    levels with three (3) questions each. To advance to the next level, 
    you need to get all questions of that level right. You can type 'close', to quit the game.
    Good luck!
    TIP: All of the answers are natural numbers typed numerically, like 4 or 5 or 17.
    
    """
    return intro


def get_problems(filepath:str)->dict:
    """Takes questionset csv filepath as input
    and returns it as a dictionary."""

    problem_set = {}

    with open(filepath, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        for row in csv_reader:
            p, a = row
            problem_set[p] = a
    
    return problem_set


def shuffle_questions(question_dict:dict)->list:
    """Takes the question dictionary as input and
    returns a shuffled list of the questions."""
    randomized_keys = [key for key in question_dict.keys()]
    random.shuffle(randomized_keys)
    return randomized_keys


def set_level(result:bool)->int:
    """Increases or decreases level, based on
    whether player wins current level or not"""
    # If player wins the level we increase it by 1
    if result:
        return 1
    # If player failed the level we decrease it by 1
    return -1


def print_level(level:int)->str:
    """ Gets level number as input.
    Prints current level.
    """
    match level:
        case constant.EASY_LEVEL:
            print("===Easy level===")
        case constant.CHALLENGING_LEVEL:
            print("===Challenging level==")
        case constant.HARD_LEVEL:
            print("===Final level===")

def get_level_string(level:int)->str:
    """ Gets level number as input.
    Prints current level.
    """
    match level:
        case constant.EASY_LEVEL:
            return "===Easy level==="
        case constant.CHALLENGING_LEVEL:
            return "===Challenging level=="
        case constant.HARD_LEVEL:
            return "===Final level==="
        
def get_question_answer_pair(
        level:int=constant.EASY_LEVEL, 
        questions:list=constant.QUESTION_SETS)->tuple:
    """ Takes current level and the list of problem-sets and inupt.
    Returns a tuple with current answe and question.
    """
    while True:
        level_questions:dict = get_problems(questions[level])
        shuffled_questions:list = shuffle_questions(level_questions)
        for i in range(constant.QUESTIONS_PER_LEVEL):
            current_question = shuffled_questions[i]
            correct_answer = level_questions[current_question]
            formatted_question = format_question(current_question)
            yield formatted_question, correct_answer

def check_answer(user_answer:str, correct_answer:str)->bool:
    """ Takes the user_answer and correct answer and checks if they are the same
    If answer is correct returns True
    else False
    """
    if user_answer == correct_answer:
        return True
    return False

def format_question(question:str)->str:
    """ Takes the current question as input
    returns the question separated in different rows,
    10 words per row.
    """
    listed = question.split(" ")

    for i, w in enumerate(listed):
        if i % 11 == 10:
            listed.insert(i, "\n")
    formatted = " ".join(listed)
    return formatted

# def track_level_progress(answer:bool):
#     while True:
#         default = False
#         check_list = []
#         for i in range(constant.QUESTIONS_PER_LEVEL):
#             print(i, "level")
#             check_list.append(answer)
#             if len(check_list) < constant.QUESTIONS_PER_LEVEL:
#                 yield default
#         if (all(check_list)):
#             default = True
#         yield default

# def track_game_progress(level_progress:bool, level:int)->int:
#     """ Takes in level progress and current level.
#     Increases or decreases level based level progress.
#     """
#     while True:
#         current_level = level
#         rounds = constant.QUESTIONS_PER_LEVEL
#         for i in range(rounds):
#             print(level_progress, "from game", i, "iter" )
#             if i == 2:
#                 if level_progress == True:
#                     current_level += 1
#                     yield current_level
#                 else:
#                     current_level -= 1
#                     if current_level < 0:
#                         current_level = 0
#                     yield current_level
#             else:
#                 yield current_level

