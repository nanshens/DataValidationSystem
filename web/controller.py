from flask import Blueprint, request, jsonify

from common.response import Response
from entity import db
from entity.attribute import Attribute
from entity.entity import Entity
from entity.repair_rule import RepairRule
from entity.validation_rule import ValidationRule
from entity.validator import Validator
from web.service import get_validator_info_by_id, copy_validator_service, generate_entity_info_service

controller = Blueprint('controller', __name__)

@controller.route("/validator", methods=["GET"])
def get_validator():
    validators = Validator.query.filter_by(active=True).all()
    return Response.of_success(jsonify([validator.to_dict() for validator in validators]))


@controller.route("/validator_info", methods=["GET"])
def get_validator_info():
    data = request.get_json()
    result = get_validator_info_by_id(data['id'])
    return Response.of_success(jsonify(result))

@controller.route("/validator", methods=["POST"])
def add_validator():
    data = request.get_json()
    new_validator = Validator(code=data['code'], name=data['name'])
    db.session.add(new_validator)
    db.session.commit()
    return Response.of_success(jsonify(new_validator.to_dict()))

@controller.route("/validatorupdate", methods=["POST"])
def update_validator():
    data = request.get_json()
    validator = Validator.query.get(data['id'])
    if validator:
        validator.name = data['name']
        validator.code = data['code']
        db.session.commit()

    return Response.of_success(jsonify(validator.to_dict()))

@controller.route("/validatordelete", methods=["POST"])
def delete_validator():
    data = request.get_json()
    validator = Validator.query.get(data['id'])
    if validator:
        validator.active = False
        db.session.commit()
    return Response.of_success(None)

@controller.route("/validatorcopy", methods=["POST"])
def copy_validator():
    data = request.get_json()
    result = copy_validator_service(data)
    return Response.of_success(result)

@controller.route("/entity", methods=["POST"])
def add_entity():
    data = request.get_json()
    new_entity = Entity(validator_id=['validator_id'], code=data['code'], name=data['name'])
    db.session.add(new_entity)
    db.session.commit()
    return Response.of_success(jsonify(new_entity.to_dict()))

@controller.route("/entities", methods=["POST"])
def add_entities():
    # todo: 添加实体属性信息
    return "<p>Hello, World!</p>"

@controller.route("/entityupdate", methods=["POST"])
def update_entity():
    data = request.get_json()
    entity = Entity.query.get(data['id'])
    if entity:
        entity.name = data['name']
        entity.code = data['code']
        db.session.commit()

    return Response.of_success(jsonify(entity.to_dict()))

@controller.route("/entitydelete", methods=["POST"])
def delete_entity():
    data = request.get_json()
    entity = Entity.query.get(data['id'])
    if entity:
        entity.active = False
        db.session.commit()
    return Response.of_success(None)

@controller.route("/entityinfogenerate", methods=["POST"])
def generate_entity_info():
    data = request.get_json()
    # todo: 读取xlsx, 或者csv 文件 生成实体属性信息
    generate_entity_info_service(data)
    return Response.of_success(None)

@controller.route("/attribute", methods=["GET"])
def get_attribute():
    return "<p>Hello, World!</p>"

@controller.route("/attribute", methods=["POST"])
def add_attribute():
    data = request.get_json()
    new_attribute = Attribute(entity_id=['entity_id'], code=data['code'], name=data['name'])
    db.session.add(new_attribute)
    db.session.commit()
    return Response.of_success(jsonify(new_attribute.to_dict()))

@controller.route("/attributeupdate", methods=["POST"])
def update_attribute():
    data = request.get_json()
    attribute = Attribute.query.get(data['id'])
    if attribute:
        attribute.name = data['name']
        attribute.code = data['code']
        db.session.commit()

    return Response.of_success(jsonify(attribute.to_dict()))

@controller.route("/attributedelete", methods=["POST"])
def delete_attribute():
    data = request.get_json()
    attribute = Attribute.query.get(data['id'])
    if attribute:
        attribute.active = False
        db.session.commit()
    return Response.of_success(None)

@controller.route("/validationrule", methods=["GET"])
def get_validation_rule():
    return "<p>Hello, World!</p>"

@controller.route("/validationrule", methods=["POST"])
def add_validation_rule():
    data = request.get_json()
    new_validation_rule = ValidationRule(validator_id=['attribute_id'], type=data['type'], code=data['code'], name=data['name'])
    db.session.add(new_validation_rule)
    db.session.commit()
    return Response.of_success(jsonify(new_validation_rule.to_dict()))

@controller.route("/validationruleupdate", methods=["POST"])
def update_validation_rule():
    data = request.get_json()
    validation_rule = ValidationRule.query.get(data['id'])
    if validation_rule:
        validation_rule.type = data['type']
        validation_rule.name = data['name']
        validation_rule.code = data['code']
        db.session.commit()

    return Response.of_success(jsonify(validation_rule.to_dict()))

@controller.route("/validationruledelete", methods=["POST"])
def delete_validation_rule():
    data = request.get_json()
    validation_rule = Attribute.query.get(data['id'])
    if validation_rule:
        validation_rule.active = False
        db.session.commit()
    return Response.of_success(None)

@controller.route("/repairrule", methods=["GET"])
def get_repair_rule():
    return "<p>Hello, World!</p>"

@controller.route("/repairrule", methods=["POST"])
def add_repair_rule():
    data = request.get_json()
    new_repair_rule = RepairRule(validator_id=['attribute_id'], type=data['type'], code=data['code'], name=data['name'])
    db.session.add(new_repair_rule)
    db.session.commit()
    return Response.of_success(jsonify(new_repair_rule.to_dict()))


@controller.route("/repairruleupdate", methods=["POST"])
def update_repair_rule():
    data = request.get_json()
    repair_rule = RepairRule.query.get(data['id'])
    if repair_rule:
        repair_rule.type = data['type']
        repair_rule.name = data['name']
        repair_rule.code = data['code']
        db.session.commit()

    return Response.of_success(jsonify(repair_rule.to_dict()))

@controller.route("/repairruledelete", methods=["POST"])
def delete_repair_rule():
    data = request.get_json()
    repair_rule = RepairRule.query.get(data['id'])
    if repair_rule:
        repair_rule.active = False
        db.session.commit()
    return Response.of_success(None)

@controller.route("/importvalidationdata", methods=["POST"])
def import_validation_data():
    # todo: 生成文件备份
    # 记录时间
    return "<p>Hello, World!</p>"

@controller.route("/executevalidator", methods=["POST"])
def execute_validator():
    # todo: 获取执行器, 获取文件, 备份文件, 生成history, 生成结果,

    return "<p>Hello, World!</p>"

@controller.route("/executerepair", methods=["POST"])
def execute_repair():
    # todo: 通过选择修复的数据 执行修复, 备份文件等
    return "<p>Hello, World!</p>"


@controller.route("/downloadrepairdata", methods=["POST"])
def download_repair_data():
    # 下载结果 history
    return "<p>Hello, World!</p>"