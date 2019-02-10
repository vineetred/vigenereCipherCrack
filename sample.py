all_freq = {}
file = open("7b.txt", "r") 
test_str = str(file.read())
from collections import Counter 
res = Counter(test_str) 
print("HELLO")
print(res)
import matplotlib.pyplot as plt
letter_freq = ['e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z']

print(res)
new = test_str
for i in (res.most_common()):
    j = 0
    # print(i[0])
    new.replace(i[0],letter_freq[j])
    j+=1
hell = open("cracled.txt",'w')
hell.write(new)

