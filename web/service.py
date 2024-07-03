# todo: 修改validator 有log
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