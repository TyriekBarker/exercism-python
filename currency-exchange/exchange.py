def exchange_money(budget:float, exchange_rate:float):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    exchanged_money = budget / exchange_rate

    return exchanged_money


def get_change(budget:float, exchanging_value:float):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    remaining_budget = budget - exchanging_value

    return remaining_budget


def get_value_of_bills(denomination:int, number_of_bills:int):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    total_value = denomination * number_of_bills

    return total_value


def get_number_of_bills(budget:float, denomination:int):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    total_bills = budget // denomination

    return total_bills


def get_leftover_of_bills(budget:float, denomination:int):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    leftover_bills = budget % denomination
    
    return leftover_bills


def exchangeable_value(budget:float, exchange_rate:float, spread:int, denomination:int):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    exchange_fee_percentage = spread / 100
    exchanged_budget = budget / (exchange_rate+(exchange_rate*exchange_fee_percentage))
    return int(exchanged_budget-(exchanged_budget % denomination))

