def even_fibonacci(num=4000000):

    i,j = 1,1
    ans = 0
    while j <= num:
        # print(j)
        if j % 2 == 0:
            ans += j
        i,j = j,j+i
    return ans

if __name__ == '__main__':
    print(even_fibonacci()) #4613732
