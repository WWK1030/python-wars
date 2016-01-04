# coding=UTF8

import requests

URL = "https://www.madailicai.com/p2p/service/"


def count_for_each(product_type, service_type):
    params = {"productType": product_type}
    result = requests.head(url=URL + service_type, params=params)
    return result.headers.get('X-Record-Count')


def list_of_each(start, size, product_type, service_type):
    params = {"from": start, "productType": product_type, "size": size}
    result = requests.get(url=URL + service_type, params=params)
    return result.json()


def count_for_car_loan():
    all_size = count_for_each("CAR_LOAN_REQUEST", "carLoans")
    sum_of_money = 0
    for each_page in range(0, int(all_size), 10):
        one_page = list_of_each(each_page, 10, "CAR_LOAN_REQUEST", "carLoans")
        for each_item in one_page:
            sum_of_money += each_item['currentInvestmentAmount']
        sum_of_money = sum_of_money
    return sum_of_money

print("融车宝: ", count_for_car_loan())


def count_for_loans():
    all_size = count_for_each("", "products")
    sum_of_money = 0
    for each_page in range(0, int(all_size), 10):
        one_page = list_of_each(each_page, 10, "", "products")
        for each_item in one_page:
            sum_of_money += each_item['currentInvestmentAmount']
        sum_of_money = sum_of_money
    return sum_of_money

print("腾信宝: ", count_for_loans())


def count_for_enterpriseLoans():
    all_size = count_for_each("ENTERPRISE_ACCOUNTS_RECEIVABLE", "enterpriseLoans")
    sum_of_money = 0
    for each_page in range(0, int(all_size), 10):
        one_page = list_of_each(each_page, 10, "ENTERPRISE_ACCOUNTS_RECEIVABLE", "enterpriseLoans")
        for each_item in one_page:
            sum_of_money += each_item['currentInvestmentAmount']
        sum_of_money = sum_of_money
    return sum_of_money

print("融企宝: ", count_for_enterpriseLoans())

all_money = count_for_loans() + count_for_car_loan() + count_for_enterpriseLoans()
print("总放款金额: ", all_money)
