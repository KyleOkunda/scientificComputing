import matplotlib.pyplot as plt

days = ["Sun","Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
temp = [20, 22, 19, 23, 21, 24, 20]

plt.plot(days, temp, marker = "o", linestyle = "-", color = "blue" )

plt.title("Daily Temp Values for a week")
plt.xlabel("Days of the week")
plt.ylabel("Temp Values")
plt.grid(True)

plt.show()