from common.enums import ResponseCode


class Response:
    def __init__(self, code, data, msg=""):
        self.code = code
        self.data = data
        self.msg = msg

    @staticmethod
    def of_success(data, msg=""):
        return Response(ResponseCode.Success.value, data, msg)

    @staticmethod
    def of_fail(msg=""):
        return Response(ResponseCode.Fail.value, None, msg)