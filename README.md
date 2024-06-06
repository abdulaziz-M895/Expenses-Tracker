# Expense Tracker

## Description
This is a basic Expense Tracker application built using Python and Tkinter. The application allows users to input their expenses with details such as amount, currency, category, payment method, and date. It also calculates the total expenses in USD using real-time currency conversion rates.

## Features
- Add expense with amount, currency, category, payment method, and date.
- Display the list of added expenses in a table format.
- Calculate and display the total amount in USD.
- Fetch real-time currency conversion rates.

## Usage
1. **Enter Expense Details**:
    - Enter the amount of the expense.
    - Select the currency from the dropdown menu.
    - Choose a category from the dropdown menu.
    - Select the payment method from the dropdown menu.
    - Enter the date in YYYY-MM-DD format.

2. **Add Expense**:
    - Click the "Add Expense" button to add the expense to the list.

3. **View Expenses**:
    - The entered expenses will be displayed in the table format below the form.

4. **View Total in USD**:
    - The total amount of all entered expenses converted to USD will be displayed at the bottom.

## Dependencies
- Python 3.x
- Tkinter
- Requests

## Code Structure
- **expense_tracker.py**: Main script containing the `ExpenseTracker` class and the application logic.

## Acknowledgements
- [ExchangeRate-API](https://www.exchangerate-api.com/) for providing the currency conversion API.
