import collections

class ListNode: #각각의 node값들
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        
    


class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        #size가 1000이고 위에 ListNode를 원소로 갖는 dic을 생성


    def put(self, key, value):

        #해싱 => key값을 1000으로 나눈 나머지값
        #우선 단순하게 만들었다  
        #but key값은 달라도 index값이 같을 수 있음
        #그래서 개별 체이닝 방식 사용
        index = key % self.size

        #만약 테이블에 해당 index에 해당하는 값이 없으면
        #[index] in None 이 아닌 [index].value is None인 이유
        #[index]가 nonde으로 검색하면 __init__의 
        # defaultdic은 존재하지않는 인덱스로 조회 시도 시
        #에러가 아닌 바로 default객체를 생성하기 때문
        #which means => 빈 ListNode를 생성하기때문에 값으로 조회            
        if self.table[index].value is None:
            #해당 index가 없으므로 생성 후 Listnode를 추가해준다. 
            self.table[index] = ListNode[key,value]
            # ex) 'index01' => 'key01' : 'val01'
            #그리고 종료
            return

        #else 해당 index에 ListNode가 존재하는경우
        #which means => Hash Collision 해시충돌이 발생할 경우
        #개별 체이닝 방식 사용
        p = self.table[index]
        while p:
            if p.key == key:  #ex)01 -> hasing -> index같은 경우 발생(hash collision) -> 같은 key값이 존재할 경우
                #기존 key값의 value를 update하고 메서드를 빠져나간다. 
                p.value =value
                return
            if p.next is None: #p.next 가 None인경우
                #which means => none이 나올 때 까지 즉 
                #해당 인덱스의 엮인 LinkedList의 끝이 나올 때 까지
                #ex)01 -> hasing -> index같은 경우 발생(hash collision) -> 같은 키가 안나옴(new key)-> 
                #반복문 빠져나온 후 새로운 ListNode 연결  
                break
            p = p.next

        p.next = ListNode(key,value)        
        

    def get(self, key): #key에 해당하는 value 조회, 없으면 return -1
        #위와 같은 방법으로 해싱
        index = key % self.size

        if self.table[index].value is None: #해당하는 index의 value값 없으면 return -1
            return -1
        
        #해당하는 index의 value가 들어있으면 
        p = self.table[index] 
        while p: # ex)01 -> hasing -> index가 같은 경우 발생(hash collision) -> 반복문 돌려서 해당 key값 검색
            if p.key == key: #같은 키가 찾음-> 해당 key(p)의 value return
                return p.value
            p = p.next   
        return -1 #반복문 끝까지 갔지만 같은 키가 안나옴(new key) -> return -1
        

    def remove(self, key):        
         #위와 같은 방법으로 해싱
        index = key % self.size
        if self.table[index].vlaue is None: #해당 index 없으면 그냥 return
            return
        
        p =self.table[index] #해당 index 찾으면 
        
        if p.key == key: #찾고자 하는 key값이 첫번째 노드일경우 => if 첫번째node의 키값과 == 지우고자하는 key 값이 같을경우 match
            self.table[index] = ListNode() if p.next is None else p.next
            #self.table의 해당 인덱스에 해당하는 ListNode 값은 = if p.next가 None이면 빈 ListNode() 반환, 아니면 다음 p.next 반환
            #이유는 다른 함수들에서 쓴 self.table[index].vlaue is None으로 에러가 발생하기에 빈 ListNode를 넣어준다

        prev = p #연결리스트 node 삭제
        while p: #해당하는 key값을 찾기위해 while 사용
            if p.key == key:
                prev.next = p.next # prev -> p -> p.next 가 있으면 prev를 p를 건너뛰고 p.next에 연결시켜 의 연결고리를 자른다
                return
            prev, p = p, p.next #현재값을 prev로 다음 next값을 현재값으로 변경 뒤 다시 반복

