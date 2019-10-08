from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
# 初始化client,apikey作为所有请求的默认值
clnt = YunpianClient('0ebfac66e930d36dfda7447b3706d3a5')
param = {YC.MOBILE:'18290026975',YC.TEXT:'【旧书搬运工】尊敬的用户：#user#，您的订单已受理，将根据您所备注的空闲时间为您配送'}
r = clnt.sms().single_send(param)
print(r.code(),r.msg(),r.data())