import pandas as pd

import numpy as np

phone_segment_input=pd.read_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/IDC All LOBs CSV Q2CY2019/IDC Mobile Segment CSV Q2CY2019.csv")

country_code_table=pd.read_csv("/Users/erishakya/Documents/MIP/IDC CountryCodes table.csv")

phone_segment_input.rename(columns={'Value (USD M)':'Value (US$M)','Storage Band':'Embedded Memory Band','RAM Band':'RAM Band(GB)'}, inplace=True)

keep_cols=['Region', 'Country','Vendor', 'Product Category', 
           'Units','Value (US$M)','Price Band', 'Air Interface',
           'Bluetooth', 'Dual SIM', 'Embedded Memory Band','Product Detail',
           'Generation','Input Method',  'Megapixels Band', 'OS', 
           'OS Version','Quarter','Year', 'Primary Memory Card',
           'Processor Vendor','Processor Speed Band','Processor Cores',
           'Screen Size','Screen Size Band','Segment Group', 
           'Smartphone Class',  'Form Factor', 'RAM Band(GB)',
           'Screen Resolution','Segment']

phone_segment_cols=phone_segment_input[keep_cols]

phone_segment_cols=phone_segment_input[keep_cols]

if 'TV' not in new_phone_segment:
    new_phone_segment.insert(27,"TV","NULL",True)

if 'WiFi' not in new_phone_segment:
    new_phone_segment.insert(28,"WiFi","NULL",True)

if 'Bluetooth LE' not in new_phone_segment:
    new_phone_segment.insert(30,"Bluetooth LE",new_phone_segment['Bluetooth'],True )

if 'Quarter 2' not in new_phone_segment:
    new_phone_segment.insert(19,"Quarter 2",new_phone_segment['Quarter'].str[-1:],True)

result =new_phone_segment.join(country_code_table.set_index('Country'), on='Country')

result.fillna(value='Fill', inplace=True)

result=result.groupby(by=['Region', 'Country', 'Vendor', 'Product Category', 
        'Price Band', 'Air Interface', 'Bluetooth', 'Dual SIM',
       'Embedded Memory Band', 'Product Detail', 'Generation', 'Input Method',
       'Megapixels Band', 'OS', 'OS Version', 'Quarter', 'Quarter 2', 'Year',
       'Primary Memory Card', 'Processor Vendor', 'Processor Speed Band',
       'Processor Cores', 'Screen Size', 'Screen Size Band', 'Segment Group',
       'Smartphone Class', 'Form Factor', 'TV', 'WiFi', 'Screen Resolution',
       'Bluetooth LE', 'RAM Band(GB)', 'Segment', 'Country Code'],as_index=False)[['Units', 'Value (US$M)']].sum()

result=result.replace({'Fill': np.nan})

result=result[['Region', 'Country', 'Country Code', 'Vendor', 'Product Category', 'Units',
       'Value (US$M)', 'Price Band', 'Air Interface', 'Bluetooth', 'Dual SIM',
       'Product Detail', 'Embedded Memory Band', 'Generation',
       'Input Method', 'Megapixels Band', 'OS', 'OS Version', 'Quarter 2',
       'Quarter', 'Year', 'Primary Memory Card', 'Processor Vendor',
       'Processor Speed Band', 'Processor Cores', 'Screen Size',
       'Screen Size Band', 'Segment Group', 'Smartphone Class', 'TV', 'WiFi',
       'Form Factor', 'Bluetooth LE', 'Screen Resolution', 'RAM Band(GB)',
       'Segment']]

result.to_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/myMIPOutput/IDC1^PHONE^SEGMENT^2019Q2.csv",index=False)


