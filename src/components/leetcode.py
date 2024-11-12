intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key= lambda p : p[0])
print(intervals)
print('--------------------------------------------')
ans = []

for p in intervals:
    print(p)
print('--------------------------------------------')
nums = [1,2,3,4,5,6]
def reverse(i, j):
    while i < j:
        nums[i], nums[j] = nums[j],nums[i]
        i += 1
        j -= 1
reverse(0,5)
print(nums)
# 3.无重复字符的最长子串
s = "abcabcbb"
for right,c in enumerate(s):
    print(right,c)



