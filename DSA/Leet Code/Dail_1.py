class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        def dfs(digit, remain_even, remain_odd, remain):

            # base; found a solution
            if remain_even == 0 and remain_odd == 0 and remain == 0:
                return 1

            # base; not possible
            if digit > 9 or remain_odd < 0 or remain_odd < 0 or remain < 0:
                return 0

            # seen before
            if (digit, remain_even, remain_odd, remain) in memo:
                return memo[(digit, remain_even, remain_odd, remain)]

            # otherwise; compute memo[(digit, odd, even, remain)]

            # possible senarios to allocate digit into slot
            freq = counter[digit]

            res = 0
            for f in range(freq + 1):
                # find new_odd & new_even
                new_even = f
                new_odd = freq - f

                # stop; not possible
                if new_even > remain_even or new_odd > remain_odd:
                    continue

                # create the possible combinations
                comb_even = comb(remain_even, new_even)
                comb_odd = comb(remain_odd, new_odd)

                # recur to the next digit
                new_remain = remain - digit * new_even
                new_remain_even = remain_even - new_even
                new_remain_odd = remain_odd - new_odd
                temp = dfs(digit + 1, new_remain_even, new_remain_odd, new_remain)

                # update res based on recurred solution
                res += comb_odd * comb_even * temp
                res = res % kMod

            # update
            memo[(digit, remain_even, remain_odd, remain)] = res

            return memo[(digit, remain_even, remain_odd, remain)]

        kMod = 10 ** 9 + 7
        n = len(num)

        counter = Counter(int(ch) for ch in num)  # stores {digit: freq}
        summ = sum(int(ch) for ch in num)  # total sum of num

        # base; not possible
        if summ % 2 != 0:
            return 0

        # define the target for each side
        target = summ // 2

        # define even & odd indices
        even_count = n // 2
        odd_count = n - even_count

        # memo[(digit, remain_even, remain_odd, remain_target)] := count number of solution for digit value with remain_even, remain_odd and remain_target
        memo = dict()

        return dfs(0, even_count, odd_count, target)