def addFibonacci(arr1,arr2) :
    result = []
    result.append(arr1[0]+arr2[0])
    result.append(arr1[1]+arr2[1])
    return result

if __name__ == '__main__':
    fibo = [[1,0],[0,1],[1,1],[1,2]]
    T = int(input())

    for _ in range(T) :
        fiboLen = len(fibo)-1

        N = int(input())

        if (N > fiboLen) :
            for i in range(fiboLen+1,N+1) :
                fibo.append(addFibonacci(fibo[i-1],fibo[i-2]))

        print(f'{fibo[N][0]} {fibo[N][1]}')




