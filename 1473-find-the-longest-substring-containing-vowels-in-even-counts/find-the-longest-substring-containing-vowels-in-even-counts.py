class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
         # Mapping vowels to bitmask positions
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Initialize the bitmask and the hashmap
        bitmask = 0
        first_occurrence = {0: -1}  # bitmask 0 is first seen at index -1
        max_len = 0
        
        for i, char in enumerate(s):
            # Update bitmask if character is a vowel
            if char in vowel_to_bit:
                bitmask ^= (1 << vowel_to_bit[char])
            
            # Check if the bitmask has been seen before
            if bitmask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[bitmask])
            else:
                # Store the first occurrence of this bitmask
                first_occurrence[bitmask] = i
    
        return max_len