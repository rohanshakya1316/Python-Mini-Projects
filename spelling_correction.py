from textblob import TextBlob

def Convert(str): 
    li = list(str.split())
    return li

str1 = input("Enter your word: ")

words = Convert(str1)

corrected_words = []

for i in words: 
    corrected_words.append(TextBlob(i))
print("Wrong words: ", words)

print("Corrected Words are: ")
for i in corrected_words: 
    print(i.correct(), end=" ")