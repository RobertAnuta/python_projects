# Coffee Machine - README


This is a Python program for a simulated coffee machine that dispenses espresso, latte, and cappuccino.

**Features:**

* Manages a menu of coffee drinks with ingredients and costs.
* Checks if there are sufficient resources (water, milk, coffee) to make a drink.
* Takes payment in quarters, dimes, nickels, and pennies.
* Calculates and dispenses change if necessary.
* Provides a report on current resource and money levels.
* Allows machine power on/off functionality.

**Usage:**

1. Run the program: `python coffee_machine.py`
2. The program will prompt you to choose a coffee (espresso, latte, cappuccino) or enter commands ("report" or "off").
3. For coffee selection:
    * The program will check if there are enough resources.
    * If sufficient resources exist, it will ask for payment.
    * It will calculate change and dispense the coffee if payment is sufficient.
4. For "report":
    * The program will display the current levels of water, milk, coffee, and total money collected.
5. For "off":
    * The program will shut down the coffee machine.

**Code Structure:**

* `MENU`: A dictionary containing coffee options with their ingredients (water, milk, coffee) and prices.
* `resources`: A dictionary to track current resource (water, milk, coffee) levels.
* `money`: A dictionary to track the total money collected.
* `check_resources`: Function to check if there are enough resources for a chosen coffee.
* `process_coins`: Function to calculate total payment based on inserted coins.
* `prepare_coffee`: Function to deduct resource usage and add money earned for a coffee.
* `main`: Main function that handles user interaction, coffee selection, payment, and reporting.

**Note:**

* This is a simulation and doesn't interact with real-world hardware.
* Error handling for invalid user input or insufficient resources could be further enhanced.

