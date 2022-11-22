import PySimpleGUI as pg

pg.theme("default1")

layout = [
    [
        pg.Text("Enter name:", size=(10, 1)),
        pg.InputText(do_not_clear=False)
    ],
    [
        pg.Text("Enter Age:", size=(10, 1) ),
        pg.InputText(do_not_clear=False)
    ],
    [
        pg.Text("Enter E-mail:", size=(10, 1)),
        pg.InputText(do_not_clear=False)
    ],
    [
        pg.Text("Enter Language:"),
        pg.Checkbox("Python","group 1"),
        pg.Checkbox("Java","group 1"),
    ],
    [
        pg.Button("OK"),
        pg.Button("Close")
    ],
]

window = pg.Window("Form", layout)

while True:
    event, values = window.read()

    if event == pg.WIN_CLOSED or event == "Close": 
        break

    elif event == "OK":
        print(f"Name: {values[0]}")
        print(f"Age: {values[1]}")
        print(f"Email: {values[2]}")

        if values[3]:
           print("User likes Python")
        
        if values[4]:
           print("User likes Java")

        for item in values :
            values[item] = None


window.close()