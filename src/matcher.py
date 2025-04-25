def isMatch(s: str, p: str) -> bool:
    # Create a dictionary to remember results of checks for pairs of indices (i, j)
    memo = {}

    # Define a function to check if the string matches the pattern
    def backtrack(i: int, j: int) -> bool:
        # If we already checked these indices, just return the stored result
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If we reach the end of the pattern, check if we also reached the end of the string
        if j == len(p):
            # If both are at the end, it's a match; otherwise, it's not
            memo[(i, j)] = (i == len(s))
            return memo[(i, j)]
        
        # Check if the current characters match or if the pattern has a dot '.'
        current_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
        
        # Check if the next char in pattern is '*'
        if j + 1 < len(p) and p[j + 1] == '*':
            # We can skip this character and the '*' (no occurrence)
            # or we can use the current character and keep '*'
            # (this means one or more occurrences of the current character)
            memo[(i, j)] = backtrack(i, j + 2) or (current_match and backtrack(i + 1, j))
            return memo[(i, j)]
        
        # If there’s no '*', we just proceed normally
        if current_match:
            # Move to the next character in both the string and the pattern
            memo[(i, j)] = backtrack(i + 1, j + 1)
            return memo[(i, j)]
        
        # If there’s no match, set the result to False
        memo[(i, j)] = False
        return memo[(i, j)]
    
    # Start checking from the beginning of both the string and the pattern
    return backtrack(0, 0)
