class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowels=defaultdict(int)
        consonants=defaultdict(int)
        for char in s:
            if char in "aeiou":
                vowels[char]+=1
            else:
                consonants[char]+=1
        
        max_vowel = max(vowels.values()) if vowels else 0
        max_consonant = max(consonants.values()) if consonants else 0

        return max_vowel + max_consonant

        