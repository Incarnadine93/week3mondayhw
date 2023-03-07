import re

f = open('regex_test.txt')
content = f.read()

content_pattern = re.compile("^[A-Za-z]+([\ A-Za-z]+)")
for x in my_emails:
    pattern = re.compile("^[A-Za-z]+([\ A-Za-z]+)")
    if pattern.match(x):
        print(x)
    else:
        print('None')