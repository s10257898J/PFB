############################################################################# Overheads segment ##################################################################
from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    overheads=[] 

    # Append overhead records into the overheads list.
    for row in reader:
        # Get the category and overhead value for each record and append to the overheads list.
        overheads.append({
            'category': row[0],
            'overheads': float(row[1])
        })

# Initialize variables to keep track of the maximum overhead and its corresponding category
max_overhead_category = ""
max_overhead_value = 0.0

# Iterate through the list of overheads
for entry in overheads:
    if entry['overheads'] > max_overhead_value:
        max_overhead_value = entry['overheads']
        max_overhead_category = entry['category']

overhead_result=f"[HIGHEST OVERHEAD] {max_overhead_category}: {max_overhead_value}%"


##################################################################### Cash on hand segment ############################################################3
from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"cash-on-hand-sgd.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    cash_on_hand=[]

# Append cash on hand records into the cash_on_hand list.
    for row in reader:
        cash_on_hand.append({
            'day': int(row[0]),
            'cash_on_hand': int(row[1])
        })
def trend_detector_cash(cash_on_hand):
    """
    Calculates cash on hand deficit and increasing days
    """
    # Calculate the difference in cash on hand for each day.
    cash_diff = [cash_on_hand[i + 1]['cash_on_hand'] - cash_on_hand[i]['cash_on_hand']
                 for i in range(len(cash_on_hand) - 1)]

    # Determine the trend of cash on hand.
    cash_trend = None

    # Check if cash on hand is always increasing.
    cash_is_increasing = True
    for diff in cash_diff:
        if diff < 0:
            cash_is_increasing = False
            break

    # Check if cash on hand is always decreasing.
    cash_is_decreasing = True
    for diff in cash_diff:
        if diff > 0:
            cash_is_decreasing = False
            break

    # Determine the trend based on conditions.
    if cash_is_increasing:
        cash_trend = 'increasing'
    elif cash_is_decreasing:
        cash_trend = 'decreasing'
    else:
        cash_trend = 'fluctuating'


    # Find the day and amount of the highest increment if cash on hand is always increasing.
    if cash_trend == 'increasing':
        cash_max_increment_day = 11
        cash_max_increment_amount = float(999999999999999999)

        for i, diff in enumerate(cash_diff):
            if diff > cash_max_increment_amount:
                cash_max_increment_amount = diff
                cash_max_increment_day = i + 12

        result = f"[CASH SURPLUS] CASH ON HAND EACH DAY IS HIGHER THAN PREVIOUS DAY.\n[HIGHEST CASH SURPLUS] DAY: {cash_max_increment_day}, AMOUNT: SGD{cash_max_increment_amount}"

    # Find the day and amount of the highest decrement if cash on hand is always decreasing.
    elif cash_trend == 'decreasing':
        cash_max_decrement_day = 11
        cash_max_decrement_amount = float(-999999999999999999)

        for i, diff in enumerate(cash_diff): 
            if diff < cash_max_decrement_amount:
                cash_max_decrement_amount = diff
                cash_max_decrement_day = i + 12   

        result = f"[CASH DEFICIT] CASH ON HAND EACH DAY IS LOWER THAN PREVIOUS DAY.\n[HIGHEST CASH DEFICIT] DAY: {cash_max_increment_day}, AMOUNT: SGD{cash_max_increment_amount}"
    # List down all the days and amounts when a deficit occurs if cash on hand fluctuates.
    else:
        cash_deficit_days = [(i + 12, diff) for i, diff in enumerate(cash_diff) if diff < 0]

        result = ""
        for day, amount in cash_deficit_days:
            result += f"\n[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n"

        # Find the top 3 highest deficit amounts and the days they happened.
        top_3_deficits = sorted(cash_deficit_days)[:3]
        result += "\nTop 3 Highest Deficit Amounts:"

        for rank, (day, amount) in enumerate(top_3_deficits, start=1):
            if rank == 1:
                rank1 = "[HIGHEST"
            elif rank == 2: 
                rank1 = "[2ND HIGHEST"
            elif rank == 3:
                rank1 = "[3RD HIGHEST"
            
        result += f"\n{rank1} CASH DEFICIT], DAY: {day}, AMOUNT: SGD{amount}"

    return result

# Get the result from the trend_detector_cash function.
cash_result = trend_detector_cash(cash_on_hand)


################################################################## Net Profit Segment ###########################################################

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
    """
    Calculates profit and loss deficit or increasing days
    """
    # Calculate the difference in net profit for each day.
    net_profit_diff = [profit_and_loss[i + 1]['net_profit'] - profit_and_loss[i]['net_profit']
                       for i in range(len(profit_and_loss) - 1)]

    # Determine the trend of net profit.
    Net_profit_trend = 0

    # Check if net profit is always increasing.
    Net_profit_is_increasing = True
    for diff in net_profit_diff:
        if diff < 0:
            Net_profit_is_increasing = False
            break

    # Check if net profit is always decreasing.
    Net_profit_is_decreasing = True
    for diff in net_profit_diff:
        if diff > 0:
            Net_profit_is_decreasing = False
            break

    # Determine the trend based on conditions.
    if Net_profit_is_increasing:
        Net_profit_trend = 'increasing'
    elif Net_profit_is_decreasing:
        Net_profit_trend = 'decreasing'
    else:
        Net_profit_trend = 'fluctuating'

# Find the day and amount of the highest increment if net profit is always increasing.
    if Net_profit_trend == 'increasing':
        Net_profit_max_increment_day = 11
        Net_profit_max_increment_amount = float(9999999999999999999999)

        for i, diff in enumerate(net_profit_diff):
            if diff > Net_profit_max_increment_amount:
                Net_profit_max_increment_amount = diff
                Net_profit_max_increment_day = i + 12
               
        result = f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY.\n[HIGHEST NET PROFIT SURPLUS] \nDAY: {Net_profit_max_increment_day}\nAMOUNT: {Net_profit_max_increment_amount}"

    # Find the day and amount of the highest decrement if net profit is always decreasing.
    elif Net_profit_trend == 'decreasing':
        Net_profit_max_decrement_day = 11
        Net_profit_max_decrement_amount = float(9999999999999999999999)

        for i, diff in enumerate(net_profit_diff):
            if diff < Net_profit_max_decrement_amount:
                Net_profit_max_decrement_amount = diff
                Net_profit_max_decrement_day = i + 12

        result = f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY.\n[HIGHEST NET PROFIT DEFICIT] \nDAY: {Net_profit_max_decrement_day}\nAMOUNT: {Net_profit_max_decrement_amount}"

    else:
        deficit_days = [(i + 12, diff) for i, diff in enumerate(net_profit_diff) if diff < 0]

        result = ""
        for day, amount in deficit_days:
            result += f"\n[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n"

        # Find the top 3 highest deficit amounts and the days they happened.
        top_3_deficits = sorted(deficit_days)[:3]

        result += "\nTop 3 Highest Deficit Amounts:"

        for rank, (day, amount) in enumerate(top_3_deficits, start=1):
            if rank == 1:
                rank1 = "[HIGHEST"
            elif rank == 2: 
                rank1 = "[2ND HIGHEST"
            elif rank == 3:
                rank1 = "[3RD HIGHEST"
            
        result += f"\n{rank1} NET PROFIT DEFICIT], DAY: {day}, AMOUNT: SGD{amount}"

    return result

# Get the result from the trend_detector function.
result = trend_detector(profit_and_loss)


################################ Section for putting into text file###############################################################3
# Print the highest overhead category.
print(overhead_result)
# Print the cash result.
print(cash_result)
# Print the result
print(result)

# Write the result to a text file.
with open("Summary_report.txt", "w") as summary_report_textfile:
    summary_report_textfile.write(overhead_result + "\n")
    summary_report_textfile.write(cash_result + "\n")
    summary_report_textfile.write(result)
