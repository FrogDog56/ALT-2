import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def clean_up(data, column):
    data = data.iloc[42:86]
    data = data.drop(data.iloc[:, 2:], axis=1)
    data[column]=data[column].str.replace(",", "")
    data[column]=data[column].astype(int)
    return data

def sum_of_medians(data1, data2, data3, col1, col2, col3):
    col1 = data1[col1]
    col2 = data2[col2]
    col3 = data3[col3]
    res = col1.groupby(np.arange(len(col1))).median() + col2.groupby(np.arange(len(col2))).median() + col3.groupby(np.arange(len(col3))).median()
    return res

def main():
    food_data = pd.read_csv(r"data\01CN.csv")
    restaurant_data = pd.read_csv(r"data\11CN.csv")
    clothing_data = pd.read_csv(r"data\03CN.csv")
    food_data = clean_up(food_data, "Food and non-alcoholic beverages")
    restaurant_data = clean_up(restaurant_data, "Restaurant and hotels")
    clothing_data = clean_up(clothing_data, "Clothing and footwear")
    median = sum_of_medians(food_data, restaurant_data, clothing_data, "Food and non-alcoholic beverages", "Restaurant and hotels", "Clothing and footwear")

    display = input("Which graph do you want to display? (1. Main), (2. Medians)\n")

    if display == "1":
        plt.plot(food_data["Time period and codes"], food_data["Food and non-alcoholic beverages"], label="Food and non-alcoholic beverages")
        plt.plot(food_data["Time period and codes"], restaurant_data["Restaurant and hotels"], label="Restaurants and hotels")
        plt.plot(food_data["Time period and codes"], clothing_data["Clothing and footwear"], label="Clothing and footwear")
        plt.title("Money Spent Compared To Time Period")

    if display == "2":
        plt.plot(food_data["Time period and codes"], median, label = "Median Expenditure")
        plt.title("Money Spent Compared To Time Period (Median)")

    plt.xlabel("Time period and codes")
    plt.ylabel("Money Spent (£M)")
    plt.legend(loc="upper right")
    plt.xticks(rotation="vertical")
    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()
    
if __name__ == "__main__":
    main()