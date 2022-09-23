import requests
import pandas
import os

def import_cars(brand: str, color: str):
    brand_upper = brand.upper()
    color_upper = color.upper()
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}&eerste_kleur={color_upper}"
    response = requests.get(endpoint)
    cars_list = response.json()
    
    if len(cars_list) == 0:
        print("Warning: No cars")

    return cars_list


def export_cars_to_file(cars_list, file_name, folder):
    cars_df = pandas.DataFrame(cars_list)

    file_folder_path = f"{folder}/{file_name}"
    
    files_folders = os.listdir()

    if folder not in files_folders:
        os.mkdir(folder)

    cars_df.to_csv(file_folder_path)


# os.makedirs() --> create sub-folders immediately
