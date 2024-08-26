import datetime
import os

from flask import Blueprint, request, jsonify

from common.response import Response
from entity import db
from entity.executor import Executor
from entity.validator import Validator
from web.service import get_validator_info_by_id, copy_validator_service, get_executor_by_id, generate_match_entity

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
        data['name'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        validator = Validator.create_from_dto(data)
        db.session.add(validator)
    else:
        validator = Validator.query.get(id)
        validator.active = data['active']
        validator.code = data['code']
        validator.name = data['name']
        validator.entities = data['entities']

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


@controller.route("/executor/all", methods=["GET"])
def get_all_executors():
    executors = Executor.query.filter_by(active=True, validator_id=request.args.get('id')).all()
    return Response.of_success([executor.to_dict() for executor in executors])


@controller.route("/executor", methods=["GET"])
def get_executor():
    result = get_executor_by_id(request.args.get('id'))
    return Response.of_success(result)

@controller.route("/executor", methods=["POST"])
def save_executor():
    data = request.get_json()
    id = data['id']

    if str(id).startswith("NEW-") :
        executor = Executor.create_from_dto(data)
        db.session.add(executor)
    else:
        executor = Executor.query.get(id)
        executor.code = data['code']
        executor.name = data['name']
        executor.match_entities = data['match_entities']
        executor.config = data['config']

    db.session.commit()
    data = executor.to_dict()
    data['validator'] = executor.validator.to_dict(True)
    return Response.of_success(data)


@controller.route("/executor/file/entities", methods=["POST"])
def generate_entity_info():
    data = request.get_json()

    result = generate_match_entity(data['id'])
    return Response.of_success(result)


@controller.route("/attribute", methods=["GET"])
def get_attribute():
    return "<p>Hello, World!</p>"


@controller.route("/repairrule", methods=["GET"])
def get_repair_rule():
    return "<p>Hello, World!</p>"


@controller.route("/upload/validation/file", methods=["POST"])
def upload_validation_file():
    # todo: 生成文件备份
    # 记录时间
    files = request.files.getlist('file')
    path = f"./data/{request.form['id']}/"
    if not os.path.exists(path):
        os.makedirs(path)
    executor = Executor.query.get(request.form['id'])

    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    for file in files:
        if file and file.filename:
            file.save(os.path.join(path, file.filename))
            executor.files.append({"name": file.filename, "upload_time": time})
    db.session.commit()
    return Response.of_success(None)


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
