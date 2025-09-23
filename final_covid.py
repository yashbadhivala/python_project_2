
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Open/Generate', 'Snapshot', 'Fix data', 'Numbers', 'Plot room', 'Stop']

class CovidTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def wash(self, path):
        if not os.path.exists(path):
            days=pd.date_range("2020-04-01", periods=120, freq="D")
            tmp=pd.DataFrame({
                "date":days,
                "country":np.random.choice(list("ABCD"), len(days)),
                "cases":np.random.randint(30,3000,len(days)),
                "deaths":np.random.randint(0,120,len(days)),
                "recovered":np.random.randint(10,2500,len(days))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def quickstats(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def look(self):
        if self.df.empty: return
        self.df = self.df.drop_duplicates();
        self.df.fillna(method="ffill", inplace=True)

    def loadit(self):
        if self.df.empty: return
        print("peak cases:", int(self.df["cases"].max())); print("mean deaths:", round(float(self.df["deaths"].mean()),2))

    def drawit(self):
        if self.df.empty: return
        plt.figure(); self.df["cases"].plot(kind="hist", bins=20); plt.title("HIST view"); plt.tight_layout(); plt.savefig("covid_03_hist.png"); plt.close()
        plt.figure(); self.df.set_index("date")[["cases","recovered"]].plot(kind="area", alpha=0.5); plt.title("AREA view 2"); plt.tight_layout(); plt.savefig("covid_03_area.png"); plt.close()

def main():
    app=CovidTool()
    while True:
        print("Mini Studio -> 1:Open/Generate 2:Snapshot 3:Fix data 4:Numbers 5:Plot room 6:Stop")
        c=input("opt: ").strip()
        if c=="1": app.wash(input("path: ") or "covid.csv"); print("ok")
        elif c=="2": app.quickstats()
        elif c=="3": app.look(); print("ok")
        elif c=="4": app.loadit()
        elif c=="5": app.drawit(); print("ok")
        elif c=="6": break
        else: print("bad")

if __name__ == "__main__":
    main()
