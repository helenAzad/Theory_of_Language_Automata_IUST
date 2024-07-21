# Accept-string-in-finiteAutomata

## Overview
This repository contains a Python script that simulates a finite automaton to determine whether a given string is accepted by the automaton. The script processes user inputs to define states, alphabet, final states, transitions, and the input string, and then evaluates the string based on the defined automaton.

## Input Format
The script expects the following inputs in sequence:

1. **States:** A comma-separated list of states, enclosed in curly braces.
   - Example: `{q0,q1,q2}`

2. **Alphabet:** A comma-separated list of symbols, enclosed in curly braces.
   - Example: `{a,b}`

3. **Final States:** A comma-separated list of final states, enclosed in curly braces.
   - Example: `{q2}`

4. **Number of Transitions:** An integer indicating the number of transitions.

5. **Transitions:** Multiple lines (as indicated by the previous input) of comma-separated transitions in the format `state1,symbol,state2`.
   - Example:
     ```
     q0,a,q1
     q1,b,q2
     ```

6. **Input String:** The string to be evaluated by the automaton.
   - Example: `ab`

## Execution Steps
1. **Initialization:**
   - Parse the input states, alphabet, and final states, removing the curly braces.
   - Initialize a dictionary to store state transitions.

2. **Transition Setup:**
   - Read the number of transitions.
   - Populate the transitions dictionary with the given state transitions.

3. **String Evaluation:**
   - Define helper functions `func1` and `func2` to check transitions and handle epsilon transitions, respectively.
   - Use the main function `func` to evaluate the input string based on the transitions and states.

4. **Acceptance Check:**
   - Determine if the final state after processing the input string is one of the final states.
   - Print `Accepted` if the string is accepted by the automaton, otherwise print `Rejected`.

## Functions
- **func1(a, b):**
  - Checks if there is a transition from state `a` with symbol `b`.
  - Returns `True` if a transition exists, otherwise returns `False`.

- **func2(a):**
  - Handles epsilon (`$`) transitions.
  - Returns a list of states reachable from state `a` via epsilon transitions.

- **func(a):**
  - Main function to process the input string `a`.
  - Uses `func1` and `func2` to update the current state based on transitions.
  - Checks if the final state after processing the string is one of the final states.
  - Prints `Accepted` or `Rejected` based on the result.

## Example Usage
```plaintext
Input:
{q0,q1,q2}
{a,b}
{q2}
2
q0,a,q1
q1,b,q2
ab

Output:
Accepted
```

## Notes
- The script assumes the automaton can have epsilon transitions, represented by the symbol `$`.
- The script uses a global variable `first` to keep track of the current states during the string evaluation process.

## How to Run
1. Clone the repository.
2. Navigate to the directory containing the script.
3. Run the script using a Python interpreter.
   ```sh
   python Accept-string-in-finiteAutomata.py
   ```
4. Follow the prompts to enter the states, alphabet, final states, number of transitions, transitions, and the input string.
