from re import findall


class Phone(object):
    def __init__(self, phone_number: str):
        phone_number = "".join(findall("\\d+", phone_number))

        if len(phone_number) > 10 and phone_number[:-10] != '1':
            raise ValueError("A very specific bad thing happened.")

        phone_number = phone_number[-10:]
        self.area_code = phone_number[:3]
        self.exchange_code = phone_number[3:6]
        self.subscriber_number = phone_number[6:]

        if [digit for digit in [self.area_code[0], self.exchange_code[0]] if digit in ['0', '1']]:
            raise ValueError("A very specific bad thing happened.")

    @property
    def number(self) -> str:
        return self.area_code + self.exchange_code + self.subscriber_number

    def pretty(self) -> str:
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}"
