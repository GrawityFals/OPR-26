import requests
from typing import Any, TypedDict


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

class CurrentUnits(TypedDict):
    time: str
    interval: str
    temperature_2m: str

class Current(TypedDict):
    time: str
    interval: int
    temperature_2m: float

class DailyUnits(TypedDict):
    time: str
    temperature_2m_max: str
    temperature_2m_min: str


class Daily(TypedDict):
    time: list[str]
    temperature_2m_max: list[float]
    temperature_2m_min: list[float]


class OpenMetroResponse(TypedDict):
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: float
    current_units: Current
    current: Current
    daily_units: DailyUnits
    daily: Daily


def call_api() -> OpenMetroResponse | None:
    url: str = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min&current=temperature_2m&timezone=auto"
    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()

    raise "Status Code wasn't 200"


def main() -> None:
    try:
        response: OpenMetroResponse | None = call_api()

        print("Trenutna temperatura: ")
        print(
            response["current"]["temperature_2m"],
            response["current_units"]["temperature_2m"]
        )

        print("Temperatura naslednjih 7 dni: ")
        for i in range(7):
            print(
                response["daily"]["temperature_2m_max"][i],
                response["daily_units"]["temperature_2m_max"]
            )

        print("Najtoplejši dan: ")
        max_temp: float = max(response["daily"]["temperature_2m_max"])
        hotest_day_idx: int = response["daily"]["temperature_2m_max"].index(max_temp)
        print(
            f"{hotest_day_idx+1}. dan",
            response["daily"]["temperature_2m_max"][hotest_day_idx],
            response["daily_units"]["temperature_2m_max"],
            response["daily"]["time"][hotest_day_idx]
        )

        print("Največja razlika: ")
        for i in range(len(response["daily"]["temperature_2m_max"])):
            pass

        print(
            f"{hotest_day_idx+1}. dan",
            response["daily"]["temperature_2m_max"][hotest_day_idx],
            response["daily_units"]["temperature_2m_max"],
            response["daily"]["time"][hotest_day_idx]
        )
        
    except "Status Code wasn't 200":
        ...

if __name__ == "__main__":
    main()
