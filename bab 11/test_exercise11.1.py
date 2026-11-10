from exercise11_1_function import city_country

def test_city_country():
    citycountry = city_country('Jakarta', 'Indonesia')
    assert citycountry == 'Jakarta , Indonesia'