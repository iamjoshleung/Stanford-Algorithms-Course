def count_split_inversion(B, C, n):
    len_B = len(B)
    len_C = len(C)
    i = 0 # pointer to B
    j = 0 # pointer to C
    D = []
    z = 0 # number of inversions

    # print("B in split: {}".format(B))
    # print("C in split: {}".format(C))

    for k in range(n):
        if i < len_B and j < len_C:
            if B[i] > C[j]:
                D.append(C[j])
                j += 1
                z += len_B - i
            else:
                D.append(B[i])
                i += 1
        else:
            if i < len_B:
                D.append(B[i])
                i += 1
            if j < len_C:
                D.append(C[j])
                j += 1
    return (D, z)


def count_sort_inversion(A, n):
    if n == 1:
        return (A, 0)
    else:
        mid = n / 2
        A_left = A[:mid]
        A_right = A[mid:]
        # print("A_left: {}".format(A_left))
        # print("length of A_left: {}".format(len(A_left)))
        # print("A_right: {}".format(A_right))
        # print("length of A_right: {}".format(len(A_right)))
        (B, x) = count_sort_inversion(A_left, len(A_left))
        (C, y) = count_sort_inversion(A_right, len(A_right))
        (D, z) = count_split_inversion(B, C, n)

        return (D, x + y + z)



def main():
    A = []
    # read file
    text_file = open('TextData_2.txt', 'r')
    for line in text_file:
        A.append(int(line))
    n = len(A)
    print("length of A: {}".format(n))
    print("# of inversions: {}".format(count_sort_inversion(A, n)))

if __name__ == "__main__":
    main()
