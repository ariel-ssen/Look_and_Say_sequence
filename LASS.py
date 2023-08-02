def ant_sequence(num):
    ant = [1]

    for i in range(num - 1):
        target = ant[0]
        new_ant = []
        count = 1
        for j in range(1, len(ant)):
            if target != ant[j]:
               
                new_ant.append(count)
                new_ant.append(target)
                target = ant[j]
                count = 1
            else:
                count += 1

        new_ant.append(count)
        new_ant.append(target)
        ant = new_ant

    return ''.join(map(str, ant))


def solution(ant):
    ant, leng = list(ant), len(ant)
    answer = ''
    if leng % 2 == 0:
        answer = ''.join(ant[leng // 2 - 1:leng // 2 + 1])
    else:
        answer = ''.join(ant[leng // 2:leng // 2 + 1])
    return answer



num = int(input("몇 번째 개미 수열을 구할까요?"))
ant_sequence_result = ant_sequence(num)
print(ant_sequence_result)
print(solution(ant_sequence_result))
