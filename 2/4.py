import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dt = pd.read_csv("company_sales_data.csv", sep=',')

ox = dt['month_number']
oy = dt['total_profit']

#1
plt.plot(ox,oy)
plt.xlabel('Month number')
plt.ylabel('Total profit')
plt.title('Company profit per month')
plt.xticks(ox)
plt.show()


#2
oy = dt['total_units']
plt.plot(ox,oy,'--o', lw = 3, color="Red", markerfacecolor = "Black", label="Profit data of last year")
plt.title('Company sales data of last year')
plt.xticks(ox)
plt.legend(loc="lower right")
plt.show()


#3.1
# for column in dt.columns:
#     if "total" in column or "month" in column: continue
#     oy = dt[column]
#     plt.plot(ox,oy,'-o',label=column)
# plt.title("Sales data")
# plt.xlabel("Month number")
# plt.ylabel("Sales unit in month")
# plt.xticks(ox)
# plt.legend()
# plt.show()

#3.2

# fig, ax = plt.subplots(nrows=3, ncols= 2, sharex=True)
#
# i = 0
# for column in dt.columns:
#     if "total" in column or "month" in column: continue
#     oy = dt[column]
#     ax[i%3,i%2].plot(ox, oy, '-o', c=np.random.rand(3,))
#     ax[i%3,i%2].set_title(oy.name)
#     i += 1
# ax[1,0].set_ylabel("Sales units in number")
# ax[2, 0].set_xlabel("Month number")
# ax[2,1].set_xlabel("Month number")
# plt.show()

#4
# ox = dt['month_number']
# oy = dt['total_profit']
#
# oy = dt['toothpaste']
# plt.scatter(ox, oy)
# plt.grid(True, linestyle='--')
# plt.title("Tooth paste Sales data")
# plt.ylabel("Number of units Sold")
# plt.xlabel("Month Number")
# plt.xticks(ox)
# plt.legend(['toothpaste'])
#
# plt.show()


#5

# oyFaceCream = dt['facecream']
# oyFaceWash = dt['facewash']
# barWidth = 0.25
#
# br1 = np.arange(len(oyFaceCream))
# br2 = [x + barWidth for x in br1]
#
# plt.bar(br1, oyFaceCream, color='b', width=barWidth, label='facecream')
# plt.bar(br2, oyFaceWash, color='orange', width=barWidth, label='facewash')
#
# plt.grid(True, linestyle='--')
# plt.title("Facewash and facecream Sales data")
# plt.ylabel("Sales units in number")
# plt.xlabel("Month Number")
# plt.xticks([r + barWidth for r in range(len(ox))],ox)
#
# plt.legend(loc='upper left')
# plt.show()

#6
#
# dts = dt.sum()
# labels = dt.columns.tolist()[1:-2]
# amounts = np.int_([x for x in dts[1:-2]])
#
# fig, ax = plt.subplots(figsize=(6,2), subplot_kw=dict(aspect='equal'))
#
# def funct(pct):
#     return f"{pct:.1f}%"
#
# wedges, texts, autotexts = ax.pie(amounts, labels = labels, autopct=lambda pct: funct(pct), textprops=dict(color="black"))
#
# ax.set_title("Sales data")
# ax.legend(labels, loc = "lower right")
# plt.setp(autotexts, size = 8, weight = 'bold')
# plt.show()

#7

# dt_amounts = []
# for column in dt.columns:
#     if "total" in column or "month" in column: continue
#     ar = []
#     for i in range(12):
#         ar.append(dt.loc[i, column])
#     dt_amounts.append(np.int_(ar))
#
# oy = np.vstack([x for x in dt_amounts])
#
# fig, ax = plt.subplots()
# ax.stackplot(ox, oy)
# ax.set_ylabel('Sales units in Number')
# ax.set_xlabel('Month Number')
# ax.set_title('All product sales data using stack plot')
# plt.legend(dt.columns[1:-2], loc='upper left')
# plt.show()


#8
# plt.figure(figsize=(10, 6))
#
# ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=3)
#
# ax2 = plt.subplot2grid((2, 3), (1, 0))
# ax3 = plt.subplot2grid((2, 3), (1, 1))
# ax4 = plt.subplot2grid((2, 3), (1, 2))
#
# plt.show()