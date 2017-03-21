# -*- coding: utf-8 -*-
from __future__ import print_function

import requests
import socket
from hashlib import md5
import ssl
import urllib
import urllib3
from PyJedoxWebApi.DataBase import DataBase
from PyJedoxWebApi import Dimension
from PyJedoxWebApi.PyJedoxWebConfig import PyJedoxWebConfig


USE_PROXY = False

class PyJedoxWeb():
    def __init__(self, ServerHost = False, User = False, Password = False):

        self.Config = PyJedoxWebConfig()
        self.useProxy = USE_PROXY

        self.ProxyUrl = self.Config.getProxyUrl()
        self.ServerHost = ServerHost if ServerHost else self.Config.getJedoxHost()
        self.ServerPort = self.Config.getJedoxPort()
        self.ServerRoot = "http://%s:%s/" % (self.ServerHost, self.ServerPort)
        # depreciated: urllib.FancyURLopener({'http': self.ProxyUrl}) if self.useProxy else
        #
        # To verify if SSL is enabled, try:
        # >>> import socket
        # >>> socket.ssl
        # <function ssl at 0x4038b0>
        #
        #try:
        #    import socket
        #    socket.ssl
        #except ImportError:
        #    print("error: no ssl support")
        #
        self.Client = urllib3.connection_from_url(self.ServerRoot)
        # get_url -> request(request(method, url, fields=None, headers=None, **urlopen_kw)
        self.getUrlResult =  self.Client.request('GET', '/')
        self.User = self.Config.getJedoxUser()
        self.Password = self.Config.getJedoxPassword()
        self.UrlEncoder = urllib.parse.urlencode
        self.__DBList = {}

    def getSid(self):
        CMD = 'server/login'
        Param = {'user': self.User,
                 'password': self.Password,
                 'sid': ', False'}
        for k, v in Param.items():
            Param[k] = urllib.parse.quote(v,'')

        Url = self.ServerRoot + CMD #+ '?'
        #print(Url)
        #print(Param)
        #Res = self.getUrlResult(Url, Param)
        r = self.Client.request('GET', Url, Param)
        if r.status == 200:
            self.Sid = r.data.decode('utf-8').split(';')[0]
            return self.Sid
        else:
            return Null;

    def loadDBList(self):
        CMD = 'server/databases'
        Param = {'show_normal': self.Config.ShowNormal,
                 'show_system': self.Config.ShowSystem}
        Url = self.getUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)

        for Row in r.data.decode('utf-8').split('\n')[:-1]:
            DB = DataBase(self, Row)
            self.__DBList[DB.getName()] = DB

    def Save(self, Param = {}):
        CMD = 'server/save'
        Url = self.getUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r

    def getDB(self, DBName):
        return self.__DBList[DBName]

    def getUrlRequest(self, CMD, Param):
        # self.ServerRoot + CMD + '?sid=' + self.Sid + '&' + self.UrlEncoder(Param)
        return self.ServerRoot + CMD + '?sid=' + self.Sid + '&' + self.UrlEncoder(Param)
        ##return '%s?sid=%s&%s' % (self.ServerRoot + CMD, self.Sid, self.UrlEncoder(Param))


    def CreateDatabase(self, DBName, DBType = 0):
        CMD = 'database/create'
        Param = {'type': DBType,
                 'new_name': DBName }
        # http://127.0.0.1:7777/database/create?sid=FdN01aRub15uP70uB3U1Q9bpw8ppT5lp&new_name=DBname&type=0
        # 2;"DBname";13;15;1;0;1868503793;
        # 2005;"database name in use";"database name is already in use";"parameter 'name' value 'DBname'";
        # 1015;"invalid session";"wrong session identifier";
        Url = self.ServerRoot + CMD + '?sid=' + self.Sid + '&' + self.UrlEncoder(Param)
        r = self.Client.request('GET', Url)
        status = r.data.decode('utf-8').split(';')[0]
        print(r.data.decode('utf-8').split(';')[2])
        #quit()
        return
