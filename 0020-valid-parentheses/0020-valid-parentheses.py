class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if len(st) > 0:
                if i == ')' and st[len(st)-1] == '(':
                    st = st[0:len(st)-1]
                elif i == '}' and st[len(st)-1] == '{':
                    st = st[0:len(st)-1]
                elif i == ']' and st[len(st)-1] == '[':
                    st = st[0:len(st)-1]
                else:
                    st.append(i)
            else:
                st.append(i)
        return len(st) == 0