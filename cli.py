import modules.functions as foos
import constant



def play_level(level:int=constant.EASY_LEVEL, questions:list=constant.QUESTION_SETS)->bool:
    """ Asks 3 questions, if all are correct
    returns True, 
    else False"""

    level_questions:dict = foos.get_problems(questions[level])
    shuffled_questions:list = foos.shuffle_questions(level_questions)

    level_score = 0

    for i in range(constant.QUESTIONS_PER_LEVEL):
        level_results = []
        answer = False
        current_question = shuffled_questions[i]
        print(current_question)
        user_answer = input(f"Your answer: ")
        print("\n", "︵‿︵‿୨♡----------Answer recorded----------♡୧‿︵‿︵", "\n")
        
        if user_answer == level_questions[current_question]:
            level_score += 1
            answer = True

        if user_answer == "close":
            exit("Thank you for playing!")
        
        level_results.append(answer)
    print(f"Your level score is {level_score} / 3")

    if all(level_results):
        return True
    
    return False


def run_game_loop(starting_level=constant.EASY_LEVEL):
    perfect = 9
    current_level = starting_level
    count = 0
    while current_level <= constant.HARD_LEVEL:
        foos.print_level(current_level)
        level_result = play_level(current_level)
        current_level += foos.set_level(level_result)
        if current_level < 0:
            current_level = 0
        count += 1

    if count == perfect:
        print("Congratulations, you beat the game with a perfect score!")

    print(f"""\n
          Congratulations, you beat the game!
          It took you {count} tries to get all {perfect} questions correct""")


if __name__ == "__main__":
    print(foos.introduce_the_game())
    run_game_loop()

