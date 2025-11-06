max_temps = list()

ndays = int(input(f"Enter number of days: "))

for i in range(ndays):
    inp = input(f"Enter max temp of day {i+1}: ")
    max_temps.append(float(inp))
   
avg_temp =  sum(max_temps)/ndays
print(f"Average temperature : {avg_temp}")

days_more_than_avg = len([temp for temp in max_temps if temp > avg_temp])

print(f"{days_more_than_avg} day(s) more than average")