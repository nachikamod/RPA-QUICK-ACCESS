import os

loop = True

while loop: 
    print('Welcome Nachi !!\n')
    print('Select domain to open :')
    print('1. Web Dev')
    print('2. Android')
    print('3. Python')
    print('0. Exit')
    sel = int(input('Select any option : '))
    if sel == 0:
        loop = False
    elif sel == 1:
        print('Web dir not created')
    elif sel == 2:
        and_loop = True
        while and_loop:
            print('Select project : ')
            print('1. mahayoga_siddhayoga_app'),
            print('2. My_Physician_App')
            print('0. Quit')
            and_sel = int(input('Select project : '))
            if and_sel == 0:
                and_loop = False
            elif and_sel == 1:
                print('\nopening project...\n')
                os.system('cmd /c "code D:/workspace/android/mahayoga_siddhayoga_app/"')
            elif and_sel == 2:
                print('\nopening project...\n')
                os.system('cmd /c "code D:/workspace/android/My_Physician_Ap/"')

    elif sel == 3:
        print('Python dir not crated')
