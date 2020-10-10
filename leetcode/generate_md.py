Class Solution:
    def __init__(self, title, link, code):
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
with open("source_leetcode_data.txt", 'r') as in_file:
    source_lines = in_file.readlines()
title = source_lines[0].split(". ")[:-1]
link = source_lines[1].split("/")[-2]
code = source_lines[3::]
leetlink = source_lines[1]
plus, other = '', ''
with open("intervals.md", 'r') as in_file:
    source_lines1 = in_file.readlines()
for i in range(1, len(source_lines1)):
    if source_lines1[i][0] == "+":
        plus += source_lines1[i]
    else:
        other += source_lines1[i]
out_file = open("intervals.md", 'w')
out_file.write("# {}\n\n{}".format("Intervals", plus))
out_file.write("+ [{}](#{}){}\n".format(Solution.d(title, source_lines), Solution.c(link, source_lines), other))
out_file.write("\n## {}\n\n".format(Solution.d(title, source_lines)))
out_file.write("{}\n".format((Solution.m(leetlink, source_lines))))
out_file.write("{}".format(Solution.v(code, source_lines)))
out_file.close()
