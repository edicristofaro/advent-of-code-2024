Regex approach worked. Part 2 was trickier than it should have been. Two problems:

1. I learned about greedy and non-greedy regex matching.

```
muls = re.findall(r"^|do\(\)(.*)don't\(\)", input_data)
```
This was matching my entire string. As it turns out, the (.*) group there is greedy by default, meaning it will match as many characters matching the pattern as possible. This means it will match until the last `don't()`.

```
re.findall(r"^|do\(\)(.*?)don't\(\)", input_data)
```

The `?` makes the `.*` non-greedy.



2. I was reading the file incorrectly

It took me a bit to notice that the file wasn't one long string, but multiple lines, and I was handling that incorrectly. I was reading the file in like this:

```
with open("input3.txt", "r") as f:
        input_data = f.read().strip()
```

f.read() reads in the entire file, as expected. but strip() was removing spaces, not newlines. So I was getting the wrong answer constantly. Probably spent an hour trying to figure this out. Once I realized I was stripping the wrong characters, I was able to fix it with:

```
with open("input3.txt", "r") as f:
        input_data = f.read().replace("\n", "")
```

This removes newlines, and now we're getting the correct answer. This probably means that some `do()` and `don't()` instances had spaces in them that I was stripping out, causing me to recognize those tokens instead of ignoring them.