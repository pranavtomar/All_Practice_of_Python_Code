"""Sample Input :
"Hello12345 Hello12345 a Hello12345"
"hello1234 bhs hello123 sunny hello1234"
Sample Output :
"#########a#########"
[H,e,l,o,1,2,3,4,5,a] """

import re
def convert_string(str):
    pattern = r'\w+'
    result = re.sub(pattern, lambda match: '#' * len(match.group()), str)
    return result


str = input("Enter a string:\n")
print(str)

output = convert_string(str)
print(output)
list = []
for char in str:
    if char not in list and char != " ":
        list.append(char)
print(list)




