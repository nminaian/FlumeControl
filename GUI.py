import PySimpleGUI as sg
import matplotlib.pyplot as plt

sg.theme("DarkAmber")

data = []
color = "b"
# Colors are
# b = blue
# g = green
# r = red
# c = cyan
# m = magenta
# y = yellow
# k = black
# w = white
# TODO make this color variable into a dictionary that is cycled through when the new line same plot event is called

layout = [
    [sg.Text("Some text on row 1")],
    [sg.Slider((0, 100), default_value=50, orientation="horizontal")],
    # [sg.Text("Enter something on row 2"), sg.InputText()],
    [sg.Graph((100, 100), (0, 0), (100, 100), background_color="white")],
    [
        sg.Button("Ok"),
        sg.Button("Clear"),
        sg.Button("New Line Same Plot"),
        sg.Button("Save Data"),
        sg.Button("Close"),
    ],
]

window = sg.Window("Window Title", layout)
while True:
    event, values = window.read()
    data.append(values[0])
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "Clear":
        data = []
        plt.clf()
        plt.show()
    elif event == "New Line Same Plot":
        data = []
    elif event == "Save":
        f = open("myfile.txt", "w")
        f.write(data)
        print(f.read())
    elif event == "Ok":
        print("You entered", values[0])
        print("data = ", data)
        print("values= ", values)
        plt.plot(data, color)
        plt.show(block=False)

window.close()
