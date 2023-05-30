import requests
import json
from urllib import request


TERRITORY_ID = '2927408'
PUBLISHED_SINCE = '2023-05-22'
PUBLISHED_UNTIL = '2023-05-22'

URL_SEARCH = f"https://queridodiario.ok.org.br/api/gazettes?territory_ids={TERRITORY_ID}&published_since={PUBLISHED_SINCE}&published_until={PUBLISHED_UNTIL}&excerpt_size=500&number_of_excerpts=1&size=10&sort_by=relevance"

try:
    response = requests.get(URL_SEARCH)
    if response.status_code == 200:
        result_json = response.json()
        str_name = TERRITORY_ID + "_" + PUBLISHED_SINCE.replace("-", "") + "_" + PUBLISHED_UNTIL.replace("-","")
        
        with open("gazettes/" + str_name + ".json", 'w') as f:
            json.dump(result_json, f)

        gazettes_list = result_json.get('gazettes')
        count = 0
        for gazette in gazettes_list:
            id_ = gazette['territory_id'] + "_" + gazette['date'].replace("-","") + "_" + str(count)
            txt_file = gazette['txt_url']
            request.urlretrieve(txt_file, "gazettes/" + id_ + ".txt")
            count += 1
    else:
        raise Exception("Erro na coleta do diário: " + response.status_code)
except Exception as e:
    print("Erro na requisição:")
    print(e)
