def main():
    a = [0 for x in range(21)]
    a[0] = 1
    for n in range(2, 21):
        print("array for N = " + str(n))
        for i in range(n, 0, -1):
            a[i] += a[i-1]
            print("\n a[" + str(i) + "] ==" + str(a[i]))
        print("\n a[" + str(0) + "] ==" + str(a[0]))


main()
