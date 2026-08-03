print("======================================================")

print("Horsepower ↔ Torque Calculator")

print("======================================================")

torque = float(input("Enter Torque (Nm): "))
rpm = float(input("Enter RPM: "))

horsepower = (torque*rpm)/7127

print()
print("======================================================")
print("Horsepower = {:.2f} HP". format(horsepower))
print("======================================================")
print("Horsepower ↔ Torque Calculator v1.1")
