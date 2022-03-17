import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests


class PetFriends:

    def __init__(self):
        self.base_url='https://petfriends1.herokuapp.com/'

    def get_api_key(self, email, pwd):
       header = {
           'email': email,
           'password': pwd,
       }
       res = requests.get(self.base_url+'api/key', headers=header)
       status = res.status_code
       try:
           result = res.json()
       except json.decoder.JSONDecodeError:
           result = res.text
       return status, result

    def get_list_pets(self,akey,filter):
        header={'auth_key': akey['key']}
        filter={'filter': filter}
        res=requests.get(self.base_url+'api/pets',headers=header,params=filter)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def create_pet_simple(self,akey,name,anm_type,age):
        header = {'auth_key': akey['key']}
        data ={'name': name,
               'animal_type':anm_type,
               'age':age,
               }
        res=requests.post(self.base_url+'api/create_pet_simple',data=data,headers=header)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_info(self,akey,petId,name,anm_type,age):
        header = {'auth_key': akey['key']}
        data = {'name': name,
                'animal_type': anm_type,
                'age': age,
                }
        res = requests.put(self.base_url + 'api/pets/'+petId['id'], data=data, headers=header)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_pet(self,akey,petId):
        header = {'auth_key': akey['key']}
        res = requests.delete(self.base_url + 'api/pets/'+petId['id'], headers=header)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
