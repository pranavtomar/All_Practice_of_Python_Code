str = input("Enter a string:\n")
subStr = input("Enter a subString:\n")

word = str.split()
print("\n\nLength",len(word))

part = str.partition(subStr)
print(part[1].strip(),part[2].strip())
print(part[0].strip(),part[1].strip())


