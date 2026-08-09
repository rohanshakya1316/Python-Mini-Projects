from collections import defaultdict

# Mapper Class
class Mapper:
    def map(self, text):
        mapped_data = []
        # Process each line
        for line in text.splitlines():
            # Split line into words
            words = line.split()
            # Generate key-value pairs
            for word in words:
                mapped_data.append((word.lower(), 1))
        return mapped_data
    
# Reducer Class
class Reducer:
    def reduce(self, grouped_data):
        result = {}
        # Process each key and its values
        for word, values in grouped_data.items():
            # Add all values for the same word
            result[word] = sum(values)
        return result
    
# Input Data
text = """
hello cloud computing
I am Rohan Shakya
cloud computing is interesting
Rohan Shakya is doing lab
hello amazon emr
I am Rohan Shakya
Rohan Shakya is a student in SS College
cloud computing
"""

# Mapper Phase
mapper = Mapper()
mapped_data = mapper.map(text)
print("Mapper Output:")
for word, count in mapped_data:
    print(word, count)

# Shuffle and Sort Phase
grouped_data = defaultdict(list)
for word, count in mapped_data:
    grouped_data[word].append(count)

# Sort the keys
grouped_data = dict(sorted(grouped_data.items()))
print("\nShuffle and Sort Output:")
for word, values in grouped_data.items():
    print(word, values)

# Reducer Phase
reducer = Reducer()
final_output = reducer.reduce(grouped_data)

# Final Output
print("\nFinal Output:")
for word, count in final_output.items():
    print(word, count)
