import pandas as pd
import urllib.parse
import json


pdfile = pd.read_csv('export.csv')
data = pdfile.iterrows()

toexport = [
]

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
                'table' : {
                    '__ref__': "tables/ 9a75wsvKRyU0qhIuHRHN"
                }
            }

            toexport.append(data)

        for index, item in enumerate(toexport):
            if item['family_name'] == family_name:

                invite_name = row['invite_name']        
                email = row['email']
                phone_number = row['phone_number']
                sex = row['sex']
                group = row['group']

                invite_data = {
                            "isgoing": False,
                            "name": invite_name,
                            "email": email,
                            "phone_number": phone_number,
                            "sex": sex,
                            "group": group,
                        }
                item['invites'].append(invite_data)


# print(toexport)

print(json.dumps(toexport))
