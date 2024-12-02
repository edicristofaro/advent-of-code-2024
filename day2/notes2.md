# Part 1

Pretty straight-forward. Made sense to create 3 boolean functions and check whether each report fit the safe conditions.

# Part 2

Brute force method works. Was easier to split safe and unsafe on the original conditions first, then re-check the unsafes by iterating through each report, removing each index sequentially, and re-testing.

This doesn't work correctly unless you make a copy of the list that you're going to delete from. That's because python assignment just assigns the reference to the original list, so deleting from the assigned variable is actually deleting from the original. You need a shallow copy instead.