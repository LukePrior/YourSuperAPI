import json
import requests
from requests.structures import CaseInsensitiveDict

def get_data(amountRange = 9999, age = 0, balance = 50000, private = False):

    # Number of products to return
    if isinstance(amountRange, int) and amountRange > 0 and amountRange <= 9999:
        amountStart = 0
        amountEnd = amountRange
    elif isinstance(amountRange, list) and len(amountRange) == 2 and isinstance(amountRange[0], int) and isinstance(amountRange[1], int) and amountRange[1] > amountRange[0] and amountRange[0] >= 0 and amountRange[1] <= 9999:
        amountStart = amountRange[0]
        amountEnd = amountRange[1]
    else:
        amountStart = 0
        amountEnd = 9999

    if isinstance(age, int) and age >= 0 and age <= 99:
        individualAgeNumber = str(age)

    if (isinstance(balance, int) or isinstance(balance, float)) and balance >= 0:
        superannuationIndividualAccountBalanceAmount = format(round(balance, 2), '.2f')

    if isinstance(private, bool):
        privateFundsExcludedIndicator = str(private).lower()

    url = "https://www.ato.gov.au/api/v1/YourSuper/APRAData?Filter='clientIdentifierTypeCode=0,clientIdentifierValueID=0,individualAgeNumber=" + individualAgeNumber + ",performanceRatingCode=All,privateFundsExcludedIndicator=" + privateFundsExcludedIndicator + ",retrieveAllProductsIndicator=false,superannuationIndividualAccountBalanceAmount=" + superannuationIndividualAccountBalanceAmount + "'"

    print(url)

    headers = CaseInsensitiveDict()
    headers["range"] = "items=" + str(amountStart) + "-" + str(amountEnd)


    resp = requests.get(url, headers=headers)

    data = json.loads(resp.content)

    print(json.dumps(data, indent=4))


get_data(balance=1000000)
