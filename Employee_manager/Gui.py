# hello_psg.py

import PySimpleGUI as sg

def open_window(msg, m_layout):
    layout = [[sg.Text(msg, key="new")],m_layout,[sg.Text('This is my sample text',key="error_msg",visible=False,text_color='red',background_color='light grey')],[sg.Button("OK"), sg.Button("CLOSE")]]
    window_son = sg.Window("Message Window", layout, modal=True, background_color='light grey')
    choice = None
    while True:
        event, svalues = window_son.read()
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break
        if event == "OK" :
            emptyval=False
            for val in svalues:
                print(svalues[val])
                if svalues[val]=='':
                    emptyval = True
                    window_son["error_msg"].update(value='missing value!',visible=True)
            if not emptyval:
              break
    window_son.close()

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
                   if val==1: # add emplyee manually
                       m1_layout =[ [sg.Text('id:', key='id_text', text_color=t_color, background_color=b_color), sg.InputText()],
                           [sg.Text('name:', key='name_text', text_color=t_color, background_color=b_color), sg.InputText()],
                           [sg.Text('phone:', key='phone_text', text_color=t_color, background_color=b_color), sg.InputText()],
                           [sg.Text('age:', key='age_text', text_color=t_color, background_color=b_color), sg.InputText()]]

                       open_window("Enter Employee Details:",m1_layout)

    window.close()

if __name__ == "__main__":
    main()