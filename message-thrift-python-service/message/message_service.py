# encoding=utf-8
from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'lyuwalle@163.com'

authCode = 'IHJVGBTTGNYEFNJA'


class MessageServiceHandler:

    def sendMobileMessage(self, mobileNumber, message):
        # 短信服务需要收费，因此打印一下即可
        print("sendMobileMessage mobile: " + mobileNumber + ", message: " + message)
        return True

    def sendEmailMessage(self, email, message):
        print("sendEmailMessage email: " + email + ", message: " + message)
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj['From'] = sender
        messageObj['To'] = email
        messageObj['Subject'] = Header('微服务测试邮件', 'utf-8')
        try:
            smtpObj = smtplib.SMTP('smtp.163.com')
            smtpObj.login(sender, authCode)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            print("邮件发送成功")
            return True
        except smtplib.SMTPException as ex:
            print("邮件发送失败")
            print(ex)
            return False




if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9090")
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thrift server start")
    server.serve()
    print("python thrift server exit")
