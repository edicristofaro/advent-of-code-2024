Part 1 came pretty quickly. I couldn't remember how to generate all combinations of a list, had to google that. But otherwise just substitution.

Part 2 was frustrating because I was stupid about it. I kept trying to apply the || operator to combine the two adjacent numbers in the original list, basically like a string substitution for a null. Took me a while to figure out that since we were evaluating the equations from left to right, I needed to combine the current subtotal with the next number. At that point, the code doesn't look much different than part 1.'

I do wonder if it's possible to do something other than brute force. Generating every possible combination and testing it was pretty slow with the much longer input data.