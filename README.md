# Tokenizing & Parsing Stack Machine

## Synopsis
The purpose of this project is to familiarize the programmer with the python language 
and virtual machines by creating a tokenizer and parser function alongside a stack
machine class.

## Stack Machine
We begin the second file by calling it "stack_macine.py". This file will hold a class called
'StackMachine'. This class is allowed to hold any interal structures that you believe is required
to use but should include a CurrentLine property and the required functions. 
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

