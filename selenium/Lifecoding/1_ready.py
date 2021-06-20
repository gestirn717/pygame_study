import re

sentence = "I have a lovely dog, really. I am not telling a lie"

a = re.findall(r'\w+ly', sentence)
print(a)
