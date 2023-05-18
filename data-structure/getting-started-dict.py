mobile={
    'id':1,
    'company':'samsung',
    'model':'A-25',
    'year':2020,
    'price':26999,
    'camera':'50MP'
}
print("Dict before clear: ",mobile)
mobile.clear()
print("Dict after clear: ",mobile)

player={
    'fname':'Lionel',
    'lname':'Messi',
    'team':'PSG',
    'country':'Argentina'
}
player_copy=player.copy()
print("After copy: ",player_copy)
print("")

menu={
    'food':'momo',
    'price':200,
    'type':'chilly',
    'spicy':'yes',
    'price':250 #this overrides the price so new price is 250 instead of 200
}
print(menu.get('price')) 
print(menu.get('spicy'))
print(menu.get('type'))
print(menu.get('price'))
# print(menu.get('rate')) return error as no such key exists in the dictionary

lang={
    'name':'python',
    'difficulty':'hard',
    'library':'yes',
    'price':0,
}
print(lang.get('price'))
print(lang.get('name'))
print("")

script_lang={
    'js':{
        'id':1,
        'name':'JavaScript',
        'community':'large'
    },
    'framework':{
        'id':1,
        'name':'reactJS',
        'community':'large'
    }
}
print("Nested dict: ",script_lang)
print(script_lang['js']['name'])
print(script_lang['js']['id'])
print(script_lang['framework']['name'])
print(script_lang['js']['community'])
print("")

student={
    1:{
        'roll':1,
        'name':'Akash',
        'address':'Ktm',
        'contact':123456,
        'gender':'M'
    },
    2:{
        'roll':2,
        'name':"Akriti",
        'address':'Pkr',
        'contact':246810,
        'gender':'F'
    }
}
print("Nested student dict: ",student)
print(student[1]['gender'])
print(student[1]['name'])
print(student[2]['gender'])
print(student[2]['name'])
print("")

staff={
    'id':1,
    'name':"Ram",
    'join_date':'05-04-2022',
    'skills':['python','git','js']
}
print("Dict with a list: ",staff)
print(staff['skills'][0])
print(staff['skills'][2])
print("")

emp={
    'id':1,
    'name':"Ram",
    'join_date':'05-04-2022',
    'country_visited':{'nep','ind','aus','usa'}
}
print("Dict with a set: ", emp)
(emp['country_visited'].discard('nep'))
print("Dict after discard 'nep' from set: ",emp)
print("")

phone={
    'id':1,
    'company':'samsung',
    'model':'A-25',
    'year':2020,
    'price':26999,
    'camera':'50MP'
}
print(phone.keys())
for data in phone.keys():
    if data=='price':
        print("Price exists")
        break
else:
    print("No such key found")

key_count=0
for val in phone.keys():
    key_count+=1
print("The total number of keys: ",key_count)

print(phone.values())
for i in phone.values():
        if i=='samsung':
             print("There is samsung")
             break
else:
     print("No such thing exists")

values_count=0
for j in phone.values():
     values_count+=1
print("Total values in dict are: ",values_count)

str_phone_value=str(phone.values)
print(type(str_phone_value))

krm={
    'id':1,
    'name':"Ram",
    'join_date':'05-04-2022',
    'country_visited':{'nep','ind','aus','usa'}
}
print(krm.items())
for val in krm.items():
     print(val)
print("")

missing_person={
    'id':1,
    'lname':'Doe',
    'country':'usa',
    'name':('John', 'Jane'),
    'gender':('male','female'),
    'cause':['murder','suicide'],
    'status':{'unidentified','pending','unresolved'}
}
print("Missing person Dict: ",missing_person)
print(missing_person.values())
for data in missing_person.values():
     if data=='John' or 'Jane':
          break
print("Jane or John exists")
for j in missing_person.keys():
     if j=='cause':
          print(missing_person[j])
     if j=='status':
          (missing_person[j].add("closed"))
          print("After adding value to the set: ",missing_person[j])
print("")

cricketer={
     1:{
        'squad no':5,
        'name':'Shyam',
        'position':'allrounder',
        'tests':50,
        'attributes':{'swing','finisher','fielder','injured','regular'}
     },
     2:{
        'squad no':18,
        'name':'Kumar',
        'position':'batsman',
        'tests':33,
        'attributes':{'opener','defensive','fielder','fit','patchy','swing'}
     }
}
print("Crickter dict: ",cricketer)
for data in cricketer.values():
     for value in data['attributes']:
          break
player_one_attributes=(cricketer[1]['attributes']).difference((cricketer[2]['attributes']))
print("Attribute of player 1: ",player_one_attributes)
player_two_attributes=(cricketer[2]['attributes']).difference((cricketer[1]['attributes']))
print("Attribute of player 2: ",player_two_attributes)
common_attributes=(cricketer[1]['attributes']).intersection((cricketer[2]['attributes']))
print("Common attributes of cricketers: ",common_attributes)
print("")

galaxy={
    'id':1,
    'company':'samsung',
    'model':'A-25',
    'year':2020,
    'price':26999,
    'camera':'50MP'
}
galaxy.setdefault('discount')
print("Dict after sedefault 'discount': ",galaxy)
galaxy.setdefault('price',24999)
print("Dict after sedefault: ",galaxy)
galaxy.setdefault('warranty','yes')
print(galaxy)

students={
     1:{
        'id':10,
        'name':'Sam',
        'country':'usa',
        'gender':'Male'
     },
     2:{
        'id':5,
        'name':'Jenny',
        'country':'uk',
        'gender':'Female'
     },
     3:{
        'id':2,
        'name':'Guy',
        'country':'aus',
        'gender':'Male'
     }
}
students[1].setdefault('fee','full')
print("After setdefault for student 1 ",students)
students[2].setdefault('fee','scholarship')
print("After setdefault for student 2 ",students)
students[3].setdefault('fee')
print("After setdefault for student 3 ",students)
print("")

student_data={
     'legacy':'yes',
     'status':'accepted',
     'house':'hobbiton',
     'realm':'mid-earth'
}
student_data1={
     'legacy':'no',
     'status':'pending',
     'house':'none',
     'realm':'earth'
}

students[1].update(student_data)
print("After updating ",students)
students[2].update(student_data)
print("After updating ",students)
students[3].update(student_data1)
print("After updating ",students)
print("")

sacked_manager={
     'name':'Graham Potter',
     'team':'chelsea',
     'postion':10,
     'spend':550,
     'pre-season':'no'
}
print("Unaltered dict: ",sacked_manager)
sacked_manager.setdefault('compensation')
sacked_manager.setdefault('contract-length')
sacked_manager.setdefault('total-duration')
print("After altering the dict: ",sacked_manager)

sacked_data={
     'compensation':10,
     'contract-length':5,
     'total-duration':0.7
}
sacked_manager.update(sacked_data)
print("After updating the dict: ",sacked_manager)

print("")

player_profile={
    'fname':'Lionel',
    'lname':'Messi',
    'team':'PSG',
    'country':'Argentina',
    'position':'forward',
    'squad no':30,
    'eu status':'yes'
}
print("POPITEM() ",player_profile.popitem())
print("After pop ",player_profile)
print("POPITEM() ",player_profile.popitem())
print("After pop ",player_profile)

player_detail={
     'ucl goals':125,
     'arg goals':102,
     'intl trophy':'yes'
}
player_profile.update(player_detail)
print("After updating with new dict: ",player_profile)
player_position={
     'position':'false 9'
}
player_profile.update(player_position)
print("After updating with new dict: ",player_profile)

print("POP(team): ",player_profile.pop('team'))
print("After pop ",player_profile)
print("POP(fname): ",player_profile.pop('fname'))
print("After pop ",player_profile)