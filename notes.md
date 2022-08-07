#Improvement process and steps

-------------------------------------------------------

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
