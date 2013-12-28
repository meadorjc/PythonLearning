#caleb meador meadorjc at gmail.com
def reverse(s):
	s_reversed = ''
	for ch in s:
		s_reversed = ch+s_reversed
	return s_reversed

def is_palindrome_v1(s):
	s_reversed = reverse(s)
	return s == s_reversed

racecar = 'racecar'
superc = 'supercalifragilisticexpialidocious'

print(reverse(racecar))
print(reverse(superc))

print(is_palindrome_v1(racecar))
print(is_palindrome_v1(superc))


def is_palindrome_v2(s):

    # num of chars in s
    n = len(s)
    print("len", n)
    print('n/2 = ', n/2)
    print ("s 0:",n, s[0:n // 2]) #(0: 7/2)
    print('s ',n,'-',n, s[n-n // 2:n]) #(7-(7/2)):7 => 5:7
    
    #compare 1st half of s to reverse of second half
    #omit the middle char of an odd-length string
    #: is range (0:n)
    return s[0:n // 2] == reverse(s[n-n // 2:])

print("v2")
print(is_palindrome_v2(racecar))
print(is_palindrome_v2(superc))


def is_palindrome_v3(s):

    #s[i] and s[j] are the next pair of chars to compare
    i = 0
    j = len(s) - 1

    #the characters in s[:i] have been successfully compared to those in s[j:].
    while i < j and s[i] == s[j]:
        i = i+1
        j = j-1
    #if we exited because we successfully compared all pairs of chars,
    # then j <= i
    return j <= i


print("v3")
print(is_palindrome_v3(racecar))
print(is_palindrome_v3(superc))


