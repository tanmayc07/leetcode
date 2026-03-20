class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        ans = [0]*len(prices)

        for i in range(len(prices)):
            while st and prices[st[-1]] >= prices[i]:
                idx = st.pop()
                ans[idx] = prices[idx] - prices[i]
            st.append(i)

        while st:
            idx = st.pop()
            ans[idx] = prices[idx]

        return ans