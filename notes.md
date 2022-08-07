# Improvement process and steps

-------------------------------------------------------
## Part 1
### Step 1: Quick refresher on IQM 
After a quick refresher I spent some time thinking about the challenges of incrementally calculating the IQM and what 
testing might look like.

### Step 2: Read and step through the code
Playing with and stepping through the code with a debugger helps build interest and gets my mind in the game. :-)  I 
spent a little time thinking about the big picture and looking for any obvious issues early on. Then I set that aside.

### Step 3: Refactoring & Improvements
My first improvement was to add a test.

To do this I needed to wrap the code in a function, parameterize the data file, export the function to a unit test, and 
create some test data.

Since the original code doesn't return anything, I made the assumption that the function's only output is stdout which
might be getting piped to another program. I wanted to keep with programming to the interface: standard out.

My second improvement was adding a linter to keep things clean.

## Part 2
For step 1, I first want to get a baseline established and added to a test case, mostly
for documenting the results and running the script with a smaller data set.

The systems time command returned: (Includes module and file loading)
```commandline
real    2m7.046s
user    2m6.203s
sys     0m0.511s
```

Since I already had a small test case to check that the output is the same
I decided to start grabbing some low-hanging fruit. The `data.sort()` was getting called 
for every iteration which will get quite expensive as the data set grows. It would be best to insert the value 
in place and maintain the sorting order.

This saved about 42ms (a 24% decrease in execution time) processing the large `data.txt` file.

Usually reduce functions are clean but slow. Updating the `reduce` to a `sum` took the
execution time from 2 minutes and 54 seconds down to 45 seconds. Sum is a bit easier to read as well.

The overall execution time reduced by 129 seconds (a 74% decrease).

The system execution time is now 37 seconds:
```commandline
real    0m37.074s
user    0m36.655s
sys     0m0.348s
```

For any further gains in performance we'll need to manage the state better and probably move the function to a class. 
This will ease testing as well but we'll save that for the next section.

For step 2 & 3, normally I like my tests to run fast, so I avoid testing with large data sets (unless checking 
performance). So, I'm going to:
1. Move the function to class, add some properties methods.
2. Update/fix the test cases and main script.
3. Write a test case that checks the processing of `data.txt` by creating an `expectation.csv` file.

For step 4, I'll create some tests to check larger values and sets with 0 - 3 items.

My last improvement was adding a README.md and requirements.txt.

Note: Normally, I would use smaller data sets to encourage running tests often.

## Questions:
### Explain how your optimization works and why you took this approach

### Would your approach continue to work if there were millions or billions of input values?
A million, yes; a billion No. The array is stored in memory and eventually the sum() function would run out of memory as
well.

### Would your approach still be efficient if you needed to store the intermediate state between each IQM calculation in a data store? If not, how would you change it to meet this requirement?
