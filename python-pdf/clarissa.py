import requests

url = 'https://dashboard.ekodevices.com/users/sign_in'

payload =  {  "$set_once": {"$email": "clarissa.lima@academico.ufpb.br","$first Name": "Clarissa","$last Name": "Lima","$name": "Clarissa Lima","$signed up at": "2022-12-20T21:00:12.000Z","Live Stream Link": "https://app.ekodevices.com/livestream/230ed932e89bcd184a887698","$plan": "Starter","Institution Id": "","Institution Name": ""},"$token": "505d769187fd7cb5be39d0b4dd21da34","$distinct_id": "245455","$device_id": "18578ebcc6d102f-0a951073806f26-26021151-1fa400-18578ebcc6ef33","$user_id": "245455"
            }

with requests.Session() as s:
    p = s.post(url, data = payload) 

   # s.get('pdf').content

    print(p)