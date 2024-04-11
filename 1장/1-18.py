##18번(1)
count = int(input("노드의 개수: "))   #노드의 개수를 입력받는다
mylist = []      #데이터를 저장할 빈 리스트 생성
for i in range(count):       #입력 받은 노드의 개수만큼 반복
    data = int(input("노드 %d의 데이터: " % (i+1)))   #노드를 입력받음
    mylist.append(data)   #데이터를 순서대로 저장

print("리스트의 내용: ", mylist)


##18번(2)
class Node:
    def __init__(self, elem, next=None):
        self.data = elem  # 노드의 데이터를 저장하는 변수
        self.link = next  # 다음 노드 링크

def printList(head, msg="생성된 연결 리스트: "):
    print(msg, end="")  # 연결 리스트의 시작을 나타내는 메시지
    n = head  # 현재 노드를 가리키는 변수 초기화
    while n != None:
        print(n.data, end="->")  # 현재 노드의 데이터 출력
        n = n.link  # 다음 노드로 이동
    print()  # 줄바꿈

head = None  # 연결 리스트의 첫 번째 노드 변수
tail = None  # 연결 리스트의 마지막 노드 변수
count = int(input("노드의 개수: "))  # 사용자로부터 노드의 개수 입력 받음
for i in range(count):
    data = int(input("노드 %d의 데이터: " % (i+1)))  # 사용자로부터 각 노드의 데이터 입력 받음
    n = Node(data, None)  # 새로운 노드 생성
    if head == None:  # 연결 리스트가 비어있는 경우
        head = tail = n  # 새로운 노드를 연결 리스트의 첫 번째 노드로 지정
    else:
        tail.link = n  # 마지막 노드의 링크를 새로운 노드로 설정
        tail = n  # tail을 새로운 노드로 업데이트
printList(head)  # 생성된 연결 리스트 출력
