# Minimization

A Python package implementing DFA (Deterministic Finite Automaton) minimization algorithms for theoretical computer science applications.

## Description

This project implements three key algorithms for working with deterministic finite automata:

### 1. Table Filling Algorithm (`table_filling`)
This is the core DFA minimization algorithm that uses the table filling method to identify equivalent states. The algorithm works in two phases:
- **Initialization**: Marks pairs of states as distinguishable if one is accepting and the other is not
- **Propagation**: Iteratively marks additional pairs as distinguishable based on their transitions

### 2. DFA Equivalence Check (`equivalent`) 
This algorithm determines if two DFAs are equivalent by:
- Creating a union of both DFAs
- Running the table filling algorithm on the combined automaton
- Checking if the start states of the original DFAs are equivalent in the result

### 3. DFA Minimization (`minimize`)
This algorithm minimizes a DFA by:
- Remove state unreachable from the start state.
- Finding all equivalent state pairs using the table filling algorithm
- Using a Disjoint Set Union (DSU) data structure to group equivalent states
- Creating a new minimized DFA with transitions between partitions, new start state and new accepting states

## Installation

### Setting up a Virtual Environment

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

1. Install the package:
```bash
pip install .
```


## Running Tests

After setting up the virtual environment and installing dependencies, run the tests with:

```bash
# Install test dependencies
pip install -e .[test]

# Run tests
pytest tests/
```

## Authors

- Juan Schandin
- Ariel Piñeiro

## Requirements

- Python >= 3.10
- pytest (for testing)
