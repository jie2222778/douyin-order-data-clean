import pandas as pd

#读取生成好的原始订单表格
df = pd.read_excel("抖音原始订单.xlsx")
print(f"清洗之前订单总数：{len(df)}")

#1.删除整张为空的空白行
df = df.dropna(how="all")
#2.剔除手机号为空，没法发货的订单
df = df.dropna(subset=["联系电话"])
#3.剔除收货地址为空的订单
df = df.dropna(subset=["收货地址"])
#4.按照订单编号去重，删掉后台重复导出的订单
df = df.drop_duplicates(subset="订单编号", keep="first")

#导出清洗之后合规能发货的订单表
df.to_excel("抖音清洗后合规订单.xlsx", index=False)
print(f"清洗完成，有效发货订单数量：{len(df)}")