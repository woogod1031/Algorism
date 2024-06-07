import collections
from structures import Stack


def removeDuplicateLetters(s): # "cbacdcbc"
    counter,stack,seen = collections.Counter(s), [], set()
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
            
        while stack and counter[stack[-1]] > 0 and char < stack[-1]:
           seen.remove(stack.pop())

        stack.append(char) #acd
        seen.add(char)

    return ''.join(stack)

ss = "bcabc"
print(removeDuplicateLetters(ss))