import sys

T= int(input())
result =list(sys.stdin.readline().strip() for _ in range(T))

result.sort()

for number in result :
    print(number)