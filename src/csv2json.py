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

data = {}

region_dict = {}
city_dict = {}
dep_dict = {}

fname='up_reg.csv'

city_list = []
city_visited = {}
region_list = []
fregion_list = []
region_visited = {}
fregion_visited = {}
dep_list = []
dep_visited = {}

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

with open(fname, encoding='utf-8') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        i = i + 1
        if i <= 3:
            #print(row)    
            continue

        city   = row[0]
        region = row[1]
        dep = row[2]

        region_full = region
        region = get_pneumonic(region)
		
	
        region_dict[region] = []
        city_dict[city] = []

        if city not in city_visited:
            city_list.append(city)
            city_visited[city] = True
        #else:
        #    print("duplicate city found", city)

        if region not in region_visited:
            region_list.append(region)
            region_visited[region] = True
        #else:
           # print("duplicate region found", region)

        if region_full not in fregion_visited:
            fregion_list.append(region_full)
            fregion_visited[region] = True
        #else:
           # print("duplicate region found", region)


        if dep not in dep_visited:
            dep_list.append(dep)
            dep_visited[dep] = True

		


with open(fname, encoding='utf-8') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        i = i + 1
        if i <= 3:
            #print(row)    
            continue

        city   = row[0]
        region = row[1]
        region = get_pneumonic(region)
        region_dict[region].append(city)
        region_dict[region].append(city)
        city_dict[city].append(region)

region_dict = custom_dict_list_2_dict_dict(region_dict)
fregion_list = custom_list2dict(fregion_list)
city_list = custom_list2dict(city_list)
dep_list = custom_list2dict(dep_list)

with open('region_city_mapping.json', 'w',  encoding='utf-8') as outfile:
    json.dump(region_dict, outfile, ensure_ascii=False)

with open('city_region_mapping.json', 'w',  encoding='utf-8') as outfile:
    json.dump(city_dict, outfile, ensure_ascii=False)

with open('city_list.json', 'w',  encoding='utf-8') as outfile:
    json.dump(city_list, outfile, ensure_ascii=False)

with open('region_list.json', 'w',  encoding='utf-8') as outfile:
    json.dump(fregion_list, outfile, ensure_ascii=False)

with open('department_list.json', 'w',  encoding='utf-8') as outfile:
    json.dump(dep_list, outfile, ensure_ascii=False)


'''
i = 0
for c in city_list:
  i = i+1

print("number of cities = ", i)

out="array(";
dup = {}
i = 0
for val in region_list:
    i = i+1
    pneumonic = val[ 0: 3: 1]
    pneumonic = pneumonic.upper() 
    pneumonic = strip_accents(pneumonic)
    if val not in dup:
        dup[val] = True;
    else:
        print("duplicate entry found")
	
    out = out+ "\"" + pneumonic + "\"" + " => " + "\""  +  val + "\"" + ", "
	
out = out + ")";

print(out)

print("number of regions = ", i)
print(get_pneumonic("chennai"))
'''	
