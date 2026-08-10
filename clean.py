import pandas as pd
import re
import numpy as np

# 1、读取Excel：强制订单编号、手机号为文本格式，规避科学计数法（第二条整改点）
df = pd.read_excel("原始订单.xlsx",dtype={"订单编号":str,"手机号":str})

# 处理单元格仅含空格的字段，将空格转为空值（第三条整改点）
for col in df.columns:
    df[col] = df[col].astype(str).str.strip()
    df[col] = df[col].replace("",np.nan)

# 剔除订单编号、手机号、收货地址任一为空的数据（第三条整改补齐订单编号空值删除）
df = df.dropna(subset=["订单编号","手机号","收货地址"])

# 正则校验11位中国大陆手机号
phone_rule = re.compile(r"^1[3-9]\d{9}$")
df = df[df["手机号"].apply(lambda x: bool(phone_rule.match(x)))]

# 过滤异常订单金额：剔除负数、超大额订单
df = df[(df["订单金额"]>0) & (df["订单金额"]<10000)]

# 只保留待发货订单，筛选后续可发货订单（第一条整改点）
df = df[df["订单状态"]=="待发货"]

# 导出清洗完毕可发货订单
df.to_excel("可发货合规订单.xlsx",index=False)

# 打印清洗数据统计，直观展示前后数据量
origin_df = pd.read_excel("原始订单.xlsx")
print(f"原始订单总条数：{len(origin_df)}")
print(f"清洗后可发货合规订单条数：{len(df)}")
print("数据清洗完成，已导出【可发货合规订单.xlsx】")
