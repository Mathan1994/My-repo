# program 1:
import re
line = "xyz intensive.learnings@cig.comna.com purple monkey"
match = re.findall(r'[\w\.-]+@[\w\.]+', line)
for i in match:
    print(i)







