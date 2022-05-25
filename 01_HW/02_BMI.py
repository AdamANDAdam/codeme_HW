# calc your BMI index

def BMI(mass, height):
    BMI= (mass)/(height**2)
    print(f'Your BMI is {round(BMI)}')
def main():
    mass = float(input('Add your mass in [kg]'))
    height = float(input('Add your height in [m]'))
    BMI(mass, height)
main()
