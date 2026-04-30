from langdetect import detect 
text = input("Enter any text in any language: ")
print(detect(text))

import langid

text = input("Enter text: ")
print(langid.classify(text)[0]) 