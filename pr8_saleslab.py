# Pandas Analyzer & Visualization – variant 3
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesLab:
    def __init__(self):
        self.data = pd.DataFrame()

    def __del__(self):
        pass

    def read_csvfile(self, file_path):
        if not os.path.exists(file_path):
            # create a tiny synthetic dataset if file missing
            df = pd.DataFrame({
                "Date": pd.date_range("2022-01-01", periods=12, freq="M"),
                "Product": ["A","B","C","D"]*3,
                "Region": ["North","South","East","West"]*3,
                "Sales": np.random.randint(200,1000,12),
                "Profit": np.random.randint(20,200,12),
                "Year": [2022,2023,2024]*4[:12]
            })
            df.to_csv(file_path, index=False)
        self.data = pd.read_csv(file_path, parse_dates=["Date"])

    def info_view(self):
        if self.data.empty:
            print("No data."); return
        print(self.data.head())
        print(self.data.tail())
        print("Columns:", list(self.data.columns))
        print(self.data.dtypes)
        print(self.data.describe())

    def fix_missing(self):
        if self.data.empty: return
        self.data = self.data.drop_duplicates()
        for col in self.data.select_dtypes(include=["object"]).columns:
            self.data[col] = self.data[col].fillna(self.data[col].mode().iloc[0] if not self.data[col].mode().empty else "NA")
        for col in self.data.select_dtypes(include=[np.number]).columns:
            self.data[col] = self.data[col].fillna(self.data[col].mean())

    def maths(self):
        if self.data.empty: return
        arr = self.data["Sales"].to_numpy()
        # numpy indexing & slicing demo
        first_five = arr[:5]
        doubled = arr * 2
        print("First 5:", first_five)
        print("Doubled sample:", doubled[:5])
        return first_five.sum()

    def joinit(self, other_df):
        if self.data.empty: return
        return pd.concat([self.data, other_df], ignore_index=True)

    def sliceit(self, by_col="Region"):
        if self.data.empty: return {}
        groups = {}
        for key, sub in self.data.groupby(by_col):
            groups[key] = sub.copy()
        return groups

    def find_sort_filter(self, keyword="A", sort_by="Sales", min_val=0):
        if self.data.empty: return pd.DataFrame()
        df = self.data[self.data["Product"].astype(str).str.contains(str(keyword), case=False, na=False)]
        df = df[df[sort_by] >= min_val].sort_values(by=sort_by, ascending=False)
        return df

    def agg(self):
        if self.data.empty: return pd.DataFrame()
        return self.data.groupby("Region")[["Sales","Profit"]].agg(["sum","mean","count"])

    def stats(self):
        if self.data.empty: return {}
        return {
            "std_Sales": float(self.data["Sales"].std()),
            "var_Profit": float(self.data["Profit"].var()),
            "quantile_25": float(self.data["Sales"].quantile(0.25))
        }

    def pivotize(self):
        if self.data.empty: return pd.DataFrame()
        return pd.pivot_table(self.data, values="Sales", index="Product", columns="Region", aggfunc="sum", fill_value=0)

    def plots(self):
        if self.data.empty: return
        plt.figure()
        self.data.groupby("Product")["Sales"].sum().plot(kind="bar")
        plt.title("Total Sales by Product"); plt.xlabel("Product"); plt.ylabel("Sales")
        plt.savefig("plot_bar_3.png"); plt.close()

        plt.figure()
        self.data.plot(kind="scatter", x="Sales", y="Sales")
        plt.title("Scatter"); plt.savefig("plot_scatter_3.png"); plt.close()

        plt.figure()
        sns.boxplot(data=self.data[["Sales","Profit"]]); plt.title("Box Plot")
        plt.savefig("plot_box_3.png"); plt.close()

def menu():
    print("\n========== Data Analysis & Visualization ==========")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Clean Data")
    print("4. Numpy/Math Quick Demo")
    print("5. Aggregations")
    print("6. Statistics")
    print("7. Pivot Table")
    print("8. Visualize")
    print("9. Exit")
    print("==================================================")

def main():
    tool = SalesLab()
    while True:
        menu()
        ch = input("Enter: ").strip()
        if ch == "1":
            path = input("CSV path (or new path to auto-generate): ") or "sales_3.csv"
            tool.read_csvfile(path); print("Loaded.")
        elif ch == "2":
            tool.info_view()
        elif ch == "3":
            tool.fix_missing(); print("Cleaned.")
        elif ch == "4":
            print("Sum of first five (demo):", tool.maths())
        elif ch == "5":
            print(tool.agg())
        elif ch == "6":
            print(tool.stats())
        elif ch == "7":
            print(tool.pivotize())
        elif ch == "8":
            tool.plots(); print("Saved plots.")
        elif ch == "9":
            print("Bye"); break
        else:
            print("Invalid")
if __name__ == "__main__":
    main()
