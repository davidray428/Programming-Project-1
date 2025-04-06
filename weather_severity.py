# Weather Severity Program

total_rain = 0.0
total_wind = 0.0
count = 0

print("Enter rain and wind data for each day (rain wind), or -1.0 to stop:")

while True:
    user_input = input()
    if user_input.strip() == "-1.0":
        break
    try:
        rain_str, wind_str = user_input.strip().split()
        rain = float(rain_str)
        wind = float(wind_str)
        total_rain += rain
        total_wind += wind
        count += 1
    except ValueError:
        print("Invalid input. Please enter two decimal numbers separated by a space or -1.0 to quit.")

# Check if any data was entered
if count > 0:
    avg_rain = total_rain / count
    avg_wind = total_wind / count
    severity = (avg_rain * 10) + avg_wind

    print(f"\nThe average rain is {avg_rain:.1f} inches")
    print(f"The average wind is {avg_wind:.1f} mph")
    print(f"The weather severity for these {count} readings is: {severity:.1f}")
else:
    print("No data was entered.")
