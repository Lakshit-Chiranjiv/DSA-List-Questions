class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sm_str_sz = len(strs[0])
        sm_str = strs[0]
        for i in strs[1:]:
            if len(i) < sm_str_sz:
                sm_str_sz = len(i)
                sm_str = i
        
        i = 0
        while i < len(strs):
            print(strs[i][0:sm_str_sz],"-",sm_str,"-",i)
            if strs[i][0:sm_str_sz] == sm_str:
                i += 1
            else:
                sm_str_sz -= 1
                if sm_str_sz < 0:
                    return ""
                sm_str = sm_str[0:sm_str_sz]
                i = -1
        
        return sm_str