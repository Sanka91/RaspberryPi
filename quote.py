class Quote:

    def __init__(self, full_content: str, author: str):
        self.full_content = full_content
        self.author = author
        self.screen_content = self.calculate_chunks()

    def calculate_chunks(self):
        split_by_space_list = self.full_content.split(" ")
        target_string = ""

        for i in split_by_space_list:
            chunk = 30
            if len(target_string) + len(i) > chunk:
                target_string += "\n "
                target_string += i
                chunk += 30
            else:
                target_string += "{} ".format(i)
        return target_string