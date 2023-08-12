class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # monotonic decreasing stack problem but with possibilities of same values in a stack

        stack = []  #pair [temp,index]
        res = [0] * len(temperatures)

        for i, T in enumerate(temperatures):

            while stack and stack[-1][0] < T:
                stackT,stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([T,i])

        return res

#         The total number of times an element can be pushed onto the stack is n (the length of the temperatures list), and the total number of times an element can be popped from the stack is also n.

# The key here is that the number of push and pop operations combined does not exceed n. This is why the algorithm's time complexity remains O(n).

# The presence of the while loop doesn't necessarily imply that the complexity becomes quadratic. The critical factor is that each element in the temperatures list is pushed and popped at most once, and the overall number of these operations is proportional to the input size n.
#  Space - O(n) and Time - O(n)
        