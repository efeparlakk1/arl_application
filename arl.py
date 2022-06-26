import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
from helpers import *

df_ = pd.read_excel("datasets/o_ret.xlsx",sheet_name = "Year 2010-2011")
df = df_.copy()

df = retail_data_prep(df)
df_ge = df[df['Country'] == "Germany"]
ge_inv_pro_df = create_invoice_product_df(df_ge)
df = retail_data_prep(df)
rules = create_rules(df)

#tryouts

check_id(df, 21987)
check_id(df, 23235)
check_id(df, 22747)

product_id = 21987
product_id = 23235
product_id = 22747

arl_recommender(rules, 21987, 5)
arl_recommender(rules, 23235, 5)
arl_recommender(rules, 22747, 5)