import csv
import json
import codecs
import unicodedata

def get_pneumonic(val):
    pneumonic = ""

    for i in range(0, 3):
        if  val[i] != ' ':
            pneumonic += val[i]
        else:
            pneumonic += val[i+1]
	
    pneumonic = pneumonic.upper() 
    pneumonic = strip_accents(pneumonic)

    return pneumonic


def is_alpha(word):
    try:
        return word.encode('ascii').isalpha()
    except:
       return False

def strip_accents(text):
    return ''.join(char for char in  unicodedata.normalize('NFKD', text) if unicodedata.category(char) != 'Mn')

region_dict = {}
city_dict = {}
dep_dict = {}

fname='up_reg.csv'

city_list = []
region_list = []
fregion_list = []
dep_list = []

def custom_dict_list_2_dict_dict(d):
    
    for k in d:
        l = d[k]
        it = iter(l)     
        new_value = dict(zip(it, it))
        d[k] = new_value

    return d


def custom_list2dict(list):
    dict = {}
    for itr in list:
        obj = {}
        obj[itr] = itr
        dict.update(obj)
    
    return dict

def custom_list2dict2(list):
    dict = {}
    for i in range(len(list)):
        dict[ get_pneumonic( list[i] )  ] =  list[i]
    
    return dict

def store_as_json(file_name, python_object):
    with open(file_name, 'w',  encoding='utf-8') as outfile:
        json.dump(python_object, outfile, ensure_ascii=False)


def extract_city_region_department(fname):
    global region_dict, city_dict, dep_dict
    global city_list, region_list, dep_list
    region_visited = {}
    city_visited = {}
    dep_visited = {}


    with open(fname, encoding='utf-8') as f:
        reader = csv.reader(f)
        i=0
        for row in reader:
            i = i + 1
            if i <= 3:
                print("skipping row : ", i)
                continue

            city   = row[0]
            region = row[1]
            dep = row[2]
            region = get_pneumonic(region)

            region_dict[region] = []
            city_dict[city] = []

            if city not in city_visited:
                city_list.append(city)
                city_visited[city] = True

            if region not in region_visited:
                region_list.append(region)
                region_visited[region] = True

            if dep not in dep_visited:
                dep_list.append(dep)
                dep_visited[dep] = True

		


def create_city_region_mapping(fname):
    global city_list, region_list
    global city_dict, region_dict
    region_visited = {}
    city_visited = {}
    dep_visited = {}


    with open(fname, encoding='utf-8') as f:
        reader = csv.reader(f)
        i=0
        for row in reader:
            i = i + 1
            if i <= 3:
                continue

            city   = row[0]
            region = row[1]
            region = get_pneumonic(region)
            region_dict[region].append(city)
            region_dict[region].append(city)
            city_dict[city].append(region)

def create_region_list(fname):
    global region_dict, city_dict, dep_dict
    global city_list, region_list, dep_list
    region_visited = {}
    city_visited = {}
    dep_visited = {}


    with open(fname, encoding='utf-8') as f:
        reader = csv.reader(f)
        i=0
        for row in reader:
            i = i + 1
            if i <= 3:
                print("skipping row : ", i)
                continue

            region = row[1]
	    
            if region not in region_visited:
                region_list.append(region)
                region_visited[region] = True


extract_city_region_department(fname)
create_city_region_mapping(fname)
create_region_list(fname)
region_dict 	= custom_dict_list_2_dict_dict(region_dict)
region_list 	= custom_list2dict2(region_list)
city_list 	= custom_list2dict(city_list)
dep_list 	= custom_list2dict(dep_list)

store_as_json('region_city_mapping.json', region_dict)
store_as_json('city_region_mapping.json', city_dict)
store_as_json('city_list.json', city_list)
store_as_json('region_list.json', region_list)
store_as_json('department_list.json', dep_list)

