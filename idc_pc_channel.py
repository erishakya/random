import pandas as pd
import numpy as np

pc_channel_input = pd.read_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/IDC All LOBs CSV Q2CY2019/IDC PC Channel CSV Q2CY2019.csv")

pc_channel_input.rename(columns={'Company':'Vendor Group','Channel Group':'Channel_Group','Value (USD M)':'Value (USD)'}, inplace=True)

keep_cols= ['Quarter', 'Region', 'Country', 'Product Category', 
            'Product', 'Product Detail', 'Vendor', 'Vendor Group', 'OS',
            'Product Brand', 'Price Band', 'Screen Size Band', 
            'Channel_Group', 'Channel', 'Units', 'Value (USD)']

pc_channel_cols=pc_channel_input[keep_cols]

new_pc_channel=pc_channel_cols.copy()

new_pc_channel.to_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/MyMipOutput/IDC1^PC^CHANNEL^2019Q2.csv",index=False)
