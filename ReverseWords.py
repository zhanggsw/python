'''
@author: zhanggong
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        words_alt = reversed(words)
        result=""
        for w in words_alt:
            result = result + str(w) + " "
        return result.strip()

if __name__ == '__main__':
    s = Solution()
    r = s.reverseWords("   this is a a  test ")
    print r
    