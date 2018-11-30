import requests


def req(route, data=None, cookies=None):
    if cookies:
        return requests.post('http://127.0.0.1:8000/' + route, data=data, cookies=cookies)
    else:
        return requests.post('http://127.0.0.1:8000/' + route, data=data)


def register(name, type, password):
    response = req('register/', {
        'username': name,
        'password': password,
        'type': type,
    })
    return response.json()


def login(name, password):
    response = req('login/', {
        'username': name,
        'password': password,
    })
    return response.json(), response.cookies


def addrec(name, desc, cookies=None):
    response = req('add/', {
        'username': name,
        'description': desc,
    }, cookies)
    return response.json()


def show_last_desc(name, cookies=None):
    response = req('receive/', {
        'username': name
    }, cookies)
    return response.json()

def show_descs(name, cookies=None):
    response = req('history/', {
        'username': name
    }, cookies)
    return response.json()


print('Hello!!')

while True:
    while True:
        entry = int(input('Enter 1 to register or 2 to log in\n'))

        if entry == 1:
            res = register(
                input('Enter your name: '),
                input('Enter type of user (doctor, patient, pharmacy): '),
                input('Enter your password: ')
            )
            if res['success']:
                print('Your account has been created!')
                break
        elif entry != 2:
            print('Wrong entry')
            continue
        break

    while True:
        name = input('Enter your name: ')
        passw = input('Enter your password: ')
        res = login(
            name, passw
        )
        cookie = res[1]
        res = res[0]
        if res['success']:
            typ = res['type']
            # cookie = res[1]
            print('Welcome', res['username'])
            break
        else:
            print(res['message'])

    while True:
        print('What Do you want to do?')
        if typ == 'doctor':                         #doctor
            print('1. Add a user receipt')
            print('2. Exit')
            entry = int(input('Enter option: '))
            if entry == 1:
                patient_name = input('Enter the patient name: ')
                desc = input('Enter the description of receipt: ')
                res = addrec(patient_name, desc, cookie)
            elif entry == 2:
                print('Goodbye!')
                break
            else:
                print('Wrong entry')

        elif typ == 'pharmacy':                     #pharmacy
            print('1. Receive the receipts')
            print('2. Exit')
            entry = int(input('Enter option: '))
            if entry == 1:
                patient_name = input('Enter the name of patient: ')
                resp = show_last_desc(patient_name, cookie)
                print(resp)

            elif entry == 2:
                print('Goodbye!')
                break
            else:
                print('Wrong entry')

        elif typ == 'patient':                     #patient
            print('1. Receive your history')
            print('2. Exit')
            entry = int(input('Enter option: '))
            if entry == 1:
                resp = show_descs(name, cookie)
                print(resp['history'])
            elif entry == 2:
                print('Goodbye!')
                break
            else:
                print('Wrong entry')
        else:
            print('Wrong entry')
        print()
