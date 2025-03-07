# Financial Transaction Tracker

## Overview

This program is a **Financial Transaction Tracker** that allows users to record and analyze their income and expenses using a CSV file. The application provides functionalities to:

1. **Add a New Transaction** (with date, amount, category, and description)
2. **View Transactions Within a Date Range**
3. **Visualize Transactions** with a plotted graph

The program reads, writes, and processes financial data using Python and the Pandas library.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries Used**:
  - `pandas` → For handling CSV files and data processing
  - `csv` → For reading and writing CSV files
  - `datetime` → For date manipulation
  - `matplotlib.pyplot` → For plotting graphs

---

## File Structure

- `main.py` → Contains the core functionality of the program
- `Data_Entry.py` → Provides input functions like `getamount()`, `getdate()`, `getcategory()`, `getdiscription()`
- `FinancialData.csv` → Stores transaction records
- `README.txt` → This document explaining the program

---

## Features

### 1. Add a New Transaction

- Users can input:
  - **Date** (defaults to the current date if not provided)
  - **Amount**
  - **Category** (Income or Expense)
  - **Description**
- The transaction is stored in `FinancialData.csv`.

### 2. View Transactions Between Dates

- Users can enter a **start date** and **end date** to view transactions.
- The program calculates:
  - **Total Income**
  - **Total Expenses**
  - **Net Worth (Income - Expenses)**

### 3. Plot Transactions

- Users can choose to view a graph of Income vs. Expenses over time.
- Uses Matplotlib to visualize financial trends.

---

## How to Run the Program

### 1. Install Dependencies

Ensure you have **Python** installed, then install the required libraries using:

```
pip install pandas matplotlib
```

### 2. Run the Program

Execute the script using:

```
python main.py
```

### 3. Follow the On-Screen Menu

- Choose an option to **add a transaction**, **view transactions**, or **exit** the program.
- If selecting to view transactions, you can also choose to **plot** the data.

---

## Notes

- If `FinancialData.csv` does not exist, it will be **created automatically**.
- The program ensures that **date formats are consistent** (`dd-mm-yyyy`).
- Transaction amounts are stored as **floating-point numbers**.

---

## Future Improvements

- Add a **GUI Interface** for better user experience
- Implement **category-based filtering**
- Provide **export options** (Excel, PDF reports)

---

## Author

- Created by **Pradeep M**
- For any issues or improvements, feel free to contribute!

