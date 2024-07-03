from flask import Blueprint, request, jsonify

from common.response import Response
from entity import db
from entity.validator import Validator
from web.service import get_validator_info_by_id, copy_validator_service, generate_entity_info_service

controller = Blueprint('controller', __name__)


@controller.route("/validator/all", methods=["GET"])
def get_all_validators():
    validators = Validator.query.filter_by(active=True).all()
    return Response.of_success([validator.to_dict() for validator in validators])


@controller.route("/validator", methods=["GET"])
def get_validator():
    result = get_validator_info_by_id(request.args.get('id'))
    return Response.of_success(result)


@controller.route("/validator", methods=["POST"])
def save_validator():
    data = request.get_json()
    id = data['id']

    if str(id).startswith("NEW-") :
        validator = Validator.create_from_dto(data)
        db.session.add(validator)
    else:
        validator = Validator.query.get(id)
        validator.active = data['active']
        validator.code = data['code']
        validator.name = data['name']
        validator.config = data['config']

    db.session.commit()
    return Response.of_success(validator.to_dict(True))


@controller.route("/validator/delete", methods=["POST"])
def delete_validator():
    data = request.get_json()
    validator = Validator.query.get(data['id'])
    if validator:
        validator.active = False
        db.session.commit()
    return Response.of_success(None)


@controller.route("/validator/copy", methods=["POST"])
def copy_validator():
    data = request.get_json()
    result = copy_validator_service(data)
    return Response.of_success(result)


@controller.route("/entityinfo/generate", methods=["POST"])
def generate_entity_info():
    data = request.get_json()
    # todo: 读取xlsx, 或者csv 文件 生成实体属性信息
    generate_entity_info_service(data)
    return Response.of_success(None)


@controller.route("/attribute", methods=["GET"])
def get_attribute():
    return "<p>Hello, World!</p>"


@controller.route("/repairrule", methods=["GET"])
def get_repair_rule():
    return "<p>Hello, World!</p>"


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
