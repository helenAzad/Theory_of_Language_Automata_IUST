# PDA-Based Calculator

## Overview

This project implements a calculator that parses and evaluates mathematical expressions using a Pushdown Automaton (PDA). It supports various operators, functions, and parentheses to handle complex expressions. The calculator checks the validity of the input expression and calculates the result, displaying `INVALID` for invalid inputs.

## Features

- **Operators**: Supports addition `+`, subtraction `-`, multiplication `*`, division `/`, exponentiation `^`, and square root `sqrt`.
- **Functions**: Handles trigonometric functions `sin`, `cos`, `tan`, as well as `abs` for absolute value, and exponential functions `exp`, `ln`.
- **Parentheses Handling**: Correctly processes nested and balanced parentheses.
- **Error Handling**: Detects invalid expressions, division by zero, and domain errors for functions.

## Input Format

The input is a single line string containing:
- **Numbers**: Real numbers (both integer and floating-point).
- **Operators**: `+`, `-`, `*`, `/`, `^`.
- **Functions**: `sqrt`, `exp`, `ln`, `sin`, `cos`, `tan`, `abs`.
- **Parentheses**: `(` and `)` for grouping expressions.

### Example

#### Input

```plaintext
10 / 2 + 4 * -3.5
```

#### Output

```plaintext
-9.00
```

## Usage

To use the calculator, provide an input expression as described. The program will evaluate the expression and print the result with two decimal places, or `INVALID` if the input is not valid.

### Running the Program

1. **Run the Script**: Execute the Python script in your environment.
2. **Provide Input**: Input a mathematical expression in the specified format.
3. **Get Output**: The result will be displayed or `INVALID` if the expression is invalid.

#### Example Command

```sh
$ python calculator.py
```

#### Example Input

```plaintext
sin(ln(5 ^ 6 * 3 - cos(sin(6))))
```

#### Example Output

```plaintext
-0.97
```

## Code Explanation

### Functions

1. **`is_number(s)`**: Checks if a string `s` is a valid number.
2. **`is_operand(s)`**: Checks if a string `s` is a valid operator.
3. **`is_func(s)`**: Checks if a string `s` is a function.
4. **`is_par(s)`**: Checks if a string `s` is a parenthesis.
5. **`add_to_list(s)`**: Parses the input string and extracts numbers, operators, functions, and parentheses.
6. **`priority(s)`**: Determines the precedence of operators.
7. **`add_to_stacks(li)`**: Converts infix expressions to postfix notation using stacks.
8. **`push_to_stack(li)`**: Evaluates the postfix expression using a stack-based approach.
9. **`calculateOper(oper, a, b)`**: Performs arithmetic operations based on the operator.
10. **`calculateFunc(func, a)`**: Evaluates mathematical functions.
11. **`the_number_of_par(entry)`**: Checks if parentheses in the expression are balanced.

### Error Handling

- **Invalid Input**: Prints `INVALID` if the expression has unmatched parentheses, invalid operations, or mathematical errors (e.g., division by zero, invalid function arguments).

---

This README provides a comprehensive guide for users to understand and utilize your PDA-based calculator, including input format, usage instructions, and code functionality.