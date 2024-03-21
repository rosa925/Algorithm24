count = int(input("노드의 개수: "))                          #노드의 개수를 입력받는다
mylist = []                                                 #데이터를 저장할 빈 리스트 생성
for i in range(count):                                      #입력 받은 노드의 개수만큼 반복
    data = int(input("노드 %d의 데이터: " % (i+1)))          #노드를 입력받음
    mylist.append(data)                                     #데이터를 순서대로 저장

print("리스트의 내용: ", mylist)
