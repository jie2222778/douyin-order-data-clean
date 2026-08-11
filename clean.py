import pandas as pd
import re
from datetime import datetime

def data_clean_work(file_path: str):
    raw_df = pd.read_excel(file_path, dtype={"订单编号": str, "联系电话": str})
    total_raw = len(raw_df)
    temp_df = raw_df.copy()
    print(f"【初始原始订单总量】：{total_raw} 条")

    for col in temp_df.columns:
        temp_df[col] = temp_df[col].astype(str).str.strip()
        temp_df[col] = temp_df[col].replace("", None)

    col_list = ["订单编号", "联系电话", "收货地址"]
    after_dropna = temp_df.dropna(subset=col_list)
    del_empty = len(temp_df) - len(after_dropna)
    temp_df = after_dropna
    print(f"【删除必填字段空缺数据】：移除 {del_empty} 条，剩余 {len(temp_df)} 条")

    phone_reg = re.compile(r"^1[3-9]\d{9}$")
    after_phone = temp_df[temp_df["联系电话"].apply(lambda x: bool(phone_reg.match(str(x))))]
    del_phone = len(temp_df) - len(after_phone)
    temp_df = after_phone
    print(f"【剔除格式错误手机号】：移除 {del_phone} 条，剩余 {len(temp_df)} 条")

    after_amount = temp_df[(temp_df["实付金额"] > 0) & (temp_df["实付金额"] < 10000)]
    del_amount = len(temp_df) - len(after_amount)
    temp_df = after_amount
    print(f"【剔除异常订单金额】：移除 {del_amount} 条，剩余 {len(temp_df)} 条")

    def check_time(time_str):
        try:
            datetime.strptime(str(time_str), "%Y-%m-%d %H:%M:%S")
            return True
        except:
            return False
    after_time = temp_df[temp_df["下单时间"].apply(check_time)]
    del_time = len(temp_df) - len(after_time)
    temp_df = after_time
    print(f"【剔除时间格式错误订单】：移除 {del_time} 条，剩余 {len(temp_df)} 条")

    after_status = temp_df[temp_df["订单状态"] == "待发货"]
    del_status = len(temp_df) - len(after_status)
    temp_df = after_status
    print(f"【剔除非待发货订单】：移除 {del_status} 条，最终合规发货订单：{len(temp_df)} 条")

    temp_df.to_excel("合规待发货订单.xlsx", index=False)
    print("\n数据清洗完毕，文件：合规待发货订单.xlsx 已生成")

if __name__ == "__main__":
    data_clean_work("抖音原始订单.xlsx")
