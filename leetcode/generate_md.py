Class Solution:
    def f(self, title, link, code):
        self.title = title
        self.link = link
        self.code = code
    def d(self, source_lines):
        title = source_lines[0].split(". ")[1][:-1]
        return title
    def c(self, source_lines):
        link = source_lines[1].split("/")[-2]
        return link
    def v(self, source_lines):
        code = source_lines[3::]
        new_code = ""
        for new_line in code:
            new_code += new_line
        new_code = "```python\n" + new_code + "\n```"
        return new_code
    def m(self, source_lines):
        leetlink = source_lines[1]
        return leetlink
