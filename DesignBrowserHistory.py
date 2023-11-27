# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
# Implement the BrowserHistory class:
#   BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
#   void visit(string url) Visits url from the current page. It clears up all the forward history.
#   string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
#   string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

# using two stacks, slower runtime 
class BrowserHistory1: 
    
    def __init__(self, homepage):
        self.pastURL = []
        self.forwardURL = []
        self.homepage = homepage

    def visit(self, url):
        self.forwardURL = []
        self.pastURL.append(self.homepage)
        self.homepage = url 

    def back(self, steps):
        while steps and self.pastURL: 
            self.forwardURL.append(self.homepage)
            self.homepage = self.pastURL.pop()
        
            steps -= 1 
        return self.homepage

    def forward(self, steps):
        while steps and self.forwardURL: 
            self.pastURL.append(self.homepage)
            self.homepage = self.forwardURL.pop()
            
            steps -= 1
        return self.homepage
    
# using a list and pointer, faster runtime 
class BrowserHistory: 
    
    def __init__(self, homepage):
        self.urlList = [homepage]
        self.curPtr = 0 

    def visit(self, url):
        self.urlList = self.urlList[:self.curPtr + 1]
        self.urlList.append(url)
        self.curPtr = len(self.urlList) - 1

    def back(self, steps):
        self.curPtr = max(0, self.curPtr - steps)
        return self.urlList[self.curPtr]

    def forward(self, steps):
        self.curPtr = min(len(self.urlList) - 1, self.curPtr + steps)
        return self.urlList[self.curPtr]

# Test cases 
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
print(browserHistory.back(1))          
print(browserHistory.back(1))  
print(browserHistory.forward(1))
browserHistory.visit("linkedin.com")
print(browserHistory.forward(2))
print(browserHistory.back(2))             
print(browserHistory.back(7))               
 