import PySimpleGUI as sg

import constant
import modules.functions as foos

def intro():
    sg.theme("Black")
    label = sg.Text(foos.introduce_the_game())
    next_button = sg.Button("Start")
    intro_layout = [[label, next_button]]


    window = sg.Window("Superduper quiz!",
                       layout=intro_layout,
                       font=("Lato", 20))
    
    while True:
        event, values = window.read(timeout=200)
        print(1, event)
        print(2, values)
        
        match event:
            case "Start":
                break
            case sg.WIN_CLOSED:
                exit()

    window.close()


def game_view():
    level_progress = []
    sg.theme("Black")
    current_level = constant.EASY_LEVEL
    question_answer = foos.get_question_answer_pair(current_level)
    current_question, correct_answer = next(question_answer)

    label = sg.Text("Quiz game!")
    score_count = sg.Text(f"Score: {level_progress.count(True)}/{constant.QUESTIONS_PER_LEVEL}", key="score")
    round_label = sg.Text(f"Round {len(level_progress) + 1}", key="round")
    level_label = sg.Text(foos.get_level_string(current_level), key="level")
    question_label = sg.Text(current_question, key="question")
    answer_box = sg.InputText(tooltip="Your answer", key="user_answer")
    answer_button = sg.Button("Answer")
    stop_button = sg.Button("Stop playing")
    game_layout = [[label],
                   [round_label],
                   [level_label],
                   [score_count],
                   [question_label],
                   [answer_box, answer_button],
                   [stop_button]]

    window = sg.Window("Superduper quiz!",
                       layout=game_layout,
                       font=("Lato", 20))

    while True:
        event, values = window.read(timeout=200)
        print(1, event)
        print(2, values)
        if values["user_answer"] == "close":
            window.close()
            break

        match event:
            case "Stop playing":
                break
            case sg.WIN_CLOSED:
                break
            case "Answer":
                answer:bool = foos.check_answer(values["user_answer"], correct_answer)
                level_progress.append(answer)
                print(level_progress)
                print(answer, "answer")

                if (len(level_progress) == constant.QUESTIONS_PER_LEVEL and
                    all(level_progress)):
                    current_level += 1
                    question_answer = foos.get_question_answer_pair(current_level)
                    level_progress = []
                    
                elif (len(level_progress)) == constant.QUESTIONS_PER_LEVEL:
                    level_progress = []
                    current_level -= 0
                    if current_level < 1:
                        current_level = 0
                    question_answer = foos.get_question_answer_pair(current_level)

                if current_level > constant.HARD_LEVEL:
                    window.close()
                    you_win()
                    break

                current_question, correct_answer = next(question_answer)
                window["question"].update(value=current_question)
                window["level"].update(value=foos.get_level_string(current_level))
                window["round"].update(value=f"Round {len(level_progress) + 1}")
                window["score"].update(value=f"Score: {level_progress.count(True)}/{constant.QUESTIONS_PER_LEVEL}")
                window["user_answer"].update(value="")
        
    window.close()

def you_win():
    sg.theme("Black")

    label = sg.Text("YOU WON!")
    stop_button = sg.Button("Stop playing")
    again_button = sg.Button("Play again")

    layout = [[label],
              [again_button, stop_button]]
    
    window = sg.Window("Superduper quiz!",
                       layout=layout,
                       font=("Lato", 20))
    while True:
        event, values = window.read(timeout=200)
        print(1, event)
        print(2, values)

        match event:
            case "Stop playing":
                break
            case "Play again":
                window.close()
                game_view()
                break

    window.close()

if __name__ == "__main__":
    intro()
    game_view()