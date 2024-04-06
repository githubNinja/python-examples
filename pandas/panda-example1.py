import pandas as pd

super_store = pd.DataFrame()
print("type ::{}".format(type(super_store)))
order_list = ["WOW23891", "WOW23892", "WOW2384922", "WOW54391"]
category_list = ['Office Supplies', 'Technology', 'Dummy', 'Dummy']
super_store['OrderId'] = order_list
super_store['category'] = category_list

print(format(super_store))

read_data_csv = pd.read_csv("../data/data-file.csv")
print(read_data_csv.head())
dataFrame = pd.DataFrame(read_data_csv, columns=['objectname', 'livetuples', 'deadtuples'])
print("head::{}".format(dataFrame.head()))
print("tail::{}".format(dataFrame.tail()))

for col in dataFrame.columns[0:3]:
    #if col["objectname"] == 'miscellaneousinformation':
     #   print("Data:{}".format(col))
    print("Data:{}".format(dataFrame[col][0:2]))

 #Slice rows


# colName = dataFrame[col]
# print("Data:{}".format(colName.values))
# print("colName:{}".format(colName))

# for data in read_data_csv.columns:
#     if data == "objectname":
#         pd.DataFrame
#         print("Data:{}".format(data))
#     else:
#         print("Object not found")
