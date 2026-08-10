## 项目简介
基于Python、Pandas对抖音小店导出的Excel订单进行脏数据清洗，剔除重复订单、手机号为空、收货地址缺失、表格空行等无效数据，筛选可直接物流发货的合规订单，规避电商重复打单风险。

## 依赖环境
```bash
pip install pandas openpyxl
