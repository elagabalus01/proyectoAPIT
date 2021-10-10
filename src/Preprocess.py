from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from pprint import pprint
import json
class Preprocess:
    def __init__(self,file=None):
        self.stemmer=SnowballStemmer("spanish")
        self.stopwords=stopwords.words("spanish")
        self.results=None
        self.filename=file

    def loadWords(self):
        try:
            with open(self.filename,'r') as file:
                self.results=json.loads(file.read())
        except FileNotFoundError:
            print("No existe un archivo con las palabras")
            print("Se creará uno al iniciar el entrenamiento")

    def countWords(self,words:list,words_area:dict):
        
        if not self.results:
            self.results={}
        for word in words:
            if word not in self.stopwords:
                stem=self.stemmer.stem(word)
                if stem not in self.results.keys():
                    self.results[stem]=1
                    print("Print primera vez palabra")
                    if stem not in words_area.keys():
                        print("Print primera vez")
                        words_area[stem]=1
                        words_area['words_overall']+=1
                    else:
                        words_area[stem]+=1
                        print("Posterior")
                else:
                    self.results[stem]+=1
                    print("Posterior palabra")
        self.results={
            k: v for k, v in
            sorted(self.results.items(), key=lambda item: item[1],reverse=True)
        }
        pprint(self.results,sort_dicts=False)
        print(words_area)

    def serialize(self):
        if self.filename:
            with open(self.filename,'w') as file:
                file.write(json.dumps(self.results))
        else:
            print("No es serializable ya que no se definió el archivo para escribir")

if __name__=="__main__":
    from TextExtractor import TextExtractor
    file=TextExtractor('./papers/paper.pdf')
    text=file.pageRangeText(1,5)
    preproceser=Preprocess()
    preproceser.loadWords()
    preproceser.countWords(text)