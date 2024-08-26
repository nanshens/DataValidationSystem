# AQ-DataValidator

一个校验多个excel 和csv 数据的系统

## 简介

一些企业系统, 类似crm, erp等,使用xlsx或者csv导入数据, 通常数据会有一些格式校验和关联关系, 可能会重复修改原数据并修复.   
使用本系统可以通过配置实体的关系, 校验信息, 修复信息, 用来快速修复导入文件, 并展示结果和导出新数据等.


## 类库

pip install Flask-SQLAlchemy
pip install flask
pip install pandas
pip install openpyxl
pip install psycopg2