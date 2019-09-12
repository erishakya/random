import pandas as pd 

import numpy as np

tablet_channel_input=pd.read_csv('/Users/erishakya/Documents/MIP/MIP.Second.data/IDC All LOBs CSV Q2CY2019/IDC Tablet Channel CSV Q2CY2019.csv')

tablet_channel_input.rename(columns={'Product Category':'Form Factor','Screen Size Band':'Screen Size Band Historical','Value (USD M)':'Value (US$M)'}, inplace=True)

keep_cols= ['Region','Country','Quarter','Vendor','Form Factor',
            'Connectivity','OS','CPU Type','Screen Size',
            'Screen Size Band Historical','Screen Resolution','Storage (GB)',
            'Channel','Units','Value (US$M)','Price Band','Year',
            'RAM (GB)','Air Interface','Generation']

tablet_channel_cols=tablet_channel_input[keep_cols]

new_tablet_channel=tablet_channel_cols.copy()

new_tablet_channel.rename(columns={'Product Category':'Form Factor','Screen Size Band':'Screen Size Band Historical','Value (USD M)':'Value (US$M)'}, inplace=True)

new_tablet_channel.fillna(value='Fill', inplace=True)

tablet_channel_output=new_tablet_channel.groupby(by =['Region', 'Country', 'Quarter', 'Vendor', 
                                                      'Form Factor', 'Connectivity','OS', 'CPU Type', 
                                                      'Screen Size', 'Screen Size Band Historical',
                                                      'Screen Resolution','Storage (GB)','Channel', 
                                                      'Price Band', 'Year', 'RAM (GB)', 'Air Interface', 
                                                      'Generation'], as_index=False)[['Units','Value (US$M)']].sum().reindex(columns=keep_cols)


tablet_channel_output.replace('Fill', np.nan)

tablet_channel_output.to_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/MyMipOutput/IDC1^TABLET^CHANNEL^2019Q2.csv",index=False)