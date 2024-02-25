def max_rect(nums: list[int], height: int):
    i = j = height
    while i >= height:
        i -= 1
    while j >= height:
        j -= 1
    print((j-i+1)*height)


nums: list[int] = [2, 1, 5, 6, 2, 3]

for i in nums:
    max_rect(nums, i)
