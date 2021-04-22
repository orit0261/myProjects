import matplotlib.dates as mdates
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(date, price , label="Price")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))