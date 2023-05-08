import matplotlib.pyplot as plt
import pandas as pd

def main():
    food_data = pd.read_csv(r"data\01CN.csv")
    restaurant_data = pd.read_csv(r"data\11CN.csv")
    food_data = food_data.iloc[2:86]
    print(food_data)
    food_data = food_data.drop(food_data.iloc[:, 2:], axis=1)
    food_data["Food and non-alcoholic beverages"]=food_data["Food and non-alcoholic beverages"].str.replace(',', '')
    food_data["Food and non-alcoholic beverages"]=food_data["Food and non-alcoholic beverages"].astype(int)
    print(food_data.dtypes)
    food_data.plot(ylabel = "Money Spent (£)", x = "Time period and codes")
    plt.show()


if __name__ == "__main__":
    main()