# Advent of Code 2024

These are my attempts to solve the daily problems at https://adventofcode.com/. Feel free to follow along, use my code, tell me I'm doing it wrong, whatever. If you're a beginner and want to try it yourself or follow along, you can keep reading for some basic set up instructions and unsolicited advice. If you know what you're doing already, you'll probably finish more problems than I will and also don't need the rest of the readme.

## Initial Setup

I'm using Python 3.13 to solve these problems. Everything really ought to use the standard library, so there's nothing in requirements.txt. You might decide you want some additional libraries in the future, so you may as well work in a virtual environment. Do that with:

```
python3.13 -m venv env
```

And to activate it:

```
source env/bin/activate
```

To deactivate when you're done or moving on to something else:

```
deactivate
```

## Daily helper script

Each daily problem follows a similar format. There are two parts, the second revealed after you solve the first, but they use the same input data. There's usually a small sample provided to you as well so that you can work through an initial solution and test that you're on the right track. Each day, there's some repetitve work to create a new code file, read in the input and sample, etc. So I created (or, rather, had Claude create) a bash script to set up each day. You can use it as follows:

```
chmod +x setup.sh #make the script executable if needed
./setup.sh <day>
```

Such as:
```
./setup.sh 1
```

Which will create:
```
day1/day1.py
day1/input1.txt
day1/notes1.md
day1/sample1.txt
```
The script will also insert some basic boilerplate into the `.py` file since every problem requires you to read in the input data and solve the two parts. However, you may want to modify this to handle the inputs based on the format and problem of the day. You can see an example in my `day1/` solution versus the setup script boilerplate.

You can optionally grab your session token once you're logged into Advent of Code, store it, and let the script grab the daily input data as well. This part is optional and the script will skip this step if a token isn't present.

```
# Create the directory if it doesn't exist
mkdir -p ~/.config

# Create the session file (replace with your actual session cookie)
echo "your_session_cookie_here" > ~/.config/aoc_session

# Restrict permissions (recommended for sensitive files)
chmod 600 ~/.config/aoc_session

# It's not a good idea to check secrets into github, so -
# In your project's .gitignore, add:
echo ".config/aoc_session" >> .gitignore
```


## Should I use AI?

Try not to. At least, if you're a beginner and you're learning the basic concepts and syntax and such, try to stick to asking very specific questions about the component you're implementing, rather than feeding the LLM the question prompt itself. For example:

- Good: "How do I loop over the elements of a list and do something with each of them?"
- Not Good: "How do I merge two lists together into pairs of elements and sum the total difference between each pair?"

This way, you're still thinking through your own program flow, data structures, and algorithms, and deciding how you generally want to approach the problem. At most, the LLM is giving you some language help. But if you're not a beginner, I suggest not using any AI tools at all. Google for syntax, but try and solve the problem entirely by yourself.

None of my solutions checked in here will have any AI generated code. I'd suggest in advance that you not use Cursor (or a similar LLM-integrated IDE), and/or disable Copilot before starting. The code completion will often give you the solution, which I presume you don't want.

## I'm stuck and really want a hint!

The Advent of Code subreddit is often helpful: https://old.reddit.com/r/adventofcode/ - just be careful if you don't want to see a full solution. You can also use this repo, although if there's no solution here, I'm probably stuck too. I usually write down a few notes after I've finished the problem, and you can read those in the `notes.md` file for that given day. It may contain some very specific information and I can't promise it won't point you directly at a solution, so try to hold off on outside resources unless you're truly stuck.
