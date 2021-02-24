import csv
import json
import codecs

data = {}

region_dict = {}
city_dict = {}

fname='/home/viki/Downloads/up_reg.csv'
#fname='/home/viki/Downloads/test_city.csv'

city_list = []
city_visited = {}
region_list = []
region_visited = {}

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
        else:
            print("duplicate region found", region)



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
        region_dict[region].append(city)
        city_dict[city].append(region)


#print("city dict")
#print(city_dict)
#print("regiondict")
#print(region_dict)

with open('region_city_mapping.json', 'w',  encoding='utf-8') as outfile:
    json.dump(region_dict, outfile, ensure_ascii=False)

with open('city_region_mapping.json', 'w',  encoding='utf-8') as outfile:
    json.dump(city_dict, outfile, ensure_ascii=False)

with open('city_list.json', 'w',  encoding='utf-8') as outfile:
    json.dump(city_list, outfile, ensure_ascii=False)

with open('region_list.json', 'w',  encoding='utf-8') as outfile:
    json.dump(region_list, outfile, ensure_ascii=False)

