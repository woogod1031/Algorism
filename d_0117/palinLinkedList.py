def isPalindrome(head):
    q = []

    if not head: #head가 빈값이면 => 처음부터 0값이거나 그러면
        return True

    node = head

    while node is not None: #node값이 다 검사할 때 까지
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop(): #배열의 양끝원소들을 비교한 후 빼준다
            return False
    return True            

