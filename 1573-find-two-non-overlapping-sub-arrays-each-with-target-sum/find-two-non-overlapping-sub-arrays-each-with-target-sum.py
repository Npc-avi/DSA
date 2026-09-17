class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        curr_sum = 0
        
        # Maps prefix_sum -> its ending index
        seen = {0: -1}
        
        # best_left[i] stores the minimum length of a valid sub-array found in arr[0...i]
        best_left = [float('inf')] * n
        
        min_sofar = float('inf')
        ans = float('inf')
        
        for i in range(n):
            curr_sum += arr[i]
            
            # Check if a sub-array summing up to target ends at index i
            if curr_sum - target in seen:
                start = seen[curr_sum - target]
                length = i - start
                
                # If there's a valid non-overlapping left sub-array, update the global answer
                if start >= 0 and best_left[start] != float('inf'):
                    ans = min(ans, length + best_left[start])
                
                # Update the smallest single sub-array found so far
                min_sofar = min(min_sofar, length)
            
            best_left[i] = min_sofar
            seen[curr_sum] = i
            
        return ans if ans != float('inf') else -1
