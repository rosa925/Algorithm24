##18번(1)
count = int(input("노드의 개수: "))                          #노드의 개수를 입력받는다
mylist = []                                                 #데이터를 저장할 빈 리스트 생성
for i in range(count):                                      #입력 받은 노드의 개수만큼 반복
    data = int(input("노드 %d의 데이터: " % (i+1)))          #노드를 입력받음
    mylist.append(data)                                     #데이터를 순서대로 저장

print("리스트의 내용: ", mylist)


##18번(2)
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

def printList(head, msg="생성된 연결 리스트: "):
    print(msg, end="")
    n = head
    while n != None:
        print(n.data, end="->")
        n = n.link
    print()

head = None
tail = None
count = int(input("노드의 개수: "))
for i in range(count):
    data = int(input("노드 %d의 데이터: " % (i+1)))
    n = Node(data, None)
    if head == None:
        head = tail = n
    else:
        tail.link = n
        tail = n
printList(head)