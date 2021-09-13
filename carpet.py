import os
os.system('cls')
def set_divisor(num) :
    divisor = []
    for i in range(1,num+1) :
        if num % i == 0 :
            divisor.append(i)
    return divisor

def solution(brown, yellow):
    divisor = set_divisor(brown + yellow)
    for i in range(len(divisor) // 2 + 1) :
        x = divisor[i]
        y = (brown+yellow) // x
        if (x*y - (x-2) * (y-2)) == brown :
            answer = sorted([x,y], reverse=True)
            break
    return answer

print(solution(10,2))	#[4, 3]
print(solution(8,1))   #[3, 3]
print(solution(24,24)) #[8, 6]