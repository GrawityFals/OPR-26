from typing import TypedDict
import requests
import json

class AgifyCall(TypedDict):
    name: str
    age: int
    count: int

def api_call(name: str) -> AgifyCall:
    with open("data.json", "r") as f:
        data: dict[str, AgifyCall] = json.load(f)
        if name in data:
            return data[name]

    url: str = "https://api.agify.io"
    params: dict[str, str] = {
        "name": name
    }

    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return response.json()
    

def save_data(new_data: AgifyCall) -> None:
    with open("data.json", "r") as f:
        data: dict[str, AgifyCall] = json.load(f)

    data = data | new_data
    print(data)

    with open("data.json", "w") as f:
        json.dump({data}, f, indent=4)
    

def main() -> None:
    # data: AgifyCall | None = api_call("maj")
    save_data({name: "maj", age: 67 count: 69})


if __name__ == "__main__":
    main()
