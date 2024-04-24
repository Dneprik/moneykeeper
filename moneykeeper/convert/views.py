import requests
from django.shortcuts import render

# Create your views here.


def convert(request):
    url = 'https://api.currencyapi.com/v3/latest?apikey=cur_live_cWwh0OI6URIUPCMsSMaHTwiloHqgFeP5rbailTfu'

    response = requests.get(url)
    print(response)
    data = response.json()
    print(data)
    curr_values = []
    for curr_data in data['data'].values():
        curr_values.append(curr_data['code'])
        print(curr_data)

    print(curr_values)
    my_data = {'list_of_currency': curr_values}

    if request.method == 'POST':
        curr_old = request.POST.get('option1')
        print(curr_old)
        curr_new = request.POST.get('option2')
        print(curr_new)
        amount = request.POST.get('input1')
        print(amount)

        for curr in data['data'].values():
            if curr['code'] == curr_old:
                cur_ex_old = curr['value']
            if curr['code'] == curr_new:
                cur_ex_new = curr['value']

        try:
            amount_float = float(amount)

        except ValueError:
            amount = 0

        if amount != '':
            res_amount = float(amount) * float(cur_ex_new) / float(cur_ex_old)
        else:
            res_amount = 0
        my_data['res'] = format(res_amount, '.2f') + "  " + curr_new
        my_data['amount'] = amount
        my_data['cur_old'] = curr_old
        my_data['cur_new'] = curr_new

        print(cur_ex_old)
        print(cur_ex_new)
        print(my_data)




    return render(request, 'convert.html', my_data)

