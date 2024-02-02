from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"profit-and-loss-sgd.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    profit_and_loss=[] 

# Append profit and loss records into the profit_and_loss list.
    for row in reader:
        profit_and_loss.append({
            'day': int(row[0]),
            'sales': int(row[1]),
            'trading_profit': int(row[2]),
            'operating_expense': int(row[3]),
            'net_profit': int(row[4])
        })


def trend_detector(profit_and_loss):
    # Calculate the difference in net profit for each day.
    net_profit_diff = [profit_and_loss[i + 1]['net_profit'] - profit_and_loss[i]['net_profit']
                       for i in range(len(profit_and_loss) - 1)]

    # Determine the trend of net profit.
    trend = 0

    # Check if net profit is always increasing.
    is_increasing = True
    for diff in net_profit_diff:
        if diff < 0:
            is_increasing = False
            break

    # Check if net profit is always decreasing.
    is_decreasing = True
    for diff in net_profit_diff:
        if diff > 0:
            is_decreasing = False
            break

    # Determine the trend based on conditions.
    if is_increasing:
        trend = 'increasing'
    elif is_decreasing:
        trend = 'decreasing'
    else:
        trend = 'fluctuating'
# Find the day and amount of the highest increment if net profit is always increasing.
    if trend == 'increasing':
        max_increment_day = 12
        max_increment_amount = float('-inf')

        for i, diff in enumerate(net_profit_diff):
            if diff > max_increment_amount:
                max_increment_amount = diff
                max_increment_day = i + 12

        result = f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY.\n[HIGHEST NET PROFIT SURPLUS] \nDAY: {max_increment_day}\nAMOUNT: {max_increment_amount}"

    # Find the day and amount of the highest decrement if net profit is always decreasing.
    elif trend == 'decreasing':
        max_decrement_day = 12
        max_decrement_amount = float('inf')

        for i, diff in enumerate(net_profit_diff):
            if diff < max_decrement_amount:
                max_decrement_amount = diff
                max_decrement_day = i + 12

        result = f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY.\n[HIGHEST NET PROFIT DEFICIT] \nDAY: {max_decrement_day}\nAMOUNT: {max_decrement_amount}"

    else:
        deficit_days = [(i + 12, diff) for i, diff in enumerate(net_profit_diff) if diff < 0]

        result = ""
        for day, amount in deficit_days:
            result += f"\n[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}"

        # Find the top 3 highest deficit amounts and the days they happened.
        top_3_deficits = sorted(deficit_days)[:3]

        result += "\n\nTop 3 Highest Deficit Amounts:"

        for rank, (day, amount) in enumerate(top_3_deficits, start=1):
            result += f"\n{rank} HIGHEST DEFICIT, DAY: {day}, AMOUNT: SGD{amount}"

    return result


# Get the result from the trend_detector function.
result = trend_detector(profit_and_loss)

# Print the result.
print(result)

# Write the result to a text file.
with open("(Net Profit)summary_report.txt", "w") as textfile:
    textfile.write(result)



