import re 
import json 

def break_pages(BASE_DIR, gazette_file, pattern):


    with open(BASE_DIR + gazette_file, 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', ' ')
        

    pages = re.split(pattern=pattern,string=text)

    count = 0
    dictionary_pages = {}
    for page in pages:
        dictionary_pages[count] = page
        count += 1


    with open(BASE_DIR + gazette_file.split(".")[0] + "_pages.json", 'w') as f:
        json.dump(dictionary_pages, f)

        
if __name__ == "__main__":

    break_pages("../output/gazettes/", "2927408_20230522_0.txt", "ANO [X|V|I]+ ")
    