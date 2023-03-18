class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.browser.insert(self.idx+1,url)
        self.idx += 1
        self.browser = self.browser[:self.idx+1]

    def back(self, steps: int) -> str:
        if steps > self.idx:
            self.idx = 0
        else:
            self.idx -= steps
        return self.browser[self.idx]

    def forward(self, steps: int) -> str:
        if steps > (len(self.browser) - self.idx - 1):
            self.idx = len(self.browser)-1
        else:
            self.idx += steps
        return self.browser[self.idx]
    

# intuition:
# 1. A list can be used to store the history of the browser
# 2. A separate index variable can be used to keep track of the current page
# 3. The list can be truncated to the current page index + 1 when a new page is visited to remove the forward history
# 4. The index can be incremented or decremented based on the number of steps and the length of the list, keeping it within the bounds of the list

# solution
# 1. Create a list to store the history of the browser and assign it to the object
# 2. Create an index variable to keep track of the current page and assign it to the object. Initialize it to 0.
# 3. When a new page is visited, insert the new page at the index + 1 position in the list. Increment the index by 1.
# 4. Truncate the list to the index + 1 position to remove the forward history using the list slicing syntax.
# 5. When the back button is pressed, decrement the index by the number of steps. If the number of steps is greater than the index, set the index to 0. Else, set the index to the index - steps.
# 6. When the forward button is pressed, increment the index by the number of steps. If the number of steps is greater than the length of the list - index - 1, set the index to the length of the list - 1. Else, set the index to the index + steps.
# 7. Return the page at the index position in the list in both the back and forward functions.