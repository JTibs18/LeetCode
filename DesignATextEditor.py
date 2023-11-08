# Design a text editor with a cursor that can do the following:
#   Add text to where the cursor is.
#   Delete text from where the cursor is (simulating the backspace key).
#   Move the cursor either left or right.
# When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.
# Implement the TextEditor class:
#   TextEditor() Initializes the object with empty text.
#   void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
#   int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
#   string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
#   string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.


class TextEditor: 

    def __init__(self):
        self.prefix = ''
        self.suffix = ''

    def addText(self, text):
        self.prefix += text

    def deleteText(self, k):
        numDeleteChars = min(k, len(self.prefix))
        self.prefix = self.prefix[:-k]
        return numDeleteChars 

    def cursorLeft(self, k): 
        if len(self.prefix) > 0:
            self.suffix = self.prefix[-k:] + self.suffix
            self.prefix = self.prefix[:-k]

        charsToReturn = min(10, len(self.prefix))
        return self.prefix[-charsToReturn:]


    def cursorRight(self, k): 
        if len(self.suffix) > 0: 
            self.prefix += self.suffix[:k]
            self.suffix = self.suffix[k:]

        charsToReturn = min(10, len(self.prefix))
        return self.prefix[-charsToReturn:]

# Test cases
textEditor = TextEditor()
textEditor.addText("leetcode")
print(textEditor.deleteText(4))
textEditor.addText("practice")
print(textEditor.cursorRight(3))
print(textEditor.cursorLeft(8))
print(textEditor.deleteText(10))
print(textEditor.cursorLeft(2))
print("CUROSOR")
print(textEditor.cursorRight(6))
