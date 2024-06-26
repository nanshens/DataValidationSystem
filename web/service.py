# todo 1. 定义表结构
# todo 1. crud 表结构
# todo 1. 定义枚举
# todo 1. controller 和service
# todo 添加验证策略 curd
# todo 为策略添加subject 和column 和rule, 修复rule
# todo: 执行策略 记录log
# todo: 生成结果 自动修改, 生成对比文件
# todo  查看历史结果
# todo: 导入文件有备份
from entity.validator import Validator


def get_validator_info_by_id(id):
    validator = Validator.query.get(id)
    return validator.to_dict(True) if validator is not None else {}

def copy_validator_service(request):
    #  get by id, copy
    pass

def generate_entity_info_service(request):
    #  get by id, copy
    pass