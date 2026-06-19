 total_spent = 0.0 

print("--- DecodeLabs Financial Engine ---")
print("Enter your expenses. Type 'exit' to finalize the ledger.")

while True:
    user_entry = input("\nEnter expense (or 'exit'): ")

    if user_entry.lower() == 'exit':
        break

    try:
        current_expense = float(user_entry)
        
        total_spent += current_expense
        
        print(f"Transaction Recorded: ${current_expense:.2f}")
        print(f"Current Running Total: ${total_spent:.2f}")
        
    except ValueError:
        print("Error: Invalid entry. Please provide a numeric value.")

print("\n" + "="*30)
print(f"FINAL AUDIT TOTAL: ${total_spent:.2f}")
print("="*30)

