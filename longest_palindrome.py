def longest_palindrome(st, i, j):
    if(i == j):
        return 1
    elif(i > j):
        return 0
    else:
        if st[i] == st[j]:
            return 2 + longest_palindrome(st, i + 1, j - 1)
        else:
            return max(longest_palindrome(st, i + 1, j), longest_palindrome(st, i, j - 1))
if __name__ == '__main__':
    st = input()
    print(longest_palindrome(st, 0, len(st) - 1))
