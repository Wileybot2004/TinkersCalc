from tkinter import *
window = Tk()
window.title("Tinker's Construct Smeltery Resource Calcuator")


header = Label(text="Tinkers Construct Smeltery Resouce Calcuator", font="bold")
header.pack()
direction = Label(text="Please fill out all options then click the Calcuate button below to figure out how many resources you need to create a smeltery of that size.")
direction.pack()


#size selector
radio_state = IntVar()
radiobutton1 = Radiobutton(text="3x3 Smeltery", value=3, variable=radio_state)
radiobutton2 = Radiobutton(text="5x5 Smeltery", value=5, variable=radio_state)
radiobutton3 = Radiobutton(text="7x7 Smeltery", value=7, variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


#height selector
spinbox = Spinbox(from_=1, to=5, width=5)
spinbox.pack()
#main logic
def action():
    size = radio_state.get()
    height = spinbox.get()
    int(size)
    heightint = int(height)
    tmp = size * heightint
    tmp2 = tmp * 4
    tmp3 = tmp2 + 6
    tmp4 = tmp3 * 4
    tmp5 = tmp4 + 8 + 6 + 8 + 3 + 7
    output.config(text=f"You need {tmp5} Seared brick(item) and 1 Glass for {tmp3} Seared brick blocks, 1 Smeltery Controller, 1 Seared Tank, 1 Seared Drain, 1 Seared Faucet and 1 Casting Table")


        







button = Button(text="Calculate", command=action)
button.pack()


output = Label(text="")
output.pack()







window.mainloop()