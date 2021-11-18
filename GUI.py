import PySimpleGUI as sg
import matplotlib.pyplot as plt

# sg.theme_previewer()
# HotDogStand = meme
# DarkGreen5 is good
# can use "sg.theme_previewer()"" to look at all the themes available
sg.theme("HotDogStand")

# TODO look at the "Animated Matplotlib" in the cookbook and attempt to implement the live graph reading

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
    [
        sg.Slider(
            (0, 100),
            key="-slider-",
            default_value=50,
            orientation="horizontal",
            expand_x=True,
            enable_events=True,
            disable_number_display=True,
        ),
        sg.T("", size=(4, 1)),
    ],
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
window = sg.Window("Flume Control", layout)
print("test1")
while True:  # Event Loop
    event, values = window.read()
    print("test2")
    data.append(values["-slider-"])
    plt.plot(data, color)
    plt.show()
    if event == sg.WIN_CLOSED or event == "Close":
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
        data.append(values["-slider-"])
        print("You entered", values["-slider-"])
        print("data = ", data)
        print("values= ", values)
        plt.plot(data, color)
        plt.show(block=False)
window.close()
