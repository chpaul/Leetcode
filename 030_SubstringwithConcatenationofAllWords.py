class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0 : return []
        ansIdx = []
        wordIdx = dict(map(lambda x:(x,words.count(x)),words))
        wordLen = len(words[0])
        for i in range(wordLen):
            left = i
            subDict = dict()
            counter = 0
            for j in range(i, len(s)- wordLen+1, wordLen):
                subStr = s[j:j+wordLen]
                if subStr in words:
                    if subStr in subDict: subDict[subStr] +=1
                    else:subDict[subStr] =1
                    counter+=1
                    while subDict[subStr] > wordIdx[subStr]:
                        subDict[s[left:left+wordLen]]-=1
                        counter-=1
                        left+=wordLen
                    if counter == len(words):
                        ansIdx.append(left)
                else: subDict,left,counter = dict(), j+wordLen, 0;
        return ansIdx


if __name__ == "__main__":
    solution = Solution()
    a = solution.findSubstring('barfoofoobarthefoobarman', ["bar","foo","the"])    # 6 9 12
    a = solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
    print(a)