import pandas as pd  
import csv 
from datetime import datetime
from Data_Entry import getamount,getdate,getcategory,getdiscription
import matplotlib.pyplot as plt  

class CSV:
    File_name = "FinacialData.csv"
    column=["Date","Amount","Category","Description"]
    Format="%d-%m-%Y"

    @classmethod
    def init_csv(cls):
        try:
            pd.read_csv(cls.File_name)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.column)
            df.to_csv(cls.File_name,index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry={
            "Date" : date
            ,"Amount":amount
            ,"Category":category
            ,"Description":description
        }
        with open(cls.File_name,"a",newline="") as csvfile:
            writer= csv.DictWriter(csvfile,fieldnames=cls.column)
            writer.writerow(new_entry)
        print("Data Added")
    
    @classmethod
    def getTransactions(cls,start_date,end_date):
        df=pd.read_csv(CSV.File_name)
        df["Date"]= pd.to_datetime(df["Date"],format=CSV.Format)
        start_date=datetime.strptime(start_date,CSV.Format)
        end_date=datetime.strptime(end_date,CSV.Format)
        mask = (df["Date"]>=start_date)& (df["Date"]<=end_date)
        fliter_df = df.loc[mask].sort_values(by="Date")
        if fliter_df.empty :
            print("NOOO Transaction B/W This Dates ")
        else:
            print(
                f"Transtion B/W {start_date.strftime(CSV.Format)} to {end_date.strftime(CSV.Format)}"
            )    
            print(
                fliter_df.to_string(index=False,formatters={"Date": lambda x : x.strftime(CSV.Format)})
            )
            total_income= fliter_df[fliter_df["Category"] == "Income"]["Amount"].sum()
            total_expence= fliter_df[fliter_df["Category"] == "Expense"]["Amount"].sum()
            print("\nSummary: ")
            print(f"Total Income : rs {total_income:.2f}")
            print(f"Total Expence : rs {total_expence:.2f}")
            print(f"Net Worth : rs {(total_income-total_expence):.2f}")
            return fliter_df


def add():
    CSV.init_csv()
    date= getdate("Enter the date in (dd-mm-YYYY) or current date : ",allow_default=True)
    amount=getamount()
    category=getcategory()
    discription=getdiscription()
    CSV.add_entry(date,amount,category,discription)

def plot_transactions(df):
    print(df)
    df.set_index("Date",inplace=True)

    income_df=(
        df[df["Category"]=="Income"]
        .resample("D")
        .sum().
        reindex(df.index,fill_value=0)
    )
    expense_df=(
        df[df["Category"]=="Expense"]
        .resample("D")
        .sum().
        reindex(df.index,fill_value=0)
    )
    plt.figure(figsize=(10,5))
    plt.plot(income_df.index , income_df["Amount"],label="Income",color="g")
    plt.plot(expense_df.index , expense_df["Amount"],label="Expense",color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expences " )
    plt.legend()
    plt.grid()
    plt.show()


    







def main():
    while True:
        print("\n1. Add a New transaction")
        print("2. View transaction b/w date range")
        print("3. Exit")

        choice=int(input("Enter value 1 , 2 or 3 : "))

        if(choice==1):
            add()
        elif(choice==2):
            s=input("Enter Start date : ")
            e=input("Enter End date : ")
            df=CSV.getTransactions(s,e)
            print(df)
            a=input("want to see plot ? (y/n)").lower()
            if(a=="y"):
                plot_transactions(df)
        elif(choice==3):
            print("Exiting....")
            break
        else:
            print("Invalid Number Entered") 












if __name__ == "__main__":
    main()







# print("Enter 1 or 2")
# a=int(input())
# if(a==1):
#     add()
# elif(a==2):
#     s=input("Start date in dd-mm-yyyy : ")
#     e=input("End date in dd-mm-yyyy : ")   
#     CSV.getTransactions(s,e)

