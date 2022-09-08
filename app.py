import pandas as pd
import urllib.parse

pdfile = pd.read_csv('invitados.csv')
data = pdfile.iterrows()

toexport = {
    'fullname' : [],
    'phone' : [],
    'message' : [],
    'link' : [],
}

for index, row in data:

    name = row['NOMBRE']
    lastname = row['APELLIDO']        
    email = row['EMAIL']

    fullname = str(name) + ' ' + str(lastname)
    phone = str(row['TELEFONO']).replace(' ', '')
    if phone and phone != 'nan' and phone[0] != '5':
        phone = '51'+phone


    wsmessage = 'Hola %s, estamos a puertas de vivir uno de los días más importantes de nuestras vidas, por ello queremos pedirte que nos guardes esta fecha.'%(fullname)
    encodemessage = urllib.parse.quote_plus(wsmessage)

    wslink = 'https://api.whatsapp.com/send?phone=%s&text=%s'%(phone, encodemessage)

    if phone and phone != 'nan':
        toexport['fullname'].append(fullname)
        toexport['phone'].append(phone)
        toexport['message'].append(wsmessage)
        toexport['link'].append(wslink)


df = pd.DataFrame(toexport)

df.to_excel('invitados2.xlsx', index=False, header = True)