def crack(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result = result + chr((ord(char) + shift - 97) % 26 + 97)
    print("Shift = ",shift)
    print(result)

cipher = "hgnodxnthmsdqbdossghrrdbqdssqzmrlhrrhnmvhsgntszmxdqqnqsghrsqzmrlhrrhnmgzrsqzudkkdczlhkkhnmkhfgsxdzqrsnhmenqlxntsgzsvdzqdbnlhmfrnnm"

for i in range(0,25):
    crack(cipher, i)