# todo: 修改validator 有log
# todo: 执行策略 记录log
# todo: 生成结果 自动修改, 生成对比文件
# todo  查看历史结果
# todo: 导入文件有备份
from entity.executor import Executor
from entity.validator import Validator


def get_validator_info_by_id(id):
    validator = Validator.query.get(id)
    return validator.to_dict(True) if validator is not None else {}

def get_executor_by_id(id):
    executor = Executor.query.get(id)
    return executor.to_dict() if executor is not None else {}

def copy_validator_service(request):
    #  get by id, copy
    pass

def generate_match_entity(id):
    # todo: 读取xlsx, 或者csv 文件 生成实体属性匹配信息
    # todo: 1 自动匹配 返回结果, 手动填写, 保存.

    pass