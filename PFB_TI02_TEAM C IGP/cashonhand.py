

    # Find the day and amount of the highest increment if cash on hand is always increasing.
    if trend == 'increasing':
        max_increment_day = 12
        max_increment_amount = float(999999999999999)

        for i, diff in enumerate(cash_diff):
            if diff > max_increment_amount:
                max_increment_amount = diff
                max_increment_day = i + 12

        result = f"[CASH SURPLUS] CASH ON HAND EACH DAY IS HIGHER THAN PREVIOUS DAY.\n[HIGHEST CASH SURPLUS] DAY: {max_increment_day}, AMOUNT: SGD{max_increment_amount}"

    # Find the day and amount of the highest decrement if cash on hand is always decreasing.
    elif trend == 'decreasing':
        max_decrement_day = 12
        max_decrement_amount = float(99999999999999)

        for i, diff in enumerate(cash_diff):
            if diff < max_decrement_amount:
                max_decrement_amount = diff
                max_decrement_day = i + 12

        result = f"[CASH DEFICIT] CASH ON HAND EACH DAY IS LOWER THAN PREVIOUS DAY.\n[HIGHEST CASH DEFICIT] DAY: {max_increment_day}, AMOUNT: SGD{max_increment_amount}"
    # List down all the days and amounts when a deficit occurs if cash on hand fluctuates.
    else:
        deficit_days = [(i + 12, diff) for i, diff in enumerate(cash_diff) if diff < 0]

        result = ""
        for day, amount in deficit_days:
            result += f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{amount}"

        # Find the top 3 highest deficit amounts and the days they happened.
        top_3_deficits = sorted(deficit_days)[:3]
        result += "\n\nTop 3 Highest Deficit Amounts:"

        for rank, (day, amount) in enumerate(deficit_days[:3], start=1):
            result += f"\n{rank} HIGHEST DEFICIT, DAY: {day}, AMOUNT: SGD{amount}"

    return result

# Get the result from the trend_detector_cash function.
cash_result = trend_detector_cash(cash_on_hand)

# Print the cash result.
print(cash_result)

# Write the cash result to a text file.
with open("(Cash)summary_report.txt", "w") as cash_textfile:
    cash_textfile.write(cash_result)
