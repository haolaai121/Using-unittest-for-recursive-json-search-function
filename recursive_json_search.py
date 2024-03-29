# Fill the Python code in this file
from test_data import *
ret_val=[]
def json_search(key,input_object):
	global ret_val
	if isinstance(input_object, dict): # Iterate dictionary
		for k, v in input_object.items(): # searching key in the dict
			if k == key:
				temp={k:v}
				ret_val.append(temp)
			if isinstance(v, dict): # the value is another dict so repeat
				json_search(key,v)
			elif isinstance(v, list): # it's a list
				for item in v:
					if not isinstance(item, (str,int)): # if dict or list repeat
						json_search(key,item)
	else: # Iterate a list because some APIs return JSON object in a list
		for val in input_object:
			if not isinstance(val, (str,int)):
				json_search(key,val)
	return ret_val
print(json_search("issueSummary",data))
