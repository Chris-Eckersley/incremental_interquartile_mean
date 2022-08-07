#Improvement process and steps

-------------------------------------------------------
## Part 1
### Step 1: Quick refresher on IQM 
After a quick refresher I spent some time thinking about the challenges of incrementally calculating the IQM and what 
testing might look like.

### Step 2: Read and step through the code
Playing with and stepping through the code with a debugger helps build interest and gets my mind in the game. :-)  I 
spend a little time thinking about the big picture and looking for any obvious issues early on. Then that gets sent off
to my subconscious. :-)

### Step 3: Refactoring & Improvements
My first improvement was to add a test.

To do this I needed to wrap the code in a function, parameterize the data file, export the function to a unit test, and 
create some test data.

Since the original code doesn't return anything, I made the assumption that the function's only output is stdout which
might be getting piped to another program.

Secondly, and before any refactoring was commited, I added a linter to keep things clean.

## Part 2
I first want to get a baseline established and added to a test case. Mostly
for documenting the results.

The systems time command returned: (Includes module and file loading)
```commandline
real    2m7.046s
user    2m6.203s
sys     0m0.511s
```

Next I decided to grab some low-hanging fruit. I immediately saw the the `data.sort()` was getting called
every time. For this mush data it's best to insert in an ordered place.

This saved about 42ms (a 24% decrease in execution time) processing the large `data.txt` file.
I imagine the percent decrease in increase with larger data sets.

Usually reduce functions are clean but slow. 

