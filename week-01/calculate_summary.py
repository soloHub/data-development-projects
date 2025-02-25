# Author: Solomon Kareem
# Write a Python function calculate_summary that takes a list of numbers 
# returns a dictionary containing the mean and median of the list. 
# If the input list is empty, return None.


def calculate_summary(nums):
    # return None for empty list
    if (len(nums) == 0):
        return None
    
    stat = {} # dictionary for summary

    # Mean process
    stat["mean"] = sum(nums) / len(nums)

    # Median process
    n = len(nums) // 2 # middle index of list
    nums.sort() # sort list

    if (len(nums) % 2 == 0):
        stat["median"] = (nums[n] + nums[n-1]) / 2 # for two items at the middle
    else :
        stat["median"] = nums[n] # for one item at the middle
    
    return stat


# Sample Input 1:
numbers_1 = [5, 2, 7, 1, 3]
print(calculate_summary(numbers_1))

# Sample Input 2:
numbers_2 = [4, 1, 3, 2]
print(calculate_summary(numbers_2))