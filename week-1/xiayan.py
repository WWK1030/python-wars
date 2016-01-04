# -*- coding: utf-8 -*-

import requests

CAR_LOAN_URL = "https://www.madailicai.com/p2p/service/carLoans"
ENTERPRISE_LOAN_URL = "https://www.madailicai.com/p2p/service/enterpriseLoans"
TENG_LOAN_URL = "https://www.madailicai.com/p2p/service/products"


def count_for_loan(url: str):
    result = requests.head(url=url)
    return result.headers.get('X-Record-Count')


def list_of_loan(url, start, size):
    params = {"from": start, "size": size, "productType": "CAR_LOAN_REQUEST"}
    result = requests.get(url=url, params=params)
    return result.json()


def sum_of_loan(url: str):
    count_loan = int(count_for_loan(url))
    i, sum_of__money = 0, 0
    while i <= count_loan:
        all_car_loan = list_of_loan(url, i, 10)
        i += 10
        for car_loan in all_car_loan:
            sum_of__money += car_loan['currentInvestmentAmount']
    return sum_of__money


sum_of_car = sum_of_loan(CAR_LOAN_URL)
print('car loan %s' % sum_of_car)

sum_of_enterprise = sum_of_loan(ENTERPRISE_LOAN_URL)
print('enterprise loan %s' % sum_of_enterprise)

sum_of_teng = sum_of_loan(TENG_LOAN_URL)
print('tengxin %s' % sum_of_teng)
