#"badas"
def longPalindrome(s):
    
    if len(s) < 2 or s == s[::-1]: #바로 펠린드롬일 경우
        return s
    
    def expand(left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]: #left가 음수로 넘어간 경우, right가 최댓값을 넘어간 경우,
                                                                    #left와 right가 같지않은, 팰린드롬이 아닌경우
            left -= 1
            right += 1
        full = s[left + 1:right] #return 되는 경우는 while이 끝났다는거=>팰린드롬을 벗어났을 때
        #print(full)       
        return full


    result = ''

    for i in range(len(s) - 1): 
        result = max(result, expand(i,i+1), expand(i,i+2),key = len)
    return result

str = "baabsd" #baaab
print(longPalindrome(str))
            
        
        

