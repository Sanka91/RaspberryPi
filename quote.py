class Quote:

    def __init__(self, full_content: str, author: str):
        self.full_content = full_content
        self.author = author
        if len(self.full_content) > 25:
            self.screen_content = "{}...".format(self.full_content[:25])
        else:
            self.screen_content = self.full_content
