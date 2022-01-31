from behave import given, when, then
import json, requests
from cerberus import Validator
import urllib


# Endpoints:
# /currencies
# A.Lists all the available currencies in prettified json format:
endpoint_a = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json'
# B.Get the currency list with EUR as base currency:
endpoint_b = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json'
# C.Get the currency value for EUR to JPY:
endpoint_c = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/jpy.json'
# D.Get the currency value for EUR to XYZ:
endpoint_d = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/xyz.json'
# E.Get the currency value for EUR to USD:
endpoint_e = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/usd.json'
# F.Get the currency value BaseURI
endpoint_baseuri = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/'



currency_count = 0
test_result = []
test_result_dict = {}
test_result.clear()
test_result_dict.clear()

# Return Dynamic Endpoint
def currency_endpoint(base,to=''):
    if to != '':
        return f"{endpoint_baseuri}{base}/{to}.json"
    return f"{endpoint_baseuri}{base}.json"

# Get Endpoint
def get_endpoint(endpoint):
    url = requests.get(endpoint)
    text = url.text
    return json.loads(text)



@given('I am an authorized user')
def authorized_user(context):
    # Init test scenario
    global test_result
    global currency_count
    test_result.clear()
    currency_count = 0
    test_result_dict.clear()

@when('I test all Endpoints')
def test_all_endpoints(context):
    global test_result
    endpoint_to_test = {endpoint_a,endpoint_b,endpoint_c,endpoint_d,endpoint_e}
    for endpoint in endpoint_to_test:
        response = requests.get(endpoint)
        # print(response)
        # print(endpoint)
        # print(response.status_code)
        # test_result.append({endpoint_a:response.status_code})
        test_result_dict[endpoint] = response.status_code
    print(test_result_dict)



@then('All Endpoints return valid')
def all_endpoints_return_valid(context):
    # result_dict = dict(test_result)
    global test_result
    for result in test_result_dict.values():
        test_result.append(True if result == 200 else False)
    all_valid = True if all(test_result) else False
    assert all_valid, f"Expect all valid, but not! {test_result_dict}"

@when('I get all currencies')
def get_all_currencies(context):
    data = get_endpoint(endpoint_a)
    # print(type(data))
    # print(len(data))
    global currency_count
    currency_count = len(data)


@then('There are {count} currencies listed')
def count_currencies(context,count):
    assert int(count) == currency_count, f"Expected {count} currencies, but {currency_count}!"

@when('I get api from all endpoints')
def get_all_endpoints(context):
    pass

@then('All schema are valid')
def all_schema_valid(context):
    pass

@when('I get currency with {basecurrency} as base currency')
def get_base_currency(context, basecurrency):
    print(currency_endpoint(basecurrency))
    data = get_endpoint(currency_endpoint(basecurrency))
    global test_result
    if basecurrency in data:
        print(data[basecurrency])
        test_result.append(True)
    else:
        test_result.append(False)

@then('Base currency result is valid')
def base_currency_result_valid(context):
    assert all(test_result),f"Expect valid result, but Not!"

@then('I got list of {basecurrency} as base currency')
def list_basecurrency(context, basecurrency):
    print(f"list basecurrency : {basecurrency}")

@when('I get currency of {basecurrency} in {resultcurrency}')
def get_base_currency(context, basecurrency, resultcurrency):
    print(currency_endpoint(basecurrency,resultcurrency))
    data = get_endpoint(currency_endpoint(basecurrency, resultcurrency))
    global test_result
    if resultcurrency in data:
        test_result.append(True)
    else:
        test_result.append(False)

@then('I got result currency of {resultcurrency}')
def got_result_currency(context, resultcurrency):
    assert all(test_result),f"Expect {resultcurrency} in result, but Not!"
