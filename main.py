import PySimpleGUI as sg
import requests
import datetime

sg.theme('Dark Blue 9')

def crypto(druh,mena):
    response = requests.get('https://api.coinbase.com/v2/exchange-rates?currency='+druh)
    data = response.json()
    return data["data"]["rates"][mena] + ' '+ mena

layout = [
    [sg.Button('x', size=(2,1))],
    [sg.Text('Cas: '), sg.Text('', key='_time_', size=(20, 1))],
    [sg.Text('Cena bitcoinu:'), sg.Text('',key='_cena_')],
    [sg.Text('Cena ethereum:'), sg.Text('',key='_cena2_')],
    [sg.Button('EUR',key='_euro_'), sg.Button('USD',key='_dolar_')]
]

window = sg.Window('okno',layout,size=(400,150),no_titlebar=True,grab_anywhere=True,keep_on_top = True)

def getTime():
    return datetime.datetime.now().strftime('%H:%M:%S')

def main(gui_obj):
    mena = 'USD'
    while True:
        event, values = gui_obj.Read(timeout=250)
        gui_obj['_time_'].Update(getTime())
        gui_obj['_cena_'].Update(crypto('BTC',mena))
        gui_obj['_cena2_'].Update(crypto('ETH',mena))
        if event == '_euro_':
            mena= 'EUR'
        if event == '_dolar_':
            mena = 'USD'
        if event == sg.WIN_CLOSED:
            break
        if event in (sg.WIN_CLOSED, 'x'):
            exit()
if __name__ == '__main__':
    main(window)