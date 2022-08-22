'clear()'
"it will clear the all elements and  return empty dictionary"
##dict = {'car':'popitem','method':'setdefault','details':'update'}
##dict.clear()
##print(dict)

'copy()'
"it will create new dictionary and not modified when the original dict is modified"
##dict = {'car':'popitem','method':'set','details':'fromkeys'}
##dict2 = dict.copy()
##dict.clear()
##print(dict)
##print(dict2)

'fromkeys'
"it will create new dictionary with specified keys with specified values"
##keys = ['delete','add','take']
##values= ['popitem','update','getvalue']
##value = 'insert'
##dict = dict.fromkeys(keys,values)
##dict2 = dict.fromkeys(keys,value)
##dict3 = dict.fromkeys(keys)#it will create default values for keys as 'None'
##print(dict)
##print(dict2)
##print(dict3)


'get()'
"gets the certain value for given key"
##dict = {'add':'update','delete':'pop','set':'setdafault'}
##print(dict.get('add'))
##print(dict.get(' '))#it returns none
##print(dict['add'])
##print(dict[' '])#it throws an error

'items()'
##"it returns a tuple with key, value pairs"
##dict = {'add':'update','delete':'pop','set':'setdafault'}
##dict['add'] = 'break'
##print(dict.items())

'keys()'
"it will return only keys of dict"
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##car["color"] = "black"#it will add in the dict
##x = car.keys()
##
##print(x)

'pop()'
"it accepts atleast one argument"
##methods = {
##    'create':'fromkeys',
##    'delete': 'popitem',
##    'add' : 'update',
##    'all' : 'items'
##    }
##methods.pop('add')#only takes keys not values
##print(methods)

'popitem()'
##"it deletes the last key,value pair in dictionary and it takes no argument"
##methods = {
##    'create':'fromkeys',
##    'delete': 'popitem',
##    'add' : 'update',
##    'all' : 'items'}
##methods.popitem()
##print(methods)

'setdefault()'
"it will gives the value of the key if key doesn't exit insert the key with a specified value"
##methods = {
##    'create':'fromkeys',
##    'delete': 'popitem',
##    'add' : 'update',
##    'all' : 'items'}
##print(methods.setdefault('create','dict'))#since it is having the value it returns the 'fromkeys' value
##print(methods.setdefault('key','value'))#it will  add to the last of the dict
##print(methods)


'update()'
"it will add the certain key to the dictionary"
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##
##car.update({"color":'white'})
##
##print(car)

'values()'
"it doesn't take any arguments and returns all values"
##methods = {
##    'create':'fromkeys',
##    'delete': 'popitem',
##    'add' : 'update',
##    'all' : 'items'}
##print(methods.values())
