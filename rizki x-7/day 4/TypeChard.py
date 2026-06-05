import PySimpleGUI as sg

sg.theme('Default')

layout = [
    [sg.Text('Type stuff here gng:'), sg.Text(size=(15,1), key='-OUTPUT-')],
    [sg.Input(key='-IN-')],
    [sg.Button('Show'), sg.Button('Exit')]
]

window = sg.Window('Pattern 2B', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])

window.close()