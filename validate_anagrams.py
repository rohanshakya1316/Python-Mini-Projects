# An anagram is a word or phrase formed by rearranging the exact letters of another word or phrase, using all original letters exactly once. Common examples include "secure" to "rescue," "dormitory" to "dirty room," and "a gentleman" to "elegant man"

def anagram(word1, word2): 
    word1 = word1.lower()
    word2 = word2.lower()

    return sorted(word1) == sorted(word2)

print(anagram("cinema", "iceman"))
print(anagram("cool", "loco"))
print(anagram("men", "women"))