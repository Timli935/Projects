import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")
import os

os.getcwd() #check the file path for imports

indicepanel = pd.read_csv('indicepanel_2.csv') #data containing performance of of major indices
indicepanel.head() #checks for the data format

indicepanel['50d_ma'] = indicepanel['Price'].rolling(window=50).mean()
Train = indicepanel.iloc[-2000:-1000:]
Test = indicepanel.iloc[-1000::]
indicepanel['Signal'] = 0
indicepanel['Signal'][50:] = np.where(indicepanel['Price'][50:] > indicepanel['50d_ma'][50:], 1, -1)
indicepanel['Signal'] = indicepanel['Signal']


#indicepanel.dropna(subset=['50d_ma'], inplace=True)
Train['Profit'] = Train['spy'] * Train['Signal'].shift(7)
Test['Profit'] = Test['spy'] * Test['Signal'].shift(7)

for df in [Train, Test]:
    df['Profit'] = df['spy'] * df['Signal']
    df['Wealth'] = df['Profit'].cumsum()

print('Total profit made in Train: ', Train['Profit'].sum())
Test['Wealth'] = Test['Profit'].cumsum()
print('Total profit made in Test: ', Test['Profit'].sum())
#Test.tail(60)

#plotting the performance of train strategy
plt.figure(figsize=(10, 10))
plt.title('Performance of Train Strat')
plt.plot(Train['Wealth'].values, color='green', label='Signal based strategy')
plt.plot(Train['spy'].cumsum().values, color='red', label='Buy and Hold strategy')
plt.legend()
plt.show()

#plotting the performance of test strategy
plt.figure(figsize=(10, 10))
plt.title('Performance of Strategy in Train')
plt.plot(Test['Wealth'].values, color='green', label='Signal based strategy')
plt.plot(Test['spy'].cumsum().values, color='red', label='Buy and Hold strategy')
plt.legend()
plt.show()

#Fund performance calculations

Train['Wealth'] = Train['Wealth'] + Train.loc[Train.index[0], 'Price']
Test['Wealth'] = Test['Wealth'] + Test.loc[Test.index[0], 'Price']

# Sharpe Ratio on Train data
Train['Return'] = np.log(Train['Wealth']) - np.log(Train['Wealth'].shift(1))
dailyr = Train['Return'].dropna()

print(f'Daily Sharpe Ratio of Train is {dailyr.mean()/dailyr.std(ddof=1)}')
print(f'Yearly Sharpe Ratio of Train is {(252**0.5)*dailyr.mean()/dailyr.std(ddof=1)}')

# Sharpe Ratio in Test data
Test['Return'] = np.log(Test['Wealth']) - np.log(Test['Wealth'].shift(1))
dailyr = Test['Return'].dropna()

print(f'Daily Sharpe Ratio is {dailyr.mean()/dailyr.std(ddof=1)}')
print(f'Yearly Sharpe Ratio is {(252**0.5)*dailyr.mean()/dailyr.std(ddof=1)}')

# Max Drawdown of Train data
Train['Peak'] = Train['Wealth'].cummax()
Train['Drawdown'] = (Train['Peak'] - Train['Wealth'])/Train['Peak']
print(f'Maximum Drawdown in Train is {Train["Drawdown"].max()}')

# Max Drawdown of Test data
Test['Peak'] = Test['Wealth'].cummax()
Test['Drawdown'] = (Test['Peak'] - Test['Wealth'])/Test['Peak']
print(f'Maximum Drawdown in Test is {Test["Drawdown"].max()}')

#R squared
R = (Train['Wealth']).corr(Train['spy'].cumsum())
print(f'R squared is {R**(2)}')



