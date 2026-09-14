import requests
from typing import Any


def slovarji_test() -> None:
    # slovarji (dict)
    my_dict: dict[str, str] = {
        "key": "value",
        "key2": "value2",
    }
    
    print(my_dict)
    print(my_dict["key"])

    # raznoliki slovar
    razno: {str, Any} = {
        "število": 6,
        "ime": "Cl9dy",
        "sezam": [1, 2, 3, 4],
        "slovar": {
            "firma": "honda",
            "moč": 9001,
        }
    }

    print(razno["število"])
    print(max(razno))
    print(razno["slovar"])
    print(razno["slovar"]["firma"], razno["slovar"]["moč"], "kw")


def call_api() -> dict | None:
    url: str = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=rain_sum&timezone=auto&forecast_days=1"
    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()

    raise f"Status Code {response.status_code}"


def main() -> None:
    response: dict | None = call_api()
    print(response)

if __name__ == "__main__":
    main()
