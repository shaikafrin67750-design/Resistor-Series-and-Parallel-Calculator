print("ELECTRICAL ENERGY CONSUMPTION CALCULATOR")
print("----------------------------------------")

power = float(input("Enter appliance power (in Watts): "))
hours = float(input("Enter usage time per day (in hours): "))
days = int(input("Enter number of days: "))

# Energy calculation
energy_wh = power * hours * days
energy_kwh = energy_wh / 1000

print("\nElectrical Energy Consumption")
print("Energy =", energy_kwh, "kWh")
