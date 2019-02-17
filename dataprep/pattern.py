"""
Reads the file line by line, in each line, it finds a pattern, 
if the pattern is present, appends it with another pattern.
@author: Tripti Samal
"""


r = 0
strings = ("greek", "southern_us", "filipino", "indian", "jamaican", "spanish", "italian", "mexican", "chinese", "british", "thai", "vietnamese", "cajun_creole", "brazilian", "french", "japanese", "irish", "moroccan", "korean", "russian", )
with open('train.json', 'r') as istr:
    with open('train1.json', 'w') as ostr:
        for line in istr:
            if any(s in line for s in strings):
                buf = "%d" % r
                buf1 = buf + '\",'
                line = line.rstrip('\",\n') + buf1
                r = r + 1
            line = line.rstrip('\n')
            print(line, file=ostr)
