from getting_started.classes.airtravel import (
    console2_card_printer,
    make_flights,
    console_card_printer,
)
from pprint import pprint as pp


def main():
    f, g = make_flights()
    # pp(f._seating)
    # f.make_boarding_cards(console_card_printer)

    print(f.aircraft_model())
    print(g.aircraft_model())
    print(f.num_available_seats())
    print(g.num_available_seats())

    # g.make_boarding_cards(console_card_printer)
    g.relocate_passanger("10A", "20A")
    g.make_boarding_cards(console_card_printer)
    g.make_boarding_cards(console2_card_printer)


if __name__ == "__main__":
    main()
