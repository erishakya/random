import pandas as pd


pc_segment_input=pd.read_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/IDC All LOBs CSV Q2CY2019/IDC PC Segment CSV Q2CY2019.csv")

pc_segment_input.rename(columns={'Company':'Vendor Group','Value (USD M)':'Value (USD)'}, inplace=True)

pc_segment_cols=pc_segment_input[keep_cols]

new_pc_segment=pc_segment_cols.copy()

new_pc_segment.to_csv("/Users/erishakya/Documents/MIP/MIP.Second.data/MyMipOutput/IDC1^PC^SEGMENT^2019Q2.csv",index=False)

