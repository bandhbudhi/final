from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup   import  Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import pandas as pd
import yfinance as yf
from openpyxl import load_workbook
from datetime import date, timedelta, datetime
import numpy as np
from kivy.uix.scrollview import ScrollView


class Basic(BoxLayout):
    nsefut = load_workbook(filename=r"nsefut.xlsx")
    NSEFUT = nsefut['Sheet1']#b2 - b189
    nsetfut_range = NSEFUT['B2':'B189']
    tickers = []

    for ticker in nsetfut_range :
        for tick  in ticker:
            ticker2 = tick.value
            tickers.append(ticker2)
            #print(tickers)

    def daily(self):
        
        with open("daily.txt","r+") as f:
                f.truncate(0)

        #time = value_inside.get()
        for a in self.tickers:
            df = pd.DataFrame(yf.download(tickers=a,period= '5y',time_interval = '1d',progress=False))
            df = df.round(decimals=2)
            f = a.replace(".NS","")
            df['Name'] = f
            today = date.today()
            d1 = today.strftime("%Y-%m-%d")
            #print(df.columns.values)

            
            diff = df['Close'] - df['Open']
            df['Diff'] = diff
                    
            percent = df['Diff']*100/df['Open']

            df['Percent'] = percent

            high = df['High'] - df['Open']
            hpercent = high*100/df['Open']

            low = df['Open'] - df['Low']
            lpercent = low*100/df['Open']

            df['High%'] = hpercent
            df['Low%'] = lpercent

            cond1 = (df['Percent'] <= 1) & (df['Percent'] >= -1)

            df['grades'] = np.select([cond1],['pos'],'N/A')

            pre = df['Volume'].iloc[-2]
            last = df['Volume'].iloc[-1]

            if (last >= pre ) and ('pos' in df['grades'].iloc[-1]):
                
                with open("daily.txt","a") as fin:                
                    pin = (df['Name'].iloc[-1])
                    print(pin,file=fin)
            else:            
                pass   
                        

    def trend(self):
        with open("trend.txt","r+") as f:
                f.truncate(0)
        for a in self.tickers:
            #time = value_inside.get()
            df = pd.DataFrame(yf.download(tickers=a,period= '5y',time_interval = '1d',progress=False))
            df = df.round(decimals=2)
            f = a.replace(".NS","")
            df['Name'] = f
            today = date.today()
            d1 = today.strftime("%Y-%m-%d")
            #print(df.columns.values)

            diff = df['Close'] - df['Open']
            df['Diff'] = diff
                    
            percent = df['Diff']*100/df['Open']

            df['Percent'] = percent

            high = df['High'] - df['Open']
            hpercent = high*100/df['Open']

            low = df['Open'] - df['Low']
            lpercent = low*100/df['Open']

            df['High%'] = hpercent
            df['Low%'] = lpercent

            cond1 = df['High%'].iloc[-1] >= 2
            cond2 = df['Low%'].iloc[-1] >= 2
            cond3 = (df['Percent'].iloc[-1] <= -2) or (df['Percent'].iloc[-1] >= 2)

            #df['grades'] = np.select([cond1],['pos'],'N/A')

            pre = df['Volume'].iloc[-2]
            last = df['Volume'].iloc[-1]

            if (last >= pre) and cond3:
                buy = df['Name'].iloc[-1]
                with open("trend.txt","a") as fin:
                    print(buy,file=fin)            
            else:
                pass

    def analyzer(self,*args):
        self.daily()
        self.trend()
        with open("daily.txt","r") as pinb:
                pinbr = pinb.read()

        self.ids.pinbar.text = pinbr                

        with open("trend.txt","r") as tinb:
                tndbr = tinb.read()

        self.ids.trendbar.text = tndbr  
                        
            


                
class TrendApp(App):
    pass

TrendApp().run()

