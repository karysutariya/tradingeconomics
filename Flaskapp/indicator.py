import tradingeconomics as te

te.login('dcbdd8ec4d16458:cqg9cd98jd9jzkg')

data = te.getIndicatorData(country=['mexico','sweden'], indicators='gdp')

real_data = dict()

for no,i in enumerate(data):
    new_dic = dict()
    new_dic['Country'] = i['Country'] + " GDP"
    new_dic['Current GDP'] = i['LatestValue']
    new_dic['Previous GDP'] = i['PreviousValue']
    real_data[no] = new_dic
