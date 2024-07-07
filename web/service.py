# todo: 修改validator 有log
# todo: 执行策略 记录log
# todo: 生成结果 自动修改, 生成对比文件
# todo  查看历史结果
# todo: 导入文件有备份
import os
import uuid

import pandas as pd
from entity import db
from entity.executor import Executor
from entity.validator import Validator


def get_validator_info_by_id(id):
    validator = Validator.query.get(id)
    return validator.to_dict(True) if validator is not None else {}

def get_executor_by_id(id):
    executor = Executor.query.get(id)
    if executor is None: return {}
    data = executor.to_dict()
    data['validator'] = executor.validator.to_dict(True)
    return data

def copy_validator_service(request):
    #  get by id, copy
    pass

def generate_match_entity(id):
    # todo: 读取xlsx, 或者csv 文件 生成实体属性匹配信息
    # todo: 1 自动匹配 返回结果, 手动填写, 保存.
    executor = Executor.query.get(id)
    validator_entities = executor.validator.entities
    path = f"./data/{id}/"
    match_entities = []

    def add_entity(match_entities, headers, filename):
        entity = {}
        entity['id'] = str(uuid.uuid4())
        entity['file_name'] = filename
        entity['entity_id'] = filename
        entity['entity_code'] = filename
        entity['active'] = True
        entity['attributes'] = []
        for header in headers:
            attribute = {}
            attribute['id'] = str(uuid.uuid4())
            attribute['column_name'] = header
            attribute['attribute_id'] = header
            attribute['attribute_code'] = header
            attribute['active'] = True
            entity['attributes'].append(attribute)
        match_entities.append(entity)

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
            headers = df.columns.tolist()
            add_entity(match_entities, headers, filename)

        elif filename.endswith('.xlsx'):
            xlsx = pd.ExcelFile(file_path)
            for sheet_name in xlsx.sheet_names:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                headers = df.columns.tolist()
                add_entity(match_entities, headers, filename + "_" + sheet_name)

    executor.match_entities = match_entities
    db.session.commit()
    return executor.to_dict()