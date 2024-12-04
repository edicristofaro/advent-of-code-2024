Some known good points in the sample file:

```
    print(f"{check_up_down(input_data, "XMAS", 6, 4)=}")
    print(f"{check_left_right(input_data, "XMAS", 5, 9)=}")
    print(f"{check_diagonal(input_data, "XMAS", 0, 5)=}")
```

I did _way_ too much work dealing with list bounds checking. I knew better. When I started, I thought about taking the list of lists grid and turning it into a coordinates dict. e.g. `input_data[y][x] -> grid[(x,y)] = input_data[y][x]`

I got lazy and decided I didn't feel like transforming the list, even though it'd have taken a minute. I spent an hour longer than I should have bounds-checking my grid scans as a result and dealing with edge cases arising from that. Literal edge cases, like negative list indices, or bugs in how I was dealing with bounds. I also have some hacky looking code where I deal with out of bounds indices with a try and empty except to silently fail and continue. That's dumb. I would have been way better off doing something like `val = grid.get((x,y), None)` and then being able to check `if val: ...` and abort easily if I'm over an edge.

Anyhow, deal with coordinates like coordinates. Use a dict where the keys are your point coordinates and the values are your point values. 

That aside -

Part 1. I decided to scan each point and look up, down, left, right, and diagonal in all 4 directions. This guaranteed I wouldn't double-count. I'm sure  I could have compacted the code a bit since there's a ton of repetition, but it was easy to reason about and worked well. The biggest issues I had were related to not using the correct data structure and instead doing a bad job of bounds-checking lists.

Part 2. At first I really wanted to use my diagonal checker from Part 1, so I augmented it to also return the endpoints of each line that it was counting as a diagonal match for the word (MAS in this case). Then I flattened that list and counted the common midpoints. Not a great idea. Rather than debug why it was excessively double-counting, I decided to scan the grid point by point, offset by 1 at each edge, since I was using that point as a midpoint and looking diagonal in opposite directions for MAS or SAM. This worked well again, once I dealt with a few more bugs because I used the wrong data structure.

There might be a better way than using dict(point) -> value, but it definitely isn't list[list[]].