namespace java com.fuck.ccp.thift.user

struct UserInfo {
    1:i32 id,
    2:string username,
    3:string password,
    4:string realName,
    5:string mobileNumber,
    6:string email
}

service UserService {
    UserInfo getUserById(1:i32 id);

    UserInfo getUserByName(1:string username);

    void registerUser(1:UserInfo userinfo);
}