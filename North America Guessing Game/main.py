import turtle 
import pandas
data = pandas.read_csv("north_america_data.csv")


screen = turtle.Screen()
screen.setup(width = 1000, height = 691)
screen.title = "North America Countries Game"
image = "north_america_img1.gif"
screen.addshape(image)
turtle.shape(image)


# To find the coordinates of the countries
# def get_mouse_click_coor(x, y):
#     print(x, y)


    
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


countries_list = data["Countries"].to_list()

guessed_countries = []
unguessed_countries = []
score = 0
while score  == 0:
    answer_country = screen.textinput(title = "Guess the country", prompt = "What's another country's name?").title()
    if answer_country.title() in countries_list:
        guessed_countries.append(answer_country.title())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data["Countries"] == answer_country]["X"]), int(data[data["Countries"] == answer_country]["Y"]))
        t.write(answer_country.title(), align = "center", font = ("Arial", 8, "normal"))
        score += 1
    elif answer_country.title() == "Exit":
        for country in countries_list:
            if country not in guessed_countries:
                unguessed_countries.append(country)
        break

while 0 < score < 37:
    answer_country = screen.textinput(title = f"{score}/37 countries Correct", prompt = "What's another country's name?").title()
    if answer_country.title() in countries_list:
        guessed_countries.append(answer_country.title())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data["Countries"] == answer_country]["X"]), int(data[data["Countries"] == answer_country]["Y"]))
        t.write(answer_country.title(), align = "center", font = ("Arial", 8, "normal"))
        score += 1
    elif answer_country.title() == "Exit":
        for country in countries_list:
            if country not in guessed_countries:
                unguessed_countries.append(country)     
        break

print(unguessed_countries)

if score == 37:
    screen.clear()
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write("You Win!", align = "center", font = ("Arial", 8, "normal"))
    screen.exitonclick()

