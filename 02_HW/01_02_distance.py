# calc trip costs

def costs(distance, consumption, price):
    print(f'Cost of trip is equal to {distance*consumption/100}')

def main():
    distance = float(input('Insert distance planned:'))
    consumpion = float(input('How many lires per 100 km travelled?'))
    price = float(input('Whats the current fuel price?'))
    costs(distance, consumpion, price)
main()