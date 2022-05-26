class Quote:

    def __init__(self, full_content: str, author: str, profession: str):
        self.full_content = full_content
        self.author = author
        self.profession = profession
        self.screen_content = self.calculate_chunks()

    def calculate_chunks(self):
        split_by_space_list = self.full_content.split(" ")
        target_string = ""
        chunk_start = 35
        max_lines_of_text = 4

        for i in split_by_space_list:
            if max_lines_of_text == 0:
                target_string += "..."
                break
            if len(target_string) + len(i) > chunk_start:
                target_string += "\n"
                target_string += "{} ".format(i)
                chunk_start += 35
                max_lines_of_text -= 1
            else:
                target_string += "{} ".format(i)
        return target_string