def main():
    # weeks = int(input("How many weeks of data do you want to input?"))
    # data = input("Week data separated by commas with no spaces")
    # data = data.split(',')
    # if len(data) != weeks:
    #     print("Incorrect data entry")
    #     return
    growth_rate = int(input("Enter growth rate: "))
    growth_rate_acceleration = float(input("Enter growth rate acceleration: "))
    base = int(input("Enter the last 90 days watch time: "))
    last_year_avg = int(input("Enter last years avg watch time: "))
    target_watch_time = int(input("Enter target watch time: "))

    base = base / 90
    last_year_avg = last_year_avg / 365

    print("This calculator assumes a constant growth rate that never changes.")
    print("This is unrealistic and so the results must be treated as general estimates.")
    print()
    target_daily_avg = target_watch_time / 365
    print("Looking for a target daily average watch time of: " + str(target_daily_avg))
    print()

    i = 0  # Weeks
    while True:
        print("Week " + str(i))
        min_week = i - 52
        new_growth_rate = growth_rate + (i * growth_rate_acceleration)
        if min_week < 0:
            ratio_last_year = 52 - i
            min = ((last_year_avg * ratio_last_year) + (base * i)) / 52
        else:
            min = base + (min_week * new_growth_rate)
        max = base + (i * new_growth_rate)
        daily_avg = (min + max) / 2
        yearly_watch_time = daily_avg * 365
        print("Daily average: " + str(daily_avg))
        print("Last 365 days from this week total watch time: " + str(yearly_watch_time))
        print()
        if yearly_watch_time > target_watch_time:
            break

        if i > 1024:
            print("Unable to determine a result")
            return

        i += 1

    print("Target watch time achieved for the previous 365 days from week " + str(i))


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
