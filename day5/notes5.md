I got a bit lucky with this one, in that I abandoned a solution in part 2 not because it didn't work but because I decided to try something easier.

# Part 1

Pretty straight-forward. Iterate through the rules, check if the list contains both numbers, and if so, that the first comes before the second. If not, that list is invalid. All lists had odd numbers of elements, so the midpoint didn't have any tricks to it.

# Part 2

I spent a little bit of time trying to sort the list of rules in a way that would let me fix each invalid list in one pass. At some point I got sick of trying to do that and just tried the brute force method - keep iterating over the lists, swapping the out of order elements each time a rule check fails, and after a full pass, if it's valid pop it to another list. If it's not, keep it in the invalid list, and just
keep looping until there's nothing left in invalid. That worked just fine and took 5 minutes to write, versus the time I was spending trying to get the single pass solution working.