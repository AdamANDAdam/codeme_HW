# write a code that will compute and display number of minutes within 7 days

def compute_minutes(days):
    minutes = days*24*60
    print(f'During the period of {days} days a number of {minutes} minutes passed.')

def main():
    days = int(input("How many days"))
    compute_minutes(days)

main()

