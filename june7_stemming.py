from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from krovetzstemmer import Stemmer 

ks = Stemmer() 
ps= PorterStemmer()
ss= SnowballStemmer(language='english')
while True:
    word= input("Enter word: ")
    print("Porter stem of",word," : ",ps.stem(word))
    print("Krovetz stem of",word,": ",ks.stem(word))
    print("Snowball stem of",word," : ",ss.stem(word))
    res= input("Want to enter more words ?")
    if res=='yes' or res== 'y':
        continue
    else:
        break    
