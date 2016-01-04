# -*- coding: utf-8 -*-

import requests

CAR_LOAN_URL = "https://www.madailicai.com/p2p/service/carLoans"
ENTERPRISE_LOAN_URL = "https://www.madailicai.com/p2p/service/enterpriseLoans"
TENG_LOAN_URL = "https://www.madailicai.com/p2p/service/products"


def count_for_loan(url: str):
    result = requests.head(url=url)
    return result.headers.get('X-Record-Count')


def list_of_car_loan(url, start, size):
    params = {"from": start, "size": size}
    result = requests.get(url=url, params=params)
    return result.json()


def sum_of_loan(url: str):
    count_car_loan = int(count_for_loan(url))
    i, sum_of_car_money = 0, 0
    while i <= count_car_loan - 10:
        all_car_loan = list_of_car_loan(url, i, 10)
        i += 10
        for car_loan in all_car_loan:
            sum_of_car_money += car_loan['currentInvestmentAmount']
    return sum_of_car_money


sum_of_teng = sum_of_loan(TENG_LOAN_URL)
sum_of_car = sum_of_loan(CAR_LOAN_URL)
sum_of_enterprise = sum_of_loan(ENTERPRISE_LOAN_URL)

print('car loan %s, enterprise loan %s, tengxin %s' % (sum_of_car, sum_of_enterprise, sum_of_teng))
