def permuteOut(e):
    for i in e:
        print(i)

def permute(elements_sorted):
    n = len(elements_sorted) - 1
    finished = False
    counter = 0

    while not finished:
        permuteOut(elements_sorted)
        counter += 1
        j = n-1


        while elements_sorted[j] >= elements_sorted[j+1]:
            j -= 1

            if(j < 0):
                finished = True
                break

        if (finished):
            break

        l = n
        while elements_sorted[j] >= elements_sorted[l]:
            l -= 1


        tmp = elements_sorted[j]
        elements_sorted[j] = elements_sorted[l]
        elements_sorted[l] = tmp

        k = j + 1
        l = n
        while k < l:

            tmp = elements_sorted[k]
            elements_sorted[k] = elements_sorted[l]
            elements_sorted[l] = tmp
            k += 1
            l -= 1

    print("permutations: " + str(counter))

e1 = ["A", "A", "A", "B", "C", "C", "C", "C", "D", "D"]

permute(e1)




