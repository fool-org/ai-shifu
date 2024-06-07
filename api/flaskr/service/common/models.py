# Desc: Common models for the application
class AppException(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.code = status_code
        self.payload = payload
    def __json__(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['code'] = self.code
        return rv
    def __str__(self):
        return self.message
    def __html__(self):
        return self.__json__()




ERROR_CODE = {
    'USER_NOT_FOUND': 1001,
    'USER_ALREADY_EXISTS': 1002,
    'USER_PASSWORD_ERROR': 1003,
    'USER_NOT_LOGIN': 1004,
    'USER_TOKEN_EXPIRED': 1005,
    'OLD_PASSWORD_ERROR': 1006,
    'RESET_PWD_CODE_EXPIRED': 1007,
    'RESET_PWD_CODE_ERROR': 1008,
    'UNKNOWN_ERROR': 9999,
    'PARAMS_ERROR': 2001
}

ERROR_MESSAGE = {
    'USER_NOT_FOUND': '没有找到用户1',
    'USER_ALREADY_EXISTS': '用户已经存在',
    'USER_PASSWORD_ERROR': '用户密码错误',
    'USER_NOT_LOGIN': '用户没有登录',
    'USER_TOKEN_EXPIRED': '用户token过期',
    'OLD_PASSWORD_ERROR': '旧密码错误',
    'RESET_PWD_CODE_EXPIRED': '重置密码验证码过期',
    'RESET_PWD_CODE_ERROR': '重置密码验证码错误',
    'UNKNOWN_ERROR': '未知错误',
    'PARAMS_ERROR': '参数错误:{param_message}'
}

USER_NOT_FOUND = AppException(ERROR_MESSAGE['USER_NOT_FOUND'], ERROR_CODE['USER_NOT_FOUND'])
USER_ALREADY_EXISTS = AppException(ERROR_MESSAGE['USER_ALREADY_EXISTS'], ERROR_CODE['USER_ALREADY_EXISTS'])
USER_PASSWORD_ERROR = AppException(ERROR_MESSAGE['USER_PASSWORD_ERROR'], ERROR_CODE['USER_PASSWORD_ERROR'])
USER_NOT_LOGIN = AppException(ERROR_MESSAGE['USER_NOT_LOGIN'], ERROR_CODE['USER_NOT_LOGIN'])
USER_TOKEN_EXPIRED = AppException(ERROR_MESSAGE['USER_TOKEN_EXPIRED'], ERROR_CODE['USER_TOKEN_EXPIRED'])
OLD_PASSWORD_ERROR = AppException(ERROR_MESSAGE['OLD_PASSWORD_ERROR'], ERROR_CODE['OLD_PASSWORD_ERROR'])
RESET_PWD_CODE_EXPIRED = AppException(ERROR_MESSAGE['RESET_PWD_CODE_EXPIRED'], ERROR_CODE['RESET_PWD_CODE_EXPIRED'])
RESET_PWD_CODE_ERROR = AppException(ERROR_MESSAGE['RESET_PWD_CODE_ERROR'], ERROR_CODE['RESET_PWD_CODE_ERROR'])
UNKNOWN_ERROR = AppException(ERROR_MESSAGE['UNKNOWN_ERROR'], ERROR_CODE['UNKNOWN_ERROR'])

def raise_param_error(param_message):
    raise AppException(ERROR_MESSAGE['PARAMS_ERROR'].format(param_message=param_message), ERROR_CODE['PARAMS_ERROR'])



