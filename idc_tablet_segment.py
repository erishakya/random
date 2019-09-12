import pandas as pd

import numpy as np

tablet_segment_input = pd.read_csv('/Users/erishakya/Documents/MIP/MIP.Second.data/IDC All LOBs CSV Q2CY2019/IDC Tablet Segment CSV Q2CY2019.csv')

tablet_segment_input.rename(columns={'Product Detail':'Form Factor','Screen Size Band':'Screen Size Band Historical','Value (USD M)':'Value (US$M)'}, inplace=True)

keep_cols= ['Region','Country','Quarter','Vendor','Form Factor',
            'Connectivity','OS','CPU Type','Screen Size',
            'Screen Size Band Historical','Screen Resolution','Storage (GB)',
            'Segment Group','Units','Value (US$M)','Price Band',
            'Year','Product Category','RAM (GB)','Air Interface',
            'Generation','Segment']

tablet_segment_cols=tablet_segment_input[keep_cols]

new_tablet_segment=tablet_segment_cols.copy()

new_tablet_segment.fillna(value='Fill', inplace=True)

tablet_segment_output =new_tablet_segment.groupby(by=['Region', 'Country', 'Quarter', 'Vendor', 
                                                      'Form Factor', 'Connectivity','OS', 'CPU Type',
                                                      'Screen Size', 'Screen Size Band Historical',
                                                      'Screen Resolution', 'Storage (GB)', 'Segment Group',
                                                      'Price Band', 'Year', 'Product Category', 'RAM (GB)','Air Interface',
                                                      'Generation', 'Segment'],as_index=False)[['Units','Value (US$M)']].sum().reindex(columns=keep_cols)

tablet_segment_output.replace('Fill', np.nan)

tablet_segment_output.to_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/MyMipOutput/IDC1^TABLET^SEGMENT^2019Q2.csv",index=False)