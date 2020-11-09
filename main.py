def findWord(matchcase):
    arr = []
    for lcase in matchcase:
        a,b = lcase[0],lcase[-1]
        if a in arr:
            idx = arr.index(a)
            if len(arr)-1 != idx:
                arr = arr[:idx]+[b]+arr[idx:]
            else:
                arr.append(b)
            print(arr)
        elif b in arr:
            idx = arr.index(b)
            if len(arr) - 1 != idx:
                # print(arr,idx)
                # print(arr[:idx - 1],[a],arr[idx-1:])
                if idx - 1 > 0:
                    # print(f'{idx} - 1 > 0')
                    arr = arr[:idx-1] + [a] + arr[idx-1:]
                else:
                    # print("index n")
                    # print([a] + arr[:])
                    arr = [a] + arr[:]
            else:
                arr.append(a)
            # print(arr)

        if a not in arr and b not in arr:
            arr.append(a)
            arr.append(b)
            # print(arr)
    print(arr)
if __name__ == '__main__':
    findWord(["P>E", "E>R", "R>U"])
    findWord(["I>N", "A>I", "P>A", "S>P"])