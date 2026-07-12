students = ["Ganesh", "Rahul", "sneha", "Priya", "om", "rutuja"]
attendance = [1,0,1,1,0,1] # 1= Present, 0 = Abesent
present_count = 0
absent_students = []
for i in range(len(students)):
    name = students[i]
    status = attendance[i]
    if status == 1:
        present_count +=1
        print(f"{name} - present")
    else:
        absent_students.append(name)

print(f"{name} - absent")
print("\n--- Attendance Report ---")
print(f"Total students: {len(students)}")
print(f"present: {present_count}")
print(f"absent: {len(absent_students)}")
print("Absent List: {absent_students}")

items = ["Rice", "sugar", "oil", "milk", "Bread"]
prices = [55, 42, 130, 28, 35]
quantities = [5, 2, 1, 3, 2]
total_bill = 0
print("---- Grocery Bill ----")
for i in range(len(items)):
    item_totle = prices[i] * quantities[i]
    total_bill += item_totle
    print(f"{items[i] : <8} x {quantities[i]: <2} = Rs. {item_totle}")
    discount = 0
    if total_bill > 500:
        discount = total_bill * 0.10
        total_bill -= discount
        print("----------------")
        print(f"Discount Applied: Rs. {discount:.2f}")
        print(f"Final Total: Rs. {total_bill:.2f}")

        amount = 4830
        denominations = [2000, 500, 200, 100, 50, 20, 10]
        notes_given = {}
        remaining = amount
        for note in denominations:
            if remaining >= note:
                count = remaining // note
                notes_given[note] = count
                remaining = remaining % note
                print(f"Amount to Withdraw: Rs. {amount}")
                print("---- Denomination Breakdown ----")
                for note, count in notes_given.items():
                    print(f"Rs. {note} x {count} = Rs. {note * count}")
                    print(f"Remaining (not dispensed) : Rs. {remaining}")

                    password = "Rutuja@123"
                    has_upper = False
                    has_lower = False
                    has_digit = False
                    has_special = False
                    special_chars = "!@#$%^&*"
                    for char in password:
                        if char.isupper():
                            has_upper = True
                        elif char.islower():
                            has_lower = True
                        elif char.isdigit():
                            has_digit = True
                        elif char in special_chars:
                            has_special = True
                            score = sum([has_upper, has_lower, has_digit, has_special])
                            print(f"password: {password}")
                            print(f"lenth: {len(password)}")
                            print(f"uppercase: {has_upper} | Lowercase: {has_lower}")
                            print(f"digit: {has_digit} | special char: {has_special}")
                            if score == 4 and len(password) >= 8:
                                print("strength: STRONG")
                            elif score >= 2:
                                print("strength: MEDIUM")
                            else:
                                print("strength: WEAK")
                                

