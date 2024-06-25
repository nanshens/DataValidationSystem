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
from entity.attribute import Attribute
from entity.entity import Entity
from entity.repair_rule import RepairRule
from entity.validation_rule import ValidationRule
from entity.validator import Validator


def get_validator_info_by_id(id):
    validator = Validator.query.get(id)
    entities = Entity.query.filter_by(active=True, validator_id=validator.id).all()
    entity_list = list()
    for entity in entities:
        entity_dict = entity.to_dict()
        attributes = Attribute.query.filter_by(active=True, entity_id=entity.id).all()
        attribute_list = list()
        for attribute in attributes:
            attribute_dict = attribute.to_dict()
            validation_rules = ValidationRule.query.filter_by(active=True, attribute_id=attribute.id).all()
            repair_rules = RepairRule.query.filter_by(active=True, attribute_id=attribute.id).all()

            attribute_dict['validation_rules'] = [rule.to_dict() for rule in validation_rules]
            attribute_dict['repair_rules'] = [rule.to_dict() for rule in repair_rules]

            attribute_list.append(attribute_dict)
        entity_dict['attributes'] = attribute_list
        entity_list.append(entity_dict)

    validator_dict = validator.to_dict()
    validator_dict['entities'] = entity_list
    return validator_dict

def copy_validator_service(request):
    #  get by id, copy
    pass

def generate_entity_info_service(request):
    #  get by id, copy
    pass