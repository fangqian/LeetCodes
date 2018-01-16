class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if d.get(find, None) is None:
                d[nums[i]] = i
            else:
                return [d[find], i]


class Solution1:
    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):
        tmp = {}
        for i in range(len(num)):
            if target - num[i] in tmp:
                return([tmp[target - num[i]], i])
            else:
                tmp[num[i]] = i


nums = [2, 5, 2, 11, 15]
target = 4
a = Solution()
print(a.twoSum(nums, target))

b = Solution1()
print(b.twoSum(nums, target))
