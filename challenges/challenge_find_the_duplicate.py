from challenges.challenge_anagrams import merge_sort


def find_duplicate(nums):
    try:
        merge_sort(nums)
        for index, num in enumerate(nums[:-1]):
            if nums[index] == nums[index + 1]:
                return num
    except TypeError:
        return False
    return False
