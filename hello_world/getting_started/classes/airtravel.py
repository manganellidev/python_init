class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passanger):
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passanger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def relocate_passanger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passanger to relocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(
            sum(1 for s in row.values() if s is None)
            for row in self._seating
            if row is not None
        )

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passengers seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")


class Aircraft:
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return (range(1, 23), "ABCDEF")


class Boeing777(Aircraft):
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return (range(1, 56), "ABCDEFGHJK")


def make_flights():
    f = Flight("SN090", AirbusA319("G-EUPT"))
    f.allocate_seat("10A", "Wagner")
    f.allocate_seat("10B", "Anaysa")
    f.allocate_seat("5D", "João")
    f.allocate_seat("5E", "José")
    f.allocate_seat("15C", "Maria")
    f.allocate_seat("15F", "Rita")

    g = Flight("FF440", Boeing777("B-USGB"))
    g.allocate_seat("10A", "Wagner")
    # g.allocate_seat("10B", "Anaysa")
    # g.allocate_seat("50D", "João")
    # g.allocate_seat("50E", "José")
    # g.allocate_seat("15C", "Maria")
    # g.allocate_seat("15F", "Rita")

    return f, g


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = (
        f"| Name: {passenger}"
        f"  Flight: {flight_number}"
        f"  Seat: {seat}"
        f"  Aircraft: {aircraft}"
        " |"
    )
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def console2_card_printer(passenger, seat, flight_number, aircraft):
    output = (
        f"| Name: {passenger}"
        f"  Flight: {flight_number}"
        f"  Seat: {seat}"
        f"  Aircraft: {aircraft}"
        " |"
    )
    banner = "*" * (len(output))
    border = "*" + " " * (len(output) - 2) + "*"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()
