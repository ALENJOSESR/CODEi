class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        
        # Append the remaining characters from word1 or word2
        if i < len(word1):
            merged.append(word1[i:])
        if j < len(word2):
            merged.append(word2[j:])
        
        return ''.join(merged)

# Example usage
# word1 = "abc"
# word2 = "pqr"
# print(mergeAlternately(word1, word2))  # Output: "apbqcr"

# word1 = "ab"
# word2 = "pqrs"
# print(mergeAlternately(word1, word2))  # Output: "apbqrs"

# word1 = "abcd"
# word2 = "pq"
# print(mergeAlternately(word1, word2))  # Output: "apbqcd"