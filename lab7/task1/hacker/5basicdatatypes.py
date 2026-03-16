if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for i in range(N):
        command = input().split()
        action = command[0]
        
        if action == 'insert':
            arr.insert(int(command[1]), int(command[2]))
        elif action == 'print':
            print(arr)
        elif action == 'remove':
            arr.remove(int(command[1]))
        elif action == 'append':
            arr.append(int(command[1]))
        elif action == 'sort':
            arr.sort()
        elif action == 'pop':
            arr.pop()
        elif action == 'reverse':
            arr.reverse()