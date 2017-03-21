import urllib
import urllib3
import socket
import md5
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
        #    print "error: no ssl support"
        #
        # self.Client = httplib.HTTPConnection(self.ServerRoot)
        self.Client = urllib3.connection_from_url(self.ServerRoot)
        # httplib
        # self.Client.request("GET", "/")
        # r1 = self.Client..getresponse()
        self.getUrlResult =  self.Client.get_url
        self.User = self.Config.getJedoxUser()
        self.Password =  self.Config.getJedoxPassword()
        self.UrlEncoder = urllib.urlencode
        self.__DBList = {}

    def getSid(self):
        CMD = 'server/login'
        Param = {'user': self.User,
                 'password': self.Password,
                 'sid': ', False'}
        for k, v in Param.iteritems():
            Param[k] = urllib.quote(v,'')
        Url = self.ServerRoot + CMD #+ '?'
        Res = self.getUrlResult(Url, Param)
        #self.Sid = Res.read().split(';')[0]
        self.Sid = Res.data.split(';')[0]
        return self.Sid

    def loadDBList(self):
        CMD = 'server/databases'
        Param = {'show_normal': self.Config.ShowNormal,
                 'show_system': self.Config.ShowSystem}
        Url = self.getUrlRequest(CMD, Param)
        Res = self.getUrlResult(Url)

        for Row in Res.data.split('\n')[:-1]:
            DB = DataBase(self, Row)
            self.__DBList[DB.getName()] = DB

    def Save(self, Param = {}):
        CMD = 'server/save'
        Url = self.getUrlRequest(CMD, Param)
        Res = self.getUrlResult(Url)
        return Res

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
        Res = self.getUrlResult(Url)

        print dir(Res)
        print Res.getheaders()
        status = Res.data.split(';')[0]
        print Res.data.split(';')[2]
        #print Res.data
        #quit()
        return
