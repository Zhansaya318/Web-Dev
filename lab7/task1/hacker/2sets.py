for i in range(int(input())):
    a_size = input()
    A = set(input().split())
    b_size = input()
    B = set(input().split())
    print(A.issubset(B))