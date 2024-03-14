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
    
if __name__ == "__main__":
    def word_counter(directory, file):
        pg = ProcessGazette(directory)
        pg.break_pages(file + ".txt","ANO [X|V|I]+ ",True)
        
        with open(directory+file+'_pages.json', 'r') as f:
            data = json.load(f)
        
        for page, content in data.items():
            print(f"Top 10 palavras na página {page+1}:")
            word_count = {}
            words = content.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
            for word, count in sorted_word_count[:10]:
                print(f"{word}: {count}")
            print("\n")
        
    
    word_count = word_counter('notebooks/gazettes/', '2927408_20230704_0')
    