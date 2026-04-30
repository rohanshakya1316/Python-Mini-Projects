import textwrap

value = """This function wraps the input paragraph such that each line in the paragraph is at most
width characters long. The wrap method returns a list of output lines. The
returned list is empty if the wrapped 
output  has no content."""

wrapper = textwrap.TextWrapper(width=60)

word_list = wrapper.wrap(text=value)

for word in word_list:
    print(word)