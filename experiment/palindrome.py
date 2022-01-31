def is_palindrome(a):
    return True if a == a[::-1] else False


def CountPS(str, n):
    # creat empty 2-D matrix that counts
    # all palindrome substring. dp[i][j]
    # stores counts of palindromic
    # substrings in st[i..j]
    dp = [[0 for x in range(n)]
          for y in range(n)]

    # P[i][j] = true if substring str[i..j]
    # is palindrome, else false
    P = [[False for x in range(n)]
         for y in range(n)]

    # palindrome of single length
    for i in range(n):
        P[i][i] = True

    # palindrome of length 2
    for i in range(n - 1):
        if (str[i] == str[i + 1]):
            P[i][i + 1] = True
            dp[i][i + 1] = 1

    # Palindromes of length more than 2. This
    # loop is similar to Matrix Chain Multiplication.
    # We start with a gap of length 2 and fill DP
    # table in a way that the gap between starting and
    # ending indexes increase one by one by
    # outer loop.
    for gap in range(2, n):

        # Pick a starting point for the current gap
        for i in range(n - gap):

            # Set ending point
            j = gap + i

            # If current string is palindrome
            if (str[i] == str[j] and P[i + 1][j - 1]):
                P[i][j] = True

            # Add current palindrome substring ( + 1)
            # and rest palindrome substring (dp[i][j-1] +
            # dp[i+1][j]) remove common palindrome
            # substrings (- dp[i+1][j-1])
            if (P[i][j] == True):
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] + 1 - dp[i + 1][j - 1])
            else:
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] - dp[i + 1][j - 1])

    # return total palindromic substrings
    return dp[0][n - 1]


# Driver Code
if __name__ == "__main__":
    str = "aabbcbbaa"
    n = len(str)
    print(CountPS(str, n))







exit()


def palindrome_substring(a):
    # 1. scan through a by index
    # 2. divide to left and right
    # 3. find possible string set from left side
    # 4. check all (3) in_string with the right

    found_palindrome = []
    for i,n in enumerate(a):
        left = a[:i]
        right = a[i:]
        # print(f"{i} {left} {right} | {len(left)} : {len(right)}")
        for ii,nn in enumerate(left):
            checkleft = left[ii:]
            checkright = right[:(len(checkleft))]
            checkright_nomiddle = right[1:(len(checkleft)+1)]
            print(checkleft,checkright)
            print(f"NoMiddle {checkleft} : {checkright_nomiddle}")

            if checkleft == checkright :
                found_palindrome.append(f"{checkleft}:{checkright}")
            if checkleft == checkright_nomiddle:
                found_palindrome.append(f"{checkleft}:{checkright_nomiddle}")






            # print("nomiddle",checkleft,checkright_nomiddle)
            # print(check)
            # if check in right:
            #     return True
    return found_palindrome
        # print(i,left,right)

# aabbaacdef

# print(palindrome_substring("iammadaamsme"))
# print(palindrome_substring("123456789"))
# print(is_palindrome("madam"))

# print(palindrome_substring("34577"))