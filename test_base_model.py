#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print('**********\n\n\n my_model')
print(my_model)
my_model.save()
print('*************\n\n\n my_model after saving')
print(my_model)
my_model_json = my_model.to_dict()
print('**********\n\n\n my_model_json')
print(my_model_json)
print('######################\n kys/values')
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
