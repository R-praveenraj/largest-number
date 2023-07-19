def largestNumber(array):
    singleArray = []
    for i in range(len(array)):
        if array[i] > 9:
            while array[i] > 0:
                singleArray.append(str(array[i] % 10))
                array[i] //= 10
        else:
            singleArray.append(str(array[i]))
    singleArray.sort(reverse=True)
    return "".join(singleArray)

array = list(map(int, input().split()))

print(largestNumber(array))