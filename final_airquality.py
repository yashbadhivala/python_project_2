
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Load CSV', 'Explore', 'Repair NAs', 'Math demo', 'Visualize', 'Exit']

class AirqualityTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def loadit(self, path):
        if not os.path.exists(path):
            d=pd.date_range("2023-03-01", periods=150, freq="D")
            tmp=pd.DataFrame({
                "date":d,
                "city":np.random.choice(["Alpha","Beta","Gamma","Delta"], len(d)),
                "AQI":np.random.randint(35,320,len(d)),
                "PM25":np.random.uniform(5,180,len(d)),
                "PM10":np.random.uniform(10,230,len(d)),
                "Temp":np.random.uniform(10,40,len(d))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def drawit(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def wash(self):
        if self.df.empty: return
        for c in self.df.columns:
            if self.df[c].dtype.kind in "biufc": self.df[c].fillna(self.df[c].median(), inplace=True)
            else: self.df[c].fillna("Unknown", inplace=True)

    def quickstats(self):
        if self.df.empty: return
        print("AQI std:", round(float(self.df["AQI"].std()),2))

    def look(self):
        if self.df.empty: return
        plt.figure(); self.df.groupby("city")[["PM25","PM10"]].mean().plot(kind="bar"); plt.title("BAR view"); plt.tight_layout(); plt.savefig("airquality_03_bar.png"); plt.close()
        plt.figure(); sns.heatmap(self.df[["AQI","PM25","PM10","Temp"]].corr(), annot=True, cmap="magma"); plt.title("HEAT view 2"); plt.tight_layout(); plt.savefig("airquality_03_heat.png"); plt.close()

def main():
    app=AirqualityTool()
    while True:
        print("Student Lab -> 1:Load CSV 2:Explore 3:Repair NAs 4:Math demo 5:Visualize 6:Exit")
        c=input("opt: ").strip()
        if c=="1": app.loadit(input("path: ") or "airquality.csv"); print("ok")
        elif c=="2": app.drawit()
        elif c=="3": app.wash(); print("ok")
        elif c=="4": app.quickstats()
        elif c=="5": app.look(); print("ok")
        elif c=="6": break
        else: print("bad")

if __name__ == "__main__":
    main()
