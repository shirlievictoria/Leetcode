from typing import List

class Solution:
    def twoSum_BruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []
    
    def twoSum_TwoPassHashTable(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []

    def twoSum_OnePassHashTable(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

def main():
    # Crear una instancia de Solution
    solution = Solution()

    # Primer caso de prueba
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum_TwoPassHashTable(nums, target)
    print(f"Input: nums = {nums}, target = {target}, Output: {result}")

    # Segundo caso de prueba
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum_TwoPassHashTable(nums, target)
    print(f"Input: nums = {nums}, target = {target}, Output: {result}")

    # Tercer caso de prueba
    nums = [1, 2, 3]
    target = 7
    result = solution.twoSum_TwoPassHashTable(nums, target)
    print(f"Input: nums = {nums}, target = {target}, Output: {result}")

    for i in range(len(nums)):
      print(i)
      
# Ejecutar main solo si este archivo es el principal
if __name__ == "__main__":
    main()
