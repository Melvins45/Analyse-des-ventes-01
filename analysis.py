# NITOPOP JEATSA GUILLAUME MELVIN 20S43003

import pandas as pd

def getNumberSales(name_product) :
    total_sales = 0
    for index, row in df.iterrows():
        if row["Product_Category"] == name_product :
            total_sales += row['Quantity_Sold']
    
    return total_sales

def getNumberSalesPerSeason(name_product, listSeason) :
    total_sales = 0
    for index, row in df.iterrows():
        if row["Product_Category"] == name_product and str(row['Sale_Date']).split("-")[1] in listSeason :
            total_sales += row['Quantity_Sold']
    
    return total_sales

def getComportmentPerProduct(name_product) :
    total_sales_returning = 0
    total_sales_new = 0
    for index, row in df.iterrows():
        if row["Product_Category"] == name_product :
            if row['Customer_Type'] == "Returning" :
                total_sales_returning += row['Quantity_Sold']
            else :
                total_sales_new += row['Quantity_Sold']
    
    return [f"Returning : {total_sales_returning}", f"New : {total_sales_new}"]

df = pd.read_csv('sales_data.csv')
seasons = [["01", "02", "03"], ["04", "05", "06"], ["07", "08", "09"], ["10", "11", "12"]]

id = lambda column : [ind for ind in range(len(df.columns)) if df.columns[ind]== column][0]

product_types = list(set(df["Product_Category"]))
customer_types = list(set(df["Customer_Type"]))

print(  customer_types )

insight = sorted([ [name_product, getNumberSales(name_product) ] for name_product in product_types ], key = lambda x : x[1], reverse=True )
print ('Présentons un insight sur la performance : ', insight , "\n")

tendance = lambda listSeason : sorted([ [name_product, getNumberSalesPerSeason(name_product, listSeason) ] for name_product in product_types ], key = lambda x : x[1], reverse=True )

tendancies = [ { str(season) : tendance(season)} for season in seasons ]

print ('Présentons les tendances saisonnières : ', tendancies , "\n")

comportments = [ [name_product, getComportmentPerProduct(name_product) ] for name_product in product_types ]
print ('Présentons les comportements des clients : ', comportments)