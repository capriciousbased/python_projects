import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Enter name')],
    [sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')] 
]

window = sg.Window('Form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    print('You entered ', values[0])

window.close()