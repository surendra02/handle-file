import json
import re
def search(file, search_list):
    """This function takes two arguments 1)- take a file in which you want to search data 2)- take a search list"""
    result = {}
    file_dict = {}
    a = open(file,'r')
    file_data = a.readlines()
    # print(f"file lenth : {len(file_data)} and my file data is : {file_data}")
    for i in file_data:
        temp = i.split(":")
        heart_atr = temp[0]
        a=temp[1].strip()           # Remove whitespace[start or end] from values
        heart_value = a.split(" ")[0]
        number = re.findall("\d{0,9}[.+]\d{0,9}", heart_value)
        if number!=[]:
            heart_value = float("".join(number))
            file_dict.update({heart_atr: heart_value})
        else:
            file_dict.update({heart_atr: heart_value})
    for i in search_list:
        if i in file_dict:
            result.update({i:file_dict[i]})
        else:
            result.update({i:"None"})
    return json.dumps(result)
your_data=search(file="in.html",search_list=["Name",'Heart Valuem','Coronary Calcium','Coronary Calcium Range'])
print(your_data,"<--json data")