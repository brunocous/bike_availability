import requests
from bs4 import BeautifulSoup
from typing import NamedTuple, List


class Bike(NamedTuple):
    name: str
    link: str

    def __str__(self) -> str:
        return f"\n{self.name}\n{self.link}\n"


class BikeRequirements(NamedTuple):
    bike_size: str
    models_of_interest: List[str]
    classes_of_interest: List[str]

    def fulfils(self, bike: Bike) -> bool:
        reqs_to_check = (self.models_of_interest, self.classes_of_interest)
        return all(
            any(rr in bike.name.lower() for rr in r) for r in reqs_to_check
        )

    def __str__(self) -> str:
        return f"Bike Requirements:\n\tbike size: {self.bike_size}\n\tmodels of interest: {self.models_of_interest}\n\tclasses of interest: {self.classes_of_interest}\n\n"


def get_in_stock_road_bikes(requirements: BikeRequirements) -> List[Bike]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }

    url = f"https://www.canyon.com/nl-be/buying-tools/in-stock-bikes/?cgid=instockbikes&prefn1=expressBikeAvailable&prefn2=pc_rahmengroesse&prefn3=pc_welt&prefn4=refinementAvailability&prefv1=true&prefv2={requirements.bike_size}&prefv3=Road&prefv4=Op%20voorraad&srule=bestsellers"

    bikes_in_stock = requests.get(url, headers=headers).text

    soup = BeautifulSoup(bikes_in_stock, "html.parser")
    product_tiles = soup.find_all(attrs="productTile__contentWrapper")
    a_css_tags = [tile.find("a") for tile in product_tiles]

    bikes = [Bike(name=at["title"], link=at["href"]) for at in a_css_tags]

    return [bike for bike in bikes if bike_requirements.fulfils(bike)]


def pretty_print_in_stock_bikes(
    good_bikes: List[Bike], bike_requirements: BikeRequirements
) -> None:
    print(bike_requirements)
    if good_bikes:
        print("Following bikes fulfilling requirements are in stock")

        for b in good_bikes:
            print("---------")
            print(b)
    else:
        print("No bikes in stock at this moment fulfilling these requirements")


if __name__ == "__main__":
    # Fill this in:
    bike_requirements = BikeRequirements(
        bike_size="M",
        models_of_interest=["ultimate", "aeroad", "inflite"],
        classes_of_interest=["cf", "cfr"],
    )
    good_bikes = get_in_stock_road_bikes(requirements=bike_requirements)
    pretty_print_in_stock_bikes(
        good_bikes=good_bikes, bike_requirements=bike_requirements
    )

