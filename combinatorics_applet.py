"""
Interactive Combinatorics Applet
An educational tool for exploring combinatorial concepts including
permutations, combinations, and the fundamental counting principle.
"""

import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import math
from itertools import permutations, combinations, product


def factorial(n):
    """
    Calculate factorial of n.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n, or None if n is negative
        
    Note: This wrapper provides consistent error handling for negative inputs
    across the module, returning None instead of raising an exception.
    """
    if n < 0:
        return None
    return math.factorial(n)


def nPr(n, r):
    """Calculate permutations: n!/(n-r)!"""
    if n < 0 or r < 0 or r > n:
        return None
    return factorial(n) // factorial(n - r)


def nCr(n, r):
    """Calculate combinations: n!/(r!(n-r)!)"""
    if n < 0 or r < 0 or r > n:
        return None
    return factorial(n) // (factorial(r) * factorial(n - r))


class CombinatoricsApplet:
    """Interactive applet for exploring combinatorics concepts."""
    
    def __init__(self):
        self.output = widgets.Output()
        self.setup_widgets()
        
    def setup_widgets(self):
        """Set up all the interactive widgets."""
        # Mode selection
        self.mode = widgets.Dropdown(
            options=['Permutations', 'Combinations', 'Product (Counting Principle)', 'Custom Lists'],
            value='Permutations',
            description='Mode:',
            style={'description_width': 'initial'}
        )
        
        # Input widgets
        self.n_input = widgets.IntText(
            value=5,
            description='n (total items):',
            style={'description_width': 'initial'}
        )
        
        self.r_input = widgets.IntText(
            value=3,
            description='r (items to select):',
            style={'description_width': 'initial'}
        )
        
        # Custom list inputs
        self.list1_input = widgets.Text(
            value='A,B,C',
            description='List 1 (comma-separated):',
            style={'description_width': 'initial'}
        )
        
        self.list2_input = widgets.Text(
            value='1,2,3',
            description='List 2 (comma-separated):',
            style={'description_width': 'initial'}
        )
        
        self.list3_input = widgets.Text(
            value='',
            description='List 3 (optional):',
            style={'description_width': 'initial'}
        )
        
        # Display options
        self.show_all = widgets.Checkbox(
            value=False,
            description='Show all results (may be slow for large n)',
            style={'description_width': 'initial'}
        )
        
        self.max_display = widgets.IntText(
            value=20,
            description='Max results to display:',
            style={'description_width': 'initial'}
        )
        
        # Calculate button
        self.calculate_btn = widgets.Button(
            description='Calculate',
            button_style='primary',
            icon='calculator'
        )
        
        # Bind events
        self.calculate_btn.on_click(self.on_calculate)
        self.mode.observe(self.on_mode_change, 'value')
        
    def on_mode_change(self, change):
        """Handle mode changes to show/hide relevant widgets."""
        self.update_display()
        
    def update_display(self):
        """Update which widgets are visible based on mode."""
        with self.output:
            clear_output(wait=True)
            self.display_help()
    
    def on_calculate(self, button):
        """Calculate and display results based on current mode."""
        with self.output:
            clear_output(wait=True)
            
            mode = self.mode.value
            
            if mode in ['Permutations', 'Combinations']:
                self.calculate_npr_ncr()
            elif mode == 'Product (Counting Principle)':
                self.calculate_product()
            elif mode == 'Custom Lists':
                self.calculate_custom()
    
    def calculate_npr_ncr(self):
        """Calculate permutations or combinations."""
        n = self.n_input.value
        r = self.r_input.value
        mode = self.mode.value
        
        # Validation
        if n < 0 or r < 0:
            print("❌ Error: n and r must be non-negative")
            return
        if r > n:
            print("❌ Error: r cannot be greater than n")
            return
            
        # Calculate formula result
        if mode == 'Permutations':
            result = nPr(n, r)
            formula = f"P({n},{r}) = {n}!/({n}-{r})! = {result:,}"
            print(f"🔢 Permutations of {r} items from {n} items")
            print(f"Formula: {formula}")
            print(f"\nResult: {result:,} permutations\n")
            
            # Generate actual permutations if requested
            if self.show_all or result <= self.max_display.value:
                items = list(range(1, n + 1))
                perms = list(permutations(items, r))
                
                print(f"First {min(len(perms), self.max_display.value)} permutations:")
                for i, perm in enumerate(perms[:self.max_display.value]):
                    print(f"  {i+1}. {perm}")
                    
                if len(perms) > self.max_display.value:
                    print(f"  ... and {len(perms) - self.max_display.value} more")
        else:  # Combinations
            result = nCr(n, r)
            formula = f"C({n},{r}) = {n}!/({r}!×({n}-{r})!) = {result:,}"
            print(f"🔢 Combinations of {r} items from {n} items")
            print(f"Formula: {formula}")
            print(f"\nResult: {result:,} combinations\n")
            
            # Generate actual combinations if requested
            if self.show_all or result <= self.max_display.value:
                items = list(range(1, n + 1))
                combs = list(combinations(items, r))
                
                print(f"First {min(len(combs), self.max_display.value)} combinations:")
                for i, comb in enumerate(combs[:self.max_display.value]):
                    print(f"  {i+1}. {comb}")
                    
                if len(combs) > self.max_display.value:
                    print(f"  ... and {len(combs) - self.max_display.value} more")
    
    def calculate_product(self):
        """Calculate Cartesian product using counting principle."""
        list1 = [x.strip() for x in self.list1_input.value.split(',') if x.strip()]
        list2 = [x.strip() for x in self.list2_input.value.split(',') if x.strip()]
        list3 = [x.strip() for x in self.list3_input.value.split(',') if x.strip()]
        
        if not list1 or not list2:
            print("❌ Error: Please provide at least two lists")
            return
        
        lists = [list1, list2]
        if list3:
            lists.append(list3)
        
        # Calculate total using counting principle
        total = 1
        for lst in lists:
            total *= len(lst)
        
        print(f"🔢 Cartesian Product (Counting Principle)")
        for i, lst in enumerate(lists, 1):
            print(f"List {i}: {lst} (size: {len(lst)})")
        
        print(f"\nTotal combinations: {' × '.join(str(len(lst)) for lst in lists)} = {total:,}\n")
        
        # Generate actual products
        prod = list(product(*lists))
        
        print(f"First {min(len(prod), self.max_display.value)} results:")
        for i, item in enumerate(prod[:self.max_display.value]):
            print(f"  {i+1}. {item}")
        
        if len(prod) > self.max_display.value:
            print(f"  ... and {len(prod) - self.max_display.value} more")
    
    def calculate_custom(self):
        """
        Calculate with custom lists.
        
        This mode is functionally identical to the Product mode but provides
        a clearer label for users who want to work with their own items
        rather than abstract mathematical concepts.
        """
        self.calculate_product()
    
    def display_help(self):
        """Display help text based on current mode."""
        mode = self.mode.value
        
        help_text = {
            'Permutations': """
📚 <b>Permutations</b>: Order matters!
Calculates P(n,r) = n!/(n-r)!
Example: Arranging 3 books from 5 books on a shelf.
            """,
            'Combinations': """
📚 <b>Combinations</b>: Order doesn't matter!
Calculates C(n,r) = n!/(r!(n-r)!)
Example: Choosing 3 toppings from 5 available toppings.
            """,
            'Product (Counting Principle)': """
📚 <b>Counting Principle</b>: Multiply choices!
If you have m ways to do one thing and n ways to do another,
there are m × n ways to do both.
Example: 3 shirts × 2 pants = 6 outfits.
            """,
            'Custom Lists': """
📚 <b>Custom Lists</b>: Use your own items!
Enter your items separated by commas.
Example: Colors, Sizes, Styles
            """
        }
        
        display(HTML(help_text.get(mode, "")))
    
    def display(self):
        """Display the complete applet interface."""
        # Title
        title = widgets.HTML(
            value="<h2>🎲 Interactive Combinatorics Applet</h2>"
        )
        
        # Instructions
        instructions = widgets.HTML(
            value="""
            <p>Explore permutations, combinations, and the counting principle interactively!</p>
            <ul>
                <li><b>Permutations</b>: Order matters (e.g., ABC vs BAC are different)</li>
                <li><b>Combinations</b>: Order doesn't matter (e.g., ABC = BAC)</li>
                <li><b>Counting Principle</b>: Multiply the number of choices at each step</li>
            </ul>
            """
        )
        
        # Create conditional display boxes
        basic_box = widgets.VBox([
            self.n_input,
            self.r_input
        ])
        
        custom_box = widgets.VBox([
            self.list1_input,
            self.list2_input,
            self.list3_input
        ])
        
        options_box = widgets.VBox([
            self.show_all,
            self.max_display
        ])
        
        # Main layout
        layout = widgets.VBox([
            title,
            instructions,
            widgets.HTML(value="<hr>"),
            self.mode,
            basic_box,
            custom_box,
            widgets.HTML(value="<hr>"),
            widgets.HTML(value="<h3>Display Options</h3>"),
            options_box,
            widgets.HTML(value="<hr>"),
            self.calculate_btn,
            widgets.HTML(value="<hr>"),
            self.output
        ])
        
        display(layout)
        
        # Show initial help
        with self.output:
            self.display_help()


def create_applet():
    """
    Create and display a new combinatorics applet.
    
    Usage:
        from combinatorics_applet import create_applet
        create_applet()
    """
    applet = CombinatoricsApplet()
    applet.display()
    return applet


# Example usage for testing
if __name__ == "__main__":
    # This would run in a Jupyter notebook
    print("Import this module in a Jupyter notebook and run create_applet()")
