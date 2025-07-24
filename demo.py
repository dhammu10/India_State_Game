import turtle
import pandas


screen = turtle.Screen()
image = "Map.gif"
turtle.title("India State Game")
screen.addshape(image)
turtle.shape(image)

# def find_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(find_cor)
guss_state = []

while len(guss_state) < 30:
    guss = screen.textinput(title="guss the Answer", prompt="Enter the State name").upper()

    data = pandas.read_csv("sates_name.csv")
    sate = data["Sates"].to_list()

    if guss in sate:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pensize(3)
        t.fillcolor("yellow")
        go = data[data.Sates == guss]
        t.goto(go.x.item(), go.y.item())
        t.write(guss)
        guss_state.append(guss)



turtle.mainloop()