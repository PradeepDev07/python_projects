from datetime import datetime


date_format="%d-%m-%Y"
Category_dic={"I":"Income","E":"Expence"}



def getdate(prompt,allow_default=False):
    
    date_str= input(prompt)
    if allow_default and not date_str:
        return  datetime.today().strftime(date_format)
    try:
        valid_date=datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return getdate(prompt,allow_default)


def getamount():
    try:
        amount=float(input("Enter The Amount : "))
        if amount<=0:
            raise ValueError("Amount must be non-Zero non-Neg Value")
        return amount
    except ValueError as e:
        print(e)
        return getamount()

def getcategory():
    category=input("Enter category ('I' for Income or 'E' for Expence) : ").upper()
    if category in Category_dic:
        return Category_dic[category]
    print("Try again => Enter category ('I' for Income or 'E' for Expence) : ")
    return getcategory()

def getdiscription():
    discription = input("Enter Discription (optional) : ")
    if(not discription):
        return "none"
    return discription    


