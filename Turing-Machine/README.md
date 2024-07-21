Sure! Here’s a README file tailored for your Turing Machine simulator project. This documentation explains the purpose of the script, how to run it, and provides some sample input and output.

---

# Turing Machine Simulator

## Overview
This project contains a Python script that decodes a binary-encoded Turing Machine, simulates its behavior, and tests a series of input strings on the machine. The script processes the encoded Turing Machine, decodes it, simulates its operations, and outputs whether each input string is accepted or rejected by the Turing Machine.

## Input Format
The script expects the following inputs:

1. **Encoded Turing Machine:** A binary string representing the encoded Turing Machine.
2. **Number of Input Strings:** An integer `n` representing the number of strings to test on the Turing Machine.
3. **Input Strings:** `n` binary strings to be tested on the Turing Machine.

### Constraints
- `1 ≤ n ≤ 10`
- The encoded Turing Machine guarantees no infinite loops.
- The start state is coded as `1`.
- The final state is coded as `1 + number_of_states`.
- The blank character on the tape is coded as `1`.

## Output Format
The script outputs exactly `n` lines. Each line corresponds to the result of testing an input string on the Turing Machine, printing either `Accepted` or `Rejected`.

## Example

### Input
```plaintext
101101011011001010110101
3
11011011
110111011
111011011
```

### Output
```plaintext
Accepted
Accepted
Rejected
```

### Input
```plaintext
101110110111101100101101111011011001101101101101100110111011011101100110111110111011010011101101110110100111011101110111010011101111010111101100111101101111011011001111010111110101
5
111011111011111111
1111101110111
1110111011111011111
111011111
```

### Output
```plaintext
Rejected
Rejected
Accepted
Rejected
Accepted
```

## How to Run
1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the script using a Python interpreter. Provide the required inputs when prompted.

```sh
python turing_machine_simulator.py
```

### Example Run
```sh
$ python turing_machine_simulator.py
101101011011001010110101
3
11011011
110111011
111011011
```
The output will be:
```plaintext
Accepted
Accepted
Rejected
```

## Code Explanation

### Functions
- **`languageOfTuringMachine(s)`**: Decodes the binary string representing the Turing Machine into a list of transitions.
- **`final_state(mylist)`**: Determines the final state from the list of transitions.
- **`find_state_index(mylist, s, start_state)`**: Finds the index of the transition corresponding to the current state and tape symbol.
- **`travelOnTape(mylist, navar)`**: Simulates the Turing Machine on the input tape and returns `Accepted` or `Rejected`.

### Main Execution
- The script first reads and decodes the Turing Machine.
- It then reads the number of input strings and each input string.
- For each input string, the script simulates the Turing Machine and prints the result.

## Notes
- The script uses a global variable `first` to keep track of the current states during the string evaluation process.
- The machine's operations assume that the blank symbol and the initial and final states are properly coded as described.
