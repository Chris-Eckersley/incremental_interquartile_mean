#Improvement process and steps

-------------------------------------------------------

### Step 1: Quick refresher on IQM 
After a quick refresher I spent some time thinking about the challenges of incramentally calculating the IQM and what 
testing might look like.

### Step 2: Read and step through the code
Playing with and stepping through the code with a debugger helps build interest and gets my mind in the game. :-)  I 
spend a little time thinking about the big picture and looking for any obvious issues early on. Then that gets sent off
to my subconscious. :-)

### Step 3: Refactoring
My first improvements were to wrap the code in a function and parameterizing the file so that I can export the function
and create some unit tests.

Since the original code doesn't return anything, I made the assumption that the function's only output is stdout 
which is getting piped to another program.

As the standard out as my interface, I started by writing a test with a smaller data set that would run a bit more quickly.

Before I committed my tests and first refactor I wanted to add a linter to keep things clean.
