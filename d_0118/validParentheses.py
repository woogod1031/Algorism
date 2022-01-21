from structures import Stack

# s "[]()"
def is_valid(s):
    stack = Stack()
    table = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }

    opener= ['[','{','(']    

    for char in s:
        if char in opener:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            if table[char] != stack.pop():
                return False  
    return stack.is_empty()       
    


print(is_valid("()[]{}"))
print(is_valid("{[]}"))
print(is_valid("({[]})"))