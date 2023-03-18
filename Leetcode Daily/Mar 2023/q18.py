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