I never want to see this problem again.

# Part 1

I ran into some list mutability issues (or, alternatively, I'm dumb and dont understand lists as well as I think I do). The biggest thing that I ran into was that I was using the list simulation method just like the example problem shows you. Yep, file ids > 9 would take up more than one space - a problem it took me nearly forever to figure out. One other minor issue with the list overscanning, added some bounds checking.

# Part 2

I did problems 10 and 11 before I was able to do Day 9 Part 2. I really thought this would be an easy one, since I'd learned a lot of the lessons in part 1. It was obvious you couldn't do this with list simulation. But I figured a real filesystem probably keeps track of locations and lengths - and they might, but I know nothing about filesystems. Still that turned out to be the right approach, and I even implemented it correctly very fast. The sample data was passing and everything. With the real input data, I was getting the wrong answer, and I figured it was because I wasn't handling free space correctly. I wrote a whole thing to recursively scan and combine free space into contiguous blocks. That was completely unnecessary, and 2 days later, I figured out that I wasn't checking to see if a file was already to the left of the next available open space. Whoops.

