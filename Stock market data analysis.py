#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf
import plotly.io as pio
import ploty.graph_objects as go
pio.templates.default ="plotly_white"


# In[2]:


pip install yfinance


# In[1]:


import yfinance as yf


# In[2]:


import pandas as pd
import yfinance as yf
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default ="plotly_white"


# In[4]:


#define the tickers for apple and google
apple_ticker ='AApl'
google_ticker='GOOGL'

#define the data range for the last quarter
start_date ="2023-07-01"
end_date ="2023-09-30"

# fetuch historical stock price data using yfinance
apple_data =yf.download(apple_ticker,start=start_date,end =end_date)
google_data = yf.download(google_ticker,start =start_date,end =end_date)


# In[5]:


#calculate daily returns
apple_data['Daily_return'] =apple_data['Adj Close'].pct_change()
google_data['Daily_return'] =google_data['Adj Close'].pct_change()


# In[6]:


#create a figure to visualize the daily return
fig =go.Figure()
fig.add_trace(go.Scatter(x=apple_data.index, y=apple_data['Daily_return'],
                        mode ='lines',name ='apple',line =dict(color ='blue')))
fig.add_trace(go.Scatter(x=google_data.index, y =google_data['Daily_return'],
                        mode ='lines',name ='google', line=dict(color ='green')))
fig.update_layout(title='Daily returns for apple and google',
                  xaxis_title='Date',yaxis_title='Daily Return',legend=dict(x=0.02, y=0.95))
fig.show()


# In[7]:


#calculate cumulative returns for the last quarter
apple_cumulative_return =(1 + apple_data['Daily_return']).cumprod() -1
google_cumulative_return =(1 + google_data['Daily_return']).cumprod() -1

#create a figure to visualize the daily return

fig =go.Figure()
fig.add_trace(go.Scatter(x=apple_cumulative_return .index, y=apple_cumulative_return,
                        mode ='lines',name ='apple',line =dict(color ='blue')))
fig.add_trace(go.Scatter(x=google_cumulative_return.index, y =google_cumulative_return,
                        mode ='lines',name ='google', line=dict(color ='green')))
fig.update_layout(title='cumulative returns for apple and google',
                  xaxis_title='Date',yaxis_title='cumulative Return',legend=dict(x=0.02, y=0.95))
fig.show()


# In[8]:


# calaculate historical volatitlity(Standard deviation of daily return)
apple_v =apple_data['Daily_return'].std()
google_v =google_data['Daily_return'].std()

#create a figure to compare volatility
fig1 =go.Figure()
fig1.add_bar(x=['apple','google'],y =[apple_v,google_v],
             text=[f'{apple_v:.4f}',f'{google_v:.4f}'],
             textposition ="auto",marker =dict(color=["blue","green"]))
fig1.update_layout(title ="volatlity compring",xaxis_title="Stock",yaxis_title="volatility(std )",bargap =0.7)
                   


# In[44]:


market_data =yf.download('^GSPC',start=start_date,end =end_date)

apple_data['Daily_return'] =apple_data['Adj Close'].pct_change()
google_data['Daily_return'] =google_data['Adj Close'].pct_change()
market_data['daily_return'] =market_data['Adj Close'].pct_change()

# calculate beta for apple and google
app =apple_data['Daily_return'].cov(market_data['daily_return'])
mar =market_data['daily_return'].var()

beta_apple =app/mar

goog =google_data["Daily_return"].cov(market_data['daily_return'])
beta_google =goog/mar

# compare beta value
if beta_apple >beta_google:
    x= "Apple is more"
else:
    x ="google is more"
print(beta_apple)
print(beta_google)
print(x)


# In[ ]:





# In[ ]:




