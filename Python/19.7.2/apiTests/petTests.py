import pytest

from app.api import PetFriends
from app.settings import valid_email, valid_password


pf=PetFriends()


def test_get_api_positive(email=valid_email,pwd=valid_password):
        status, result = pf.get_api_key(email,pwd)
        assert status == 200
        assert 'key' in result

def test_get_api_negative_user(email='unvalid_email',pwd=valid_password):
        status, result = pf.get_api_key(email,pwd)
        assert status == 403

def test_get_api_negative_pass(email=valid_email,pwd='unvalid_email'):
        status, result = pf.get_api_key(email,pwd)
        assert status == 403


def test_get_all_list_positive(filter=''):
        _, akey =pf.get_api_key(valid_email,valid_password)
        status, result = pf.get_list_pets(akey,filter)
        assert status == 200
        assert len(result['pets']) > 0

def test_get_personal_list_positive(filter='my_pets'):
        _, akey =pf.get_api_key(valid_email,valid_password)
        status, result = pf.get_list_pets(akey,filter)
        assert status == 200
        assert len(result['pets']) > 0

def test_get_wotkey_list_negative(filter=''):
        _, akey =pf.get_api_key(valid_email,valid_password)
        akey['key']='error'
        status, result = pf.get_list_pets(akey,filter)
        assert status == 403

def test_get_filter_list_negative(filter='aboba'):
        _, akey =pf.get_api_key(valid_email,valid_password)
        status, result = pf.get_list_pets(akey,filter)
        assert status == 500

def test_create_pet_simple_positive():
        _, akey =pf.get_api_key(valid_email,valid_password)
        testname='Фуфайкин'
        status, result = pf.create_pet_simple(akey,testname,'Интернет-зверь',9)
        assert status == 200
        assert result['name']==testname

def test_set_photo_positive():
        _, akey = pf.get_api_key(valid_email, valid_password)
        testname = 'Фуфайкин'
        _, petId = pf.create_pet_simple(akey, testname, 'Интернет-зверь', 9)
        photo='../images/business_pica.jpeg'
        status,result = pf.set_photo(akey,petId,photo)
        assert status == 200

def test_update_info_positive():
        _, akey =pf.get_api_key(valid_email,valid_password)
        testname='Фуфайкин'
        _, petId = pf.create_pet_simple(akey,testname,'Интернет-зверь',9)
        testname = 'Мармышкин'
        status, result = pf.update_info(akey,petId,testname,'Интернет-зверь',12)
        assert status == 200
        assert result['name']==testname

def test_delete_pet_positive():
        _, akey = pf.get_api_key(valid_email, valid_password)
        testname = 'Фуфайкин'
        _, petId = pf.create_pet_simple(akey, testname, 'Интернет-зверь', 9)
        status, result = pf.delete_pet(akey, petId,)
        assert status == 200