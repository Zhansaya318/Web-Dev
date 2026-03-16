x = input()
nums = input().split()
print(all(int(x) > 0 for x in nums) and any(x == x[::-1] for x in nums))