nums = [1,1,2]
List = set()
k = 0

n = len(nums)
for i in range(n):
    if i not in List:
        List.add(nums[i])

k = len(List)

num = List
print(k, num)