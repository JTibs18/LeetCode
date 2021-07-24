# HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

# The special characters and their entities for HTML are:

# Quotation Mark: the entity is &quot; and symbol character is ".
# Single Quote Mark: the entity is &apos; and symbol character is '.
# Ampersand: the entity is &amp; and symbol character is &.
# Greater Than Sign: the entity is &gt; and symbol character is >.
# Less Than Sign: the entity is &lt; and symbol character is <.
# Slash: the entity is &frasl; and symbol character is /.
# Given the input text string to the HTML parser, you have to implement the entity parser.

# Return the text after replacing the entities by the special characters.

def entityParser(text):
    newSen = ""
    indx = 0

    while indx < len(text):
        if text[indx] == "&":
            if len(text[indx:]) > 3 and text[indx + 1] == "a" and text[indx + 2] == "m" and text[indx + 3] == "p" and text[indx + 4] == ";":
                indx += 5
                newSen += "&"
            elif len(text[indx:]) > 5 and text[indx + 1] == "q" and text[indx + 2] == "u" and text[indx + 3] == "o" and text[indx + 4] == "t" and text[indx + 5] == ";":
                indx += 6
                newSen += '"'
            elif len(text[indx:]) > 5 and text[indx + 1] == "a" and text[indx + 2] == "p" and text[indx + 3] == "o" and text[indx + 4] == "s" and text[indx + 5] == ";":
                indx += 6
                newSen += "'"
            elif len(text[indx:]) > 3 and text[indx + 1] == "g" and text[indx + 2] == "t" and text[indx + 3] == ";":
                indx += 4
                newSen += '>'
            elif len(text[indx:]) > 3 and text[indx + 1] == "l" and text[indx + 2] == "t" and text[indx + 3] == ";":
                indx += 4
                newSen += '<'
            elif len(text[indx:]) > 6 and text[indx + 1] == "f" and text[indx + 2] == "r" and text[indx + 3] == "a" and text[indx + 4] == "s" and text[indx + 5] == "l" and text[indx + 6] == ";":
                indx += 7
                newSen += '/'
            else:
                newSen += text[indx]
                indx += 1
        else:
            newSen += text[indx]
            indx += 1

    return newSen

#Test cases
text = "&amp; is an HTML entity but &ambassador; is not."
print(entityParser(text))

text = "and I quote: &quot;...&quot;"
print(entityParser(text))

text = "Stay home! Practice on Leetcode :)"
print(entityParser(text))

text = "x &gt; y &amp;&amp; x &lt; y is always false"
print(entityParser(text))

text = "leetcode.com&frasl;problemset&frasl;all"
print(entityParser(text))

text = "&&&"
print(entityParser(text))
