namespace java com.fuck.ccp.message
namespace py message.api

service MessageService {

    bool sendMobileMessage(1:string mobileNumber, 2:string message);

    bool sendEmailMessage(1:string email, 2:string message);

}