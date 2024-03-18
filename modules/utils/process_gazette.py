import re 
import json 



class ProcessGazette():

    def __init__(self, BASE_DIR):

        self.BASE_DIR = BASE_DIR


    def break_pages(self, gazette_file, pattern, save_file=False):


        with open(self.BASE_DIR + gazette_file, 'r', encoding='utf-8') as f:
            text = f.read().replace('\n', ' ')
            

        pages = re.split(pattern=pattern,string=text)

        count = 0
        dictionary_pages = {}
        for page in pages:
            dictionary_pages[count] = page
            count += 1


        if save_file:

            with open(self.BASE_DIR + gazette_file.split(".")[0] + "_pages.json", 'w') as f:
                json.dump(dictionary_pages, f)

        return dictionary_pages
    

    