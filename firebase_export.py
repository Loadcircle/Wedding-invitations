import pandas as pd
import urllib.parse
import json


pdfile = pd.read_csv('export.csv')
data = pdfile.iterrows()

toexport = [
]

def value_or_none(value):
    if str(value) == 'nan':
        return None
    return value

for index, row in data:
    family_name = row['family_name']
    if family_name and str(family_name) != 'nan':     
        family_exist = any(x['family_name'] == family_name for x in toexport)

        if not family_exist:
            data = {
                'family_name' : family_name,
                'invitation_message' : False,
                'invites' : [
                ],
                'table' : None
            }

            toexport.append(data)

        for index, item in enumerate(toexport):
            if item['family_name'] == family_name:

                invite_name = value_or_none(row['invite_name'])
                email = value_or_none(row['email'])
                phone_number = value_or_none(row['phone_number'])
                sex = value_or_none(row['sex'])
                group = value_or_none(row['group'])

                invite_data = {
                            "isgoing": False,
                            "name": invite_name,
                            "email": email,
                            "phone_number": phone_number,
                            "sex": sex,
                            "group": group,
                        }
                item['invites'].append(invite_data)

with open('families.json', 'w') as outfile:
    json.dump(toexport, outfile)
    print('exported file')

