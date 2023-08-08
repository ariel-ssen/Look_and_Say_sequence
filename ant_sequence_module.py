def ant_sequence(num):
    ant = [1] #첫번째 개미 수열
    for i in range(num - 1): #파이썬의 숫자는 0부터 시작 
        target = ant[0] #리스트 원소 
        new_ant = [] #다음 개미 수열을 저장할 리스트 
        count = 1 #1개씩 카운팅
        for j in range(1, len(ant)): # 현재 개미 수열에서 숫자 하나씩 살펴보며 개수 세기 
            if target != ant[j]: #숫자의 연속이 끝긴경우 
               
                new_ant.append(count) #갯수를 추가한다.
                new_ant.append(target) #리스트 원소를 추가한다.
                target = ant[j]
                count = 1
            else: #숫자가 게속 연속적으로 나오는 경우 개수 1씩 증가 
                count += 1

        new_ant.append(count) # 마지막에 저장되어있는 target과 count를 다음 개미 수열에 추가함
        new_ant.append(target)
        ant = new_ant

    return ''.join(map(str, ant))

def solution(ant):
    ant, leng = list(ant), len(ant)
    answer = ''
    if leng % 2 == 0:
        answer = ''.join(ant[leng // 2 - 1:leng // 2 + 1])#인덱싱 슬라이스
    else: 
        ## 2로 나누어 떨어지지 않은 개미수열
        answer = ''.join(ant[leng // 2:leng // 2 + 1])
    return answer

num = int(input("몇 번째 개미 수열을 구할까요?"))
ant_sequence_result = ant_sequence(num)
print(ant_sequence_result)
print(solution(ant_sequence_result))