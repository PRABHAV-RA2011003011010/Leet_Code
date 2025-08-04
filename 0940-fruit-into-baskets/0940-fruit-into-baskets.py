class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)
        i = 0
        max_len = 0
        
        for j in range(len(fruits)):
            fruit_count[fruits[j]] += 1

            # If we have more than 2 types, shrink window from the left
            while len(fruit_count) > 2:
                fruit_count[fruits[i]] -= 1
                if fruit_count[fruits[i]] == 0:
                    del fruit_count[fruits[i]]
                i += 1
            
            max_len = max(max_len, j - i + 1)

        return max_len