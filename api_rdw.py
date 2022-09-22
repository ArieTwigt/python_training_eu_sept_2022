import requests
import pandas

selected_brand = input("Which brand?\n").upper()

endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand}"

response = requests.get(endpoint)
car_list = response.json()

df_cars = pandas.DataFrame(car_list)
df_cars = df_cars.fillna(0)
df_cars['catalogusprijs'] = df_cars['catalogusprijs'].astype(int)

# export as csv
file_name = f"export_{selected_brand}.csv"
df_cars.to_csv(file_name, sep=";")

print(f"🚗Exported: {file_name}")

# HTTP
# GET - retreive data
# PUT - update data
# POST - send (new) data
# DELETE = delete

# API

# Request always provides a response, even when it went wrong
# Response has a code
# 200 - Succesful response
#   # 201 - Redirection
# 400
#  403 - Unauthorized
#  404 - Not found
# 500
#   503 - Server
