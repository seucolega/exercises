"""
Currency Exchange on Exercism's Python Track
"""

import math


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Estimate value after exchange

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: int) -> float:
    """Calculate currency left after an exchange

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate value of bills

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Calculate number of bills

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return math.floor(budget / denomination)


def exchangeable_value(
        budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculate value after exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    return (
            get_number_of_bills(
                exchange_money(
                    budget,
                    exchange_rate_plus_the_spread(exchange_rate, spread)
                ),
                denomination,
            )
            * denomination
    )


def non_exchangeable_value(
        budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculate non-exchangeable value

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    return math.floor(
        exchange_money(
            budget, exchange_rate_plus_the_spread(exchange_rate, spread)
        )
        % denomination
    )


def exchange_rate_plus_the_spread(exchange_rate: float, spread: int) -> float:
    """calculating the exchange rate plus the spread

    :param exchange_rate:
    :param spread:
    :return: float exchange rate plus the spread.
    """

    return exchange_rate * (1 + spread / 100)
