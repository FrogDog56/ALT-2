import matplotlib.pyplot as plt
import pandas as pd

def clean_up(data, column):
    data = data.iloc[2:86]
    data = data.drop(data.iloc[:, 2:], axis=1)
    data[column]=data[column].str.replace(",", "")
    data[column]=data[column].astype(int)
    return data

def main():
    xValues = []

    food_data = pd.read_csv(r"data\01CN.csv")
    restaurant_data = pd.read_csv(r"data\11CN.csv")
    clothing_data = pd.read_csv(r"data\03CN.csv")
    food_data = clean_up(food_data, "Food and non-alcoholic beverages")
    restaurant_data = clean_up(restaurant_data, "Restaurant and hotels")
    clothing_data = clean_up(clothing_data, "Clothing and footwear")

    for i in range(1, len(food_data["Time period and codes"]) + 1):
        xValues.append(i)

    plt.plot(food_data["Time period and codes"], food_data["Food and non-alcoholic beverages"], label="Food and non-alcoholic beverages")
    plt.plot(food_data["Time period and codes"], restaurant_data["Restaurant and hotels"], label="Restaurants and hotels")
    plt.plot(food_data["Time period and codes"], clothing_data["Clothing and footwear"], label="Clothing and footwear")
    plt.xlabel("Time period and codes")
    plt.ylabel("Money Spent (£)")
    plt.title("Money Spent Compared To Time Period")
    plt.legend(loc="upper right")
    plt.xticks(xValues, food_data["Time period and codes"], rotation="vertical")
    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()


if __name__ == "__main__":
    main()