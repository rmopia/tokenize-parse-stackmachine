# Tokenizing & Parsing Stack Machine

## Synopsis
The purpose of this project is to familiarize the programmer with the python language 
and virtual machines by creating a tokenizer and parser function alongside a stack
machine class.

## Tokenizing & Parsing
Here we begin by creating a file called "tokenize_parse.py". This file will hold a tokenizer function
and a parsing function. The tokenizer takes in a string input and follows all the same rules
we used that will be discussed in the next portion. This means the only valid strings are:
> push, pop, add, sub, mul, div, mod, skip, save, get

Otherwise the only other valid input must be a number. Anything else should raise a ValueError
with the following message:

                Unexpected Token: <token>
The function should then return a list of the tokenized contents only if they are deemed valid.
The parse function will then take the returned list and validate it by returning a boolean (True/False).
The tokens are deemed valid by their format. This means certain tokens must be accompanied
with another token which should be defined as a number. These include:
> push, save, get

Otherwise the remaining tokens must not be accompanied by any other token, even a number,
on the same line. These tokens include:
> pop, add, sub, mul, div, mod, skip

If a parsing error occurs, rather than returning a false, it is recommended to raise a
ValueError with the appropriate message

## Stack Machine
We begin the second file by calling it "stack_macine.py". This file will hold a class called
'StackMachine'. This class is allowed to hold any internal structures created and should include a CurrentLine property and the required functions. 
This class will hold the following functions: push, pop, add, sub, mul, div, mod, skip, save, get
and execute.

To begin, the CurrentLine is initialized to zero. This property is used later on
during part 3. The execute function should accept a list of tokens (which should
have already been tokenized and parsed) and should act like a switch by being able
to read the line and then create behavior based on that line. I.e. 'push 5' should
call the push function with a argument of 5. These functions all have different behaviors
and should be implemented as stated:
* push # - inserts the number on to the top of the stack. Returns None
* pop - pops the top value off of the stack. Returns the popped value
* add - pops two items off of the stack, adds them together and pushes it back in. Returns None
* sub - pops two items off of the stack, item one subtracts to item two and are pushed back into the stack. Returns None
* mul - pops two items off of the stack, multiplies them together and pushes its product back in. Returns None
* div - pops two items off of the stack, divides the first item by the second item and pushes its quotient back in. Returns None
* mod - pops two items off of the stack, divides the first item by the second item and pushes the remainder, instead of the quotient, back in. Returns None
* skip - pops two items off of the stack, checks whether the first popped item is zero. If it is zero, the CurrentLine is incremented by the second item. If it isn't zero, do nothing. Returns None in both cases
* save # - pops one item off the stack and places it into a separate structure for later use (during the get function). Returns None
* get # - gets a previously saved item out of the area it was saved. It then pushes the item onto the stack. Note that when you get the
saved item out of the structure, it should not be deleted. The only case when the saved item should be removed is when it is overwritten by another
save function of the same index. This means you can get the saved item multiple times. Returns None

When the execute function is finished, the CurrentLine property should be incremented
by one. Ensure the program raises an IndexError when a value cannot be popped out of
the stack when it is deemed empty, as well as when the get function attempts to
get an item out of the specified index but it is empty. 

## Driver
Part 3, the driver program, should be called "driver.py". 

Ensure it imports everything necessary out of part 1 and part 2. The program should read a command line argument
and denote it as a file. It should then be tokenized and then parsed. It is recommended
to then place the tokens into an indexable structure to easily navigate and obtain
the required keywords when needed. The StackMachine class should then be instantiated and
execute the contents line by line. When there are no more lines, it should stop executing.
Ensure that if an IndexError is raised via the StackMachine class, the following message is displayed:

                Line #: '<tokens>' caused Invalid Memory Access
                
Also ensure that if anything other than 'None' is returned it is printed out (i.e. the pop function).
Thirdly, ensure that if in any instance that the CurrentLine property is negative (meaning a negative index when read)
it is handled by the following message and the program exits out:

                Trying to execute invalid line: #

