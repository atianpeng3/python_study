import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高气温和最低气温
filrname = r"下载数据/death_valley_2014.csv"
with open(filrname) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    for index, column_header in enumerate(head_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], r"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)      # alpha指定颜色的透明度，0表示完全透明，1表示完全不透明
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # 设置图形的格式
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=14)
    plt.xlabel("", fontsize=10)
    fig.autofmt_xdate()         # 绘制斜的日期标签，以免彼此重叠
    plt.ylabel("Temperature (F)", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()
