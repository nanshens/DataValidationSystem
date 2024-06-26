from flask import jsonify

from common.enums import ResponseCode


class Response:
    def __init__(self, code, data, msg=""):
        self.code = code
        self.data = data
        self.msg = msg

    def to_dict(self):
        res_dict = dict()
        res_dict['code'] = self.code
        res_dict['data'] = self.data
        res_dict['msg'] = self.msg
        return res_dict

    @staticmethod
    def of_success(data, msg=""):
        return jsonify(Response(ResponseCode.Success.value, data, msg).to_dict())

    @staticmethod
    def of_fail(msg=""):
        return jsonify(Response(ResponseCode.Fail.value, None, msg).to_dict())