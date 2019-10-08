from user.models import securityCode
from gongju.commen import get_random_id
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient

apikey = "0ebfac66e930d36dfda7447b3706d3a5" #我的apikey

TEMPLATES = {
    "REPW":"【旧书搬运工】正在进行修改密码，您的验证码是%s",
    "LOGIN":"【旧书搬运工】正在进行登录操作，您的验证码是%s",
    "REGISTER":"【旧书搬运工】欢迎使用旧书搬运工，您的手机验证码是%s。本条信息无需回复"
}

def security_code_is_exist(security_code):
    result = securityCode.objects.filter(security_code=security_code)
    if len(result) > 0:
        return True
    else:
        return False

def get_random_security_code():
    data_dict = get_random_id(start="", num_number=4)
    return data_dict["data"]

def send_security_code(mobile,security_code,securtity_name):
    # 初始化client,apikey作为所有请求的默认值
    clnt = YunpianClient(apikey)
    print(TEMPLATES[securtity_name] % (security_code))
    param = {YC.MOBILE:mobile,YC.TEXT:TEMPLATES[securtity_name] % (security_code)}
    r = clnt.sms().single_send(param)
    print(r.code(),r.data(),r.msg())
    if r.code() != 0:
        raise Exception("验证码发送失败！")