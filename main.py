import pandas
from turtle import Turtle, Screen
from state_name import StateName


turtle = Turtle()
screen = Screen()
screen.title("U.S States Guess")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_name = StateName()


# x = input("What is your name?: ").title()
# print(x)



data = pandas.read_csv("50_states.csv")

guess_on = True
correct_answer = 0
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State {correct_answer}/50", prompt="What's another state's name?").title()
    state_row = data[data["state"] == answer_state]
    if answer_state == "Exit":
        break
    elif not state_row.empty:
        guess_states.append(answer_state)
        xcor = int(state_row.x)
        ycor = int(state_row.y)
        state_position = [xcor, ycor]
        state_name.draw_name(state_position, answer_state)
        correct_answer += 1



state_list = data["state"].to_list()
new_list = []
new_list = [state for state in state_list if state not in guess_states]

# for state in guess_states:
#     if state in state_list:
#         state_list.remove(state)

state_not_guessed = pandas.DataFrame(new_list)
state_not_guessed.to_csv("remaining_states.csv")





# states_info = data.to_dict()








# for state in data["state"]:
#     if state == answer_state:
#         state_row = states_info["state"][0]
#         print(state_row)



#
# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#
#
#
#
#
#
# # #to get the coordinate on mouse click in the canvas
# # def get_mouse_click_coor(x, y):
# #     print(x, y)
# # screen.onscreenclick(get_mouse_click_coor)
#
#
