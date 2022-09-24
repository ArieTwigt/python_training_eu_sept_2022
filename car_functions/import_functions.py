import requests

def import_car_by_brand(brand: str, color: str, cilinders: int=0) -> list:
    '''
    This function imports cars
    '''
    
    brand_upper = brand.upper()
    color_upper = color.upper()

    if cilinders == 0:
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}&eerste_kleur={color_upper}"
    else:
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}&eerste_kleur={color_upper}&aantal_cilinders={cilinders}"

    response = requests.get(endpoint)

    cars_list = response.json()
    return cars_list


if __name__ == '__main__':
    print("I am coming from the main")


