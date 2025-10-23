# CombinatorialCode

Educational resources for learning combinatorics through interactive Python notebooks.

## 📚 Contents

This repository contains:
- **Lesson Notebooks (1-7)**: Educational lessons on combinatorics concepts
- **Python Primer**: Introduction to Python programming
- **Interactive Combinatorics Applet**: An interactive tool for exploring permutations, combinations, and the counting principle

## 🎲 Interactive Combinatorics Applet

The applet provides an interactive interface for exploring:
- **Permutations**: Arrangements where order matters (P(n,r) = n!/(n-r)!)
- **Combinations**: Selections where order doesn't matter (C(n,r) = n!/(r!(n-r)!))
- **Counting Principle**: Multiplying independent choices
- **Custom Lists**: Exploring combinations with your own data

### Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Open the demo notebook:
```bash
jupyter notebook Combinatorics_Applet_Demo.ipynb
```

3. Run all cells to launch the interactive applet!

### Usage Example

```python
from combinatorics_applet import create_applet

# Create and display the interactive applet
applet = create_applet()
```

Or use the functions directly:
```python
from combinatorics_applet import nPr, nCr, factorial

# Calculate permutations: P(5,3)
print(nPr(5, 3))  # Output: 60

# Calculate combinations: C(5,3)  
print(nCr(5, 3))   # Output: 10
```

## 🚀 Features

- **Interactive Widgets**: User-friendly interface for exploring combinatorics
- **Live Calculations**: See results instantly as you change parameters
- **Visual Results**: Display actual permutations and combinations
- **Educational**: Built-in help and formulas for learning
- **Customizable**: Use your own lists and items

## 📖 Learning Resources

The notebook includes:
- Step-by-step examples
- Practice problems
- Mathematical formulas
- Real-world applications

## 🤝 Contributing

Feel free to contribute additional lessons, improvements, or examples!