import matplotlib.pyplot as plt
import pandas as pd

def main():
    xValues = []

    food_data = pd.read_csv(r"data\01CN.csv")
    restaurant_data = pd.read_csv(r"data\11CN.csv")
    food_data = food_data.iloc[2:86]
    food_data = food_data.drop(food_data.iloc[:, 2:], axis=1)
    food_data["Food and non-alcoholic beverages"]=food_data["Food and non-alcoholic beverages"].str.replace(',', '')
    food_data["Food and non-alcoholic beverages"]=food_data["Food and non-alcoholic beverages"].astype(int)
    
    for i in range(1, len(food_data["Time period and codes"]) + 1):
        xValues.append(i)

    plt.plot(food_data["Time period and codes"], food_data["Food and non-alcoholic beverages"], label="Food and non-alcoholic beverages")
    plt.xlabel("Time period and codes")
    plt.ylabel("Money Spent (£)")
    plt.title("Money Spent Compared To Time Period")
    plt.legend(loc="upper right")
    plt.xticks(xValues, food_data["Time period and codes"], rotation="vertical")
    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()


if __name__ == "__main__":
    main()