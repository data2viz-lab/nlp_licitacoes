import os
import re 
import json 



class ProcessGazette():
    def __init__(self, BASE_DIR):
        self.BASE_DIR = BASE_DIR

    def break_pages(self, gazette_file, pattern, save_file=False):
        with open(os.path.join(self.BASE_DIR, gazette_file), 'r', encoding='utf-8') as f:
            text = f.read().replace('\n', ' ')

        pages = re.split(pattern=pattern, string=text)

        count = 0
        dictionary_pages = {}
        for page in pages:
            dictionary_pages[count] = page
            count += 1

        if save_file:
            # Criar um nome curto para o arquivo usando um identificador e a data
            identifier = gazette_file.split('.')[0]  # Pode precisar ajustar isso dependendo dos nomes dos seus arquivos
            date_match = re.search(r'\d{2} \w+ \d{4}', text)
            date_str = date_match.group() if date_match else 'unknown_date'
            short_name = f"{identifier}_{date_str}_pages.json"
            
            with open(os.path.join(self.BASE_DIR, short_name), 'w') as f:
                json.dump(dictionary_pages, f)

        return dictionary_pages, short_name



    
#teste