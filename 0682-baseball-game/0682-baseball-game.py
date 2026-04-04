class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        res = 0

        for i in range(len(operations)):
            if operations[i]=="C":
                st.pop()
            elif operations[i]=="D":
                a = st[-1]*2
                st.append(a)
            elif operations[i]=="+":
                if len(st)>=2:
                    a = st.pop()
                    b = st.pop()
                    st.append(b)
                    st.append(a)
                    st.append(a+b)
            else:
                st.append(int(operations[i]))
        
        for i in range(len(st)): res+=st[i]

        return res