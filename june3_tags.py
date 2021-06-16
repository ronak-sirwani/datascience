from collections import Counter
import nltk

text= "Lionel Andrés Messi is an Argentine professional footballer who plays as a forward and captains both Spanish club Barcelona and the Argentina national team. Often considered as the best player in the world and widely regarded as one of the greatest players of all time."
token= nltk.word_tokenize(text)
tag= nltk.pos_tag(token)
print("Tokens with their Parts Of Speech : ")
print(tag)


fd= nltk.FreqDist(token)
print("\nTop 3 most common words: ",fd.most_common(3))