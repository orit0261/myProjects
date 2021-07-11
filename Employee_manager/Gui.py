# hello_psg.py

import PySimpleGUI as sg

def open_window(msg):
    layout = [[sg.Text(msg, key="new")],[sg.Button("CLOSE")]]
    window = sg.Window("Message Window", layout, modal=True, background_color='black')
    choice = None
    while True:
        event, values = window.read()
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break
    window.close()

def main():
    t_color = 'black'
    b_color = 'silver'
    layout = [[sg.Text("Choose One Option:",text_color=t_color, background_color=b_color)],
              [sg.Text("1. Add new Employee manually",text_color=t_color, background_color=b_color)],
              [sg.Text("2. Add new Employee from file",text_color=t_color, background_color=b_color)],
              [sg.Text("3. Delete Employee manually",text_color=t_color, background_color=b_color)],
              [sg.Text("4. Delete Employee from file",text_color=t_color, background_color=b_color)],
              [sg.Text("5. Mark Attendance",text_color=t_color, background_color=b_color)],
              [sg.Text("6. Generate Attendance Report of an Employee",text_color=t_color, background_color=b_color)],
              [sg.Text("7. Print report for current month for all employees",text_color=t_color, background_color=b_color)],
              [sg.Text("8. Print report for all employees who where late",text_color=t_color, background_color=b_color)],
              [sg.Text('Enter Your choise:',text_color=t_color, background_color=b_color), sg.InputText()],
              [sg.Button("OK"),sg.Button("CLOSE")]]

    # Create the window
    window = sg.Window("Main Menu", layout, resizable=True, background_color='silver')

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break

        if event == "OK" :
           try:
             val = int(values[0])
           except ValueError:
             open_window(f'int value is excepted, You entered {values[0]}')
           else:
               if val>0 and val<9:
                open_window("Processing...")

    window.close()

if __name__ == "__main__":
    main()