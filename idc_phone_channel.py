import pandas as pd

import numpy as np

phone_channel_input = pd.read_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/IDC All LOBs CSV Q2CY2019/IDC Mobile Channel CSV Q2CY2019.csv")

country_code_table=pd.read_csv("/Users/erishakya/Documents/MIP/IDC CountryCodes table.csv")

phone_channel_input.rename(columns={'Value (USD M)':'Value (US$M)','Storage Band':'Embedded Memory Band','RAM Band':'RAM Band(GB)'}, inplace=True)

keep_cols=['Region', 'Country', 'Vendor', 'Product Category',
       'Units', 'Value (US$M)', 'Price Band', 'Air Interface', 'Bluetooth',
       'Dual SIM','Embedded Memory Band','Product Detail', 'Generation',
       'Input Method', 'Megapixels Band', 'OS', 'OS Version', 
       'Quarter','Year', 'Primary Memory Card', 'Processor Vendor',
       'Processor Speed Band', 'Processor Cores', 'Screen Size',
       'Screen Size Band', 'Channel Group', 'Smartphone Class', 
       'Form Factor', 'RAM Band(GB)', 'Screen Resolution',
       'Channel']

phone_channel_cols=phone_channel_input[keep_cols]

new_phone_channel=phone_channel_cols.copy()

if 'TV' not in new_phone_channel:
    new_phone_channel.insert(27,"TV","NULL",True)

if 'WiFi' not in new_phone_channel:
    new_phone_channel.insert(28,"WiFi","NULL",True)

if 'Bluetooth LE' not in new_phone_channel:
    new_phone_channel.insert(30,"Bluetooth LE",new_phone_channel['Bluetooth'],True )

if 'Quarter 2' not in new_phone_channel:
    new_phone_channel.insert(18,"Quarter 2",new_phone_channel['Quarter'].str[-1:],True)

result =new_phone_channel.join(country_code_table.set_index('Country'), on='Country')

result.fillna(value='Fill', inplace=True)

result=result.groupby(by=['Region', 'Country','Country Code', 'Vendor',
       'Product Category', 'Price Band', 'Air Interface', 'Bluetooth', 'Dual SIM',
       'Embedded Memory Band', 'Product Detail', 'Generation', 'Input Method',
       'Megapixels Band', 'OS', 'OS Version', 'Quarter', 'Quarter 2', 'Year',
       'Primary Memory Card', 'Processor Vendor', 'Processor Speed Band',
       'Processor Cores', 'Screen Size', 'Screen Size Band', 'Channel Group',
       'Smartphone Class', 'TV', 'WiFi', 'Form Factor', 'Bluetooth LE',
       'RAM Band(GB)','Screen Resolution','Channel'],as_index=False)[['Units','Value (US$M)']].sum()

result=result.replace({'Fill':np.nan})

result.to_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/MyMipOutput/IDC1^PHONE^CHANNEL^2019Q2.csv",index=False)