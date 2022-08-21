package com.fuck.ccp.user.service;

import com.fuck.ccp.thift.user.UserInfo;
import com.fuck.ccp.thift.user.UserService;
import org.apache.thrift.TException;

/**
 * @author: Lyuwalle  @date: 2022/08/21 21:02
 */
public class UserServiceImpl implements UserService.Iface {

    @Override
    public UserInfo getUserById(int id) throws TException {
        return null;
    }

    @Override
    public UserInfo getUserByName(String username) throws TException {
        return null;
    }

    @Override
    public void registerUser(UserInfo userinfo) throws TException {

    }
}
