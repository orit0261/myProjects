#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
import collections


class solution(object):

    def longestCommonPrefix(self,a):

            size = len(a)

            # if size is 0, return empty string
            if (size == 0):
                return ""

            if (size == 1):
                return a[0]

            # sort the array of strings
            a.sort()

            # find the minimum length from
            # first and last string
            end = min(len(a[0]), len(a[size - 1]))

            # find the common prefix between
            # the first and last string
            i = 0
            while (i < end and
                   a[0][i] == a[size - 1][i]):
                i += 1

            pre = a[0][0: i]
            return pre


print(solution().longestCommonPrefix( ["flower","flow","flight"]))
print(solution().longestCommonPrefix( ["falowering","fblowe","fclights"]))
print(solution().longestCommonPrefix( ["dog", "racecar", "car"]))

