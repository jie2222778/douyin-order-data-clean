import pandas as pd

# 构造抖音电商订单：订单编号、买家昵称、手机号、收货地址、下单时间、商品名称、实付金额、订单状态
data_list = [

]
columns = ["订单编号","买家昵称","联系电话","收货地址","下单时间","商品名称","实付金额","订单状态"]
df = pd.DataFrame(data_list,columns=columns)
df.to_excel("抖音原始订单.xlsx", index=False)
print("抖音电商订单生成完毕！文件：抖音原始订单.xlsx")
print(f"原始订单总数：{len(df)}")
