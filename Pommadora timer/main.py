from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✔"
a = 10

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=421, height=360)
window.config(padx=100, pady=50, bg="white")

label1 = Label(text = "       ", bg="white")
label1.grid(row=0, column=0)

canvas = Canvas(width=421, height=360, bg="white", highlightthickness=0)
Image = PhotoImage(file="Tomato.png")
canvas.create_image(210.5, 180, image = Image)
b = canvas.create_text(210.5, 190, text= a, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row = 1,column = 1)

label2 = Label(text="Timer", fg="green", bg="white", font=(FONT_NAME, 60, "bold"))
label2.grid(row=0, column=1)

label3 = Label(text="       ", bg="white")
label3.grid(row=4, column=0)

start_button = Button(text = "Start", fg="red", bg="pink", font=(FONT_NAME, 25, "bold"), highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", fg="red", bg="pink", font=(FONT_NAME, 25, "bold"), highlightthickness=0)    
reset_button.grid(row = 2, column=2)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
c = 0
from time import *
while a == 10 and c < 5:
    canvas.itemconfig(b, text=a)
    label2.config(text="Timer", fg="green")
    while a >= 0:
        window.update()
        sleep(1)
        canvas.itemconfig(b, text=a)
        a -= 1
    a = 5
    checkmarks = Label(text = checkmark, fg="green", bg="white", font=(FONT_NAME, 25, "bold"))
    checkmarks.grid(row=3, column=1)
    checkmarks.config(text=checkmark)
    checkmark = checkmark + "✔"
    label2.config(text="Break", fg="red")
    while a >= 0 and c < 4:
        window.update()
        sleep(1)
        canvas.itemconfig(b, text=a)
        a -= 1
    a = 10
    if c == 4:
        a = 20
        while a >= 0:
            window.update()
            sleep(1)
            canvas.itemconfig(b, text=a)
            a -= 1
        canvas.itemconfig(b, text="TIME'S UP!")
    c += 1
window.mainloop()




