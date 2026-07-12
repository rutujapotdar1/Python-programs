days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
tempreatures = [32, 34, 31, 29, 35, 36, 33]
total_temp = 0
max_temp = tempreatures[0]
min_temp = tempreatures[0]
max_day = days[0]
min_day = days[0]
for i in range(len(days)):
    temp = tempreatures[i]
    total_temp += temp
    if temp > max_temp:
        max_temp = temp 
        max_day = days[i]
        if temp < min_temp:
            min_temp = temp
            min_day = days[i]
            average_temp = total_temp / len(days)
            print("---- Weekly Temperature Report ----")
            print(f"Average Temperature: {average_temp:.2f}C")
            print(f"Hottest Day: {max_day} ({max_temp}C)")
            print(f"Coolest Day: {min_day} ({min_temp}C)")