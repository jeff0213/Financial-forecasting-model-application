import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def patent_evaluation(hyp_dict,img_path):
    Fin_BusinessTurnover = hyp_dict['Fin_BusinessTurnover']
    Fin_Direct_costs = hyp_dict['Fin_Direct_costs']
    Fin_Indirect_costs = hyp_dict['Fin_Indirect_costs']
    Fin_ProvisionForDeprec = hyp_dict['Fin_ProvisionForDeprec']
    Fin_DeprecPeriod = hyp_dict['Fin_DeprecPeriod']
    Def_of_BusinessArea = hyp_dict['Def_of_BusinessArea']
    Fin_DiscountFactor = hyp_dict['Fin_DiscountFactor']
    Fin_TotalGrowthIn_General_CompanyMarket = hyp_dict['Fin_TotalGrowthIn_General_CompanyMarket']
    B5 = hyp_dict['B5']
    C2 = hyp_dict['C2']
    C3 = hyp_dict['C3']
    C6 = hyp_dict['C6']
    D1 = hyp_dict['D1']
    D2 = hyp_dict['D2']
    D3 = hyp_dict['D3']
    D4 = hyp_dict['D4']
    e = []
    for y in range(5):
        Revenue = C6 * (1 + C2) ** (y) * Def_of_BusinessArea * (1 + C2) ** (1 + y) * 100
        print(Revenue)
        e.append(Revenue)

    e = [0, 0, 0.644, 0.85169, 1.1263600249999999, 1.4896111330624995, 1.970010723475155, 0, 0, 0]

    Fin_Share_Direct_costs = Fin_Direct_costs / Fin_BusinessTurnover * 100
    Fin_Share_Indirect_costs = Fin_Indirect_costs / Fin_BusinessTurnover * 100
    Share_Costs = (Fin_Share_Direct_costs + Fin_Share_Indirect_costs) / 100

    f = []
    for y in range(2):
        Costs = e[y] * D3 * Share_Costs + D2 * Def_of_BusinessArea * 100
        print(Costs)
        f.append(Costs)
    # plt.plot(f)
    f = [0.49, 0.49, 0, 0, 0, 0, 0, 0, 0, 0]

    g = []
    for y in range(5):
        Regained_revenue = (100 - Share_Costs * 100) * (1 - D1) * Def_of_BusinessArea * (1 + C2) ** (1 + y)
        print(Regained_revenue)
        g.append(Regained_revenue)
    # plt.plot(g)

    g = [0, 0, 1.7262857566103826, 1.9852286201019398, 2.283012913117231, 2.625464850084815, 3.019284577597537, 0, 0, 0]

    # Revenue = C6*(1+C2)**2*Def_of_BusinessArea*(1+C2)**2*100#(computed for each year in which the product is on the market within its life expectancy)
    Fin_Share_Direct_costs = Fin_Direct_costs / Fin_BusinessTurnover * 100
    Fin_Share_Indirect_costs = Fin_Indirect_costs / Fin_BusinessTurnover * 100
    Share_Costs = (Fin_Share_Direct_costs + Fin_Share_Indirect_costs) / 100
    Costs = Revenue * D3 * Share_Costs + D2 * Def_of_BusinessArea * 100
    Regained_revenue = (100 - Share_Costs * 100) * (1 - D1) * Def_of_BusinessArea * (1 + C2) ** (1 + y)
    Efficiency = Share_Costs * 100 * (1 - D3) * Def_of_BusinessArea * (1 + C2) ** 2
    Share_Deprec = Fin_Share_ProvisionForDeprec = Fin_ProvisionForDeprec / Fin_BusinessTurnover * 100
    InvestmentReduction = Fin_DeprecPeriod * Share_Deprec * (1 - D4) * Def_of_BusinessArea * (1 + C2) ** 2
    Investments = Fin_ProvisionForDeprec * Fin_DeprecPeriod
    Liquidity = Revenue - Costs - Investments + Regained_revenue + Efficiency + InvestmentReduction

    h = []
    for y in range(5):
        Patent_Regained_Deprec = Fin_BusinessTurnover * Def_of_BusinessArea * Share_Deprec * (1 - D1) * (1 + C2) ** (
                1 + y) / 100
        print(Patent_Regained_Deprec)
        h.append(Patent_Regained_Deprec)

    h = [0, 0, 3852546.8625, 4430428.891875, 5094993.225656249, 5859242.209504685, 6738128.540930388, 0, 0, 0]

    b = []
    c = []
    d = []
    for y in range(7):
        WithoutPatent_Turnover = Fin_BusinessTurnover * D1 * (1 + C2) ** (1 + y) * Def_of_BusinessArea
        WithoutPatent_Costs = Share_Costs * WithoutPatent_Turnover
        WithoutPatent_Deprec = Share_Deprec / 100 * WithoutPatent_Turnover
        WithoutPatent_Profits = WithoutPatent_Turnover - WithoutPatent_Costs - WithoutPatent_Deprec
        Patent_Turnover = e[y] * Fin_BusinessTurnover / 100
        Patent_regained_revenue = Fin_BusinessTurnover * g[y] / 100
        Patent_Costs = (Fin_BusinessTurnover * f[y] / 100 - (
                (WithoutPatent_Turnover / Def_of_BusinessArea) * (Efficiency / 100) / (1 + C2) ** (1 + y))) - (
                               Patent_regained_revenue / (Share_Costs) * Efficiency) / 100
        # Patent_Regained_Deprec = Fin_BusinessTurnover*Def_of_BusinessArea*Share_Deprec*(1-D1)*(1+C2)**(1+y)/100#(computed only if revenue for the current year is greater than 0)
        Patent_Deprec = (
                (Patent_Turnover * D4 * Share_Deprec / 100) - (WithoutPatent_Turnover * Share_Deprec * (1 - D4) / 100) -
                h[y] * (1 - D4))  # (computed only if revenue for the current year is greater than 0)
        Patent_Profits = Patent_Turnover - Patent_Costs - Patent_Deprec - h[y] + Patent_regained_revenue
        A = WithoutPatent_Profits + Patent_Profits
        # print(WithoutPatent_Profits)
        b.append(WithoutPatent_Profits)
        # print(Patent_Profits)
        c.append(Patent_Profits)
        # print(A)
        d.append(A)

    b = list(b)
    b.extend([0, 0, 0])
    c = list(c)
    c.extend([0, 0, 0])
    h = sum(c)
    d = list(d)
    d.extend([0, 0, 0])
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = np.arange(len(x))
    tick_label = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    width = 0.35
    # fig= plt.plots()
    plt.figure(figsize=[20, 15])
    plt.bar(x, b, width, alpha=0.9, label='Business-area profits without the patent technology')
    plt.plot(x + width / 2, c, marker='*', label='Foreseeable profits for the patent technology')
    plt.bar(x + width, d, width, alpha=0.9, label='Business-area profits with the patent technology')
    plt.xticks(x + width / 2, tick_label)  # 将坐标设置在指定位置
    # plt.xticklabels(x)#将横坐标替换成
    plt.legend()
    plt.savefig(img_path+"1.png")
    # plt.show()
    img_path = img_path+"1.png"



    result = {'Business-area profits without the patent technology':b,'Foreseeable profits for the patent technology':c,
              'Business-area profits with the patent technology':d }

    return result


if __name__ == '__main__':
    patent_evaluation()
