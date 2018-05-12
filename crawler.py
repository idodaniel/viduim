import json
from pprint import pprint
from search_dict import SearchDict
import collections
import re

def get_gender_key(msg):
    girl_emoji = re.compile(u'\U0001F534')
    boy_emoji = re.compile(u'\U0001F535')

    if re.search(girl_emoji, msg):
        return 0
    elif re.search(boy_emoji, msg):
        return 1
    else:
        return 2

def save_results(results):
    res = []
    total_count = results[0]['count'] + results[1]['count']
    for key in results[0]:
        res.append({
            'parameter'       : key, 
            'percent_f'       : ((results[0][key] / results[0]['count']) * 100),  
            'percent_m'       : ((results[1][key] / results[1]['count']) * 100), 
            'num_f'           : results[0][key], 
            'num_m'           : results[1][key],
            'percent_sum'     : (((results[0][key] + results[1][key]) / total_count) * 100),
            'percent_num'     : (results[0][key] + results[1][key])
        })
    return res

def print_result(res_list):
    print("\nParameter\t%(F)\t%(M)\t\tNum(F)\tNum(M)\t\tSum(%)\tSum")
    print("===="*19)
    for result in res_list:
        print("{0:<12s}:\t{1:.1f}%\t{2:.1f}%\t||\t{3}\t{4}\t||\t{5:.1f}%\t{6}".format(
            result['parameter'], result['percent_f'], result['percent_m'],
            result['num_f'], result['num_m'], result['percent_sum'], result['percent_num']))

    #print("\nUnknown gender count: {0}".format(results[2]['count']))

def main():

    search_fields = SearchDict().get()

    with open('data.json', encoding="utf8") as f:
        data = f.read()
        data.encode('unicode_escape')
        data = json.loads(data, strict=False)['data']

        gender = dict({'count': 0})
        for key in search_fields:
            gender[key] = 0

                   #girl          #boy            #unknown
        results = [gender.copy(), gender.copy(), {'count': 0}]

        for conf in data:
            try:
                msg = conf['message']
            except KeyError:    # happens when no message value, for example: (X updated their cover photo)
                continue

            gender_key = get_gender_key(msg)
            results[gender_key]['count'] += 1
            
            if gender_key != 2:
                for search_key, regex in search_fields.items():
                    if re.search(regex, msg):
                        results[gender_key][search_key] += 1
        
        #print_result(results)
        res_dict = sorted(save_results(results), key=lambda k: k['percent_sum'], reverse=True)
        print_result(res_dict)

if __name__ == "__main__":
    main()