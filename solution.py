def minEatingSpeed(piles, h):
    # Initialize binary search boundaries
    left, right = 1, max(piles)
    
    while left <= right:  # Changed to <= to ensure we find the exact value
        k = (left + right) // 2
        # Calculate total hours needed using ceiling division
        total_hours = sum((pile + k - 1) // k for pile in piles)
        
        if total_hours <= h:
            # This speed works, but we might find a smaller one
            right = k - 1
        else:
            # Speed is too slow, need to try faster
            left = k + 1
    
    return left  # Return the minimum valid eating speed
