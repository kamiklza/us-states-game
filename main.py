import pandas
from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()
screen.title("U.S States Gage")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
data = pandas.read_csv("50_states.csv")
state_row = data[data["state"] == "California"]
state_x = state_row.x
print(state_x)
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
# screen.mainloop()