import yfinance as yf
import pandas as pd
import pprint
from statistics import mean

PE_Lookup = {0.05: 10, 0.06: 11, 0.07: 11, 0.08: 12, 0.09: 13, 0.1: 13, 0.11: 14, 0.12: 15, 0.13: 16, 0.14: 17, 0.15: 18, 0.16: 19, 0.17: 20, 0.18: 21, 0.19: 23, 0.2: 24, 0.21: 25, 0.22: 27, 0.23: 29, 0.24: 30, 0.25: 32, 0.26: 33, 0.27: 34, 0.28: 35, 0.29: 36, 0.3: 37, 0.31: 38, 0.32: 39, 0.33: 41, 0.34: 42, 0.35: 43, 0.36: 44, 0.37: 46, 0.38: 47, 0.39: 49, 0.4: 50, 0.41: 51, 0.42: 53, 0.43: 55, 0.44: 56, 0.45: 58, 0.46: 60, 0.47: 61, 0.48: 63, 0.49: 65, 0.5: 67}

class Company:

    def __init__(self, data):
        self.__data = data
        self.name = self.__data.info['shortName']
        self.ticker = self.__data.ticker

        self._perpetual_growth_rate = 0.025
        self.shares_outstanding = self.__data.info['sharesOutstanding']/1000000

        # This is not correct, change later
        self.free_cash_flow = [x/1000000 for x in self.__data.cashflow.loc[['Total Cash From Operating Activities']].values.tolist()[0][::-1]]

        self.revenue = [x/1000000 for x in self.__data.financials.loc[['Total Revenue']].values.tolist()[0]][::-1]
        self.net_income = [x/1000000 for x in self.__data.financials.loc[['Net Income']].values.tolist()[0]][::-1]
        self.net_profit_margins = [x/y for x, y in zip(self.net_income, self.revenue)]
        self.fcf_to_profit_margins = [x/y for x, y in zip(self.free_cash_flow, self.net_income)]

        self.avg_profit_margin = mean(self.net_profit_margins)
        self.avg_fcf_to_profit_margin = mean(self.fcf_to_profit_margins)
        self.growth_rate = self.__data.expectedGrowth

        self._ad_profit_margin = None
        self._ad_fcf_to_profit_margin = None
        self._ad_growth_rate = None

        self._personal_required_return_rate = 0.07
        self.todays_share_price = self.__data.info['regularMarketPrice'] # check later

        self.updateDCFModel()
        self.updateGrowthModel()
        self.getSuggestedModel()

    def updateDCFModel(self):
        pft_margin = self.avg_profit_margin if self._ad_profit_margin is None else self._ad_profit_margin
        fcf_pft_margin = self.avg_fcf_to_profit_margin if self._ad_fcf_to_profit_margin is None else self._ad_fcf_to_profit_margin
        gth_rate = self.growth_rate if self._ad_growth_rate is None else self._ad_growth_rate

        y0 = self.__data.expectedRevenue.loc[tick.expectedRevenue['Period'] == '0y', 'Revenue'].item()/1000000
        y1 = self.__data.expectedRevenue.loc[tick.expectedRevenue['Period'] == '+1y', 'Revenue'].item()/1000000
        self.revenue_e = [y0] + [y1*pow(1+gth_rate, x) for x in range(3)]
        self.net_income_e = [x * pft_margin for x in self.revenue_e]
        self.free_cash_flow_e = [x * fcf_pft_margin for x in self.net_income_e]
        self.ternimal_value = self.free_cash_flow_e[-1] * (1 + self.perpetual_growth_rate) / (self.personal_required_return_rate - self.perpetual_growth_rate)

        self.discount_factor = [pow(1+self.personal_required_return_rate, x+1) for x in range(4)]
        self.pv_of_future_cash_flow = [x/y for x, y in zip(self.free_cash_flow_e, self.discount_factor)]

        self.todays_value = sum(self.pv_of_future_cash_flow) + (self.ternimal_value/self.discount_factor[-1])

        self.fair_value_of_equity = self.todays_value/self.shares_outstanding

    def updateGrowthModel(self):
        gth_rate = self.growth_rate if self._ad_growth_rate is None else self._ad_growth_rate

        self.eps = (self.__data.earnings['Earnings'].iloc[-1]/1000000)/self.shares_outstanding
        self.eps_e = [self.__data.expectedEPS.loc[self.__data.expectedEPS['Period'] == '0y', 'EPS'].item()] + [self.__data.expectedEPS.loc[self.__data.expectedEPS['Period'] == '+1y', 'EPS'].item()*pow(1+gth_rate, x) for x in range(4)]

        self.pe_ratio = self.todays_share_price/self.eps
        self.pe_ratio_e = PE_Lookup[round(min(0.5, max(0.05, gth_rate)), 2)]
        self.projected_share_price = self.pe_ratio_e * self.eps_e[-1]
        self.annual_return_pa = pow(self.projected_share_price/self.todays_share_price, 0.2) - 1

        self.fair_value_of_price = self.projected_share_price/pow(1+self.personal_required_return_rate, 5)
        self.profit_margin = self.fair_value_of_price/self.todays_share_price - 1

    def getSuggestedModel(self):
        if(sum(e > 0 for e in self.free_cash_flow)>=3 and self.avg_fcf_to_profit_margin > 0):
            return 'DCF'
        elif(self.eps > 0 or self.eps_e[1] > 0):
            return 'GROWTH'
        else:
            return 'NA'

    @property
    def ad_profit_margin(self):
        return self._ad_profit_margin

    @ad_profit_margin.setter
    def ad_profit_margin(self, val):
        self._ad_profit_margin = val
        self.updateDCFModel()

    @property
    def ad_fcf_to_profit_margin(self):
        return self._ad_fcf_to_profit_margin

    @ad_fcf_to_profit_margin.setter
    def ad_fcf_to_profit_margin(self, val):
        self._ad_fcf_to_profit_margin = val
        self.updateDCFModel()

    @property
    def ad_growth_rate(self):
        return self._ad_growth_rate

    @ad_growth_rate.setter
    def ad_growth_rate(self, val):
        self._ad_growth_rate = val
        self.updateDCFModel()
        self.updateGrowthModel()

    @property
    def perpetual_growth_rate(self):
        return self._perpetual_growth_rate

    @perpetual_growth_rate.setter
    def perpetual_growth_rate(self, val):
        self._perpetual_growth_rate = val
        self.updateDCFModel()

    @property
    def personal_required_return_rate(self):
        return self._personal_required_return_rate
    
    @personal_required_return_rate.setter
    def personal_required_return_rate(self, val):
        self._personal_required_return_rate = val
        self.updateDCFModel()
        self.updateGrowthModel()        

if __name__ == '__main__':
    try:
        tick = yf.Ticker("TSLA")
    except:
        print("No Company Ticker Found.")
        exit(0)
    comp = Company(tick)
    # pprint.PrettyPrinter(indent=4).pprint(comp.pe_ratio_e)
    suggestedModel = comp.getSuggestedModel()
    if(suggestedModel == 'DCF'):
        print(comp.fair_value_of_equity)

        # 这里相当于改变表格里蓝色格子的值，结果会自动更新。所有用了setter的变量都可以这样操作
        comp.personal_required_return_rate = 0.9
        print(comp.fair_value_of_equity)
    elif(suggestedModel == 'GROWTH'):
        print(comp.fair_value_of_price)

        # 同上
        comp.ad_growth_rate = 2.0
        print(comp.fair_value_of_price)
    else:
        print('傻逼公司')
