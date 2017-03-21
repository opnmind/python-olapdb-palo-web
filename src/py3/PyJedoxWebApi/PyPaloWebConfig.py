# -*- coding: utf-8 -*-
from __future__ import print_function

import md5

class PyJedoxWebConfig(object):
    """
    Configuration Class
    Contains Configuration Info
    """

    def __init__(self):
        """
        Private Constructor Method
        self = Object pointer
        """

        self.__JedoxHost='127.0.0.1'
        self.__JedoxPort='7777'
        self.__JedoxUser='admin'
        self.__JedoxPassword='admin'
        self.__useProxy = False
        self.__ProxyUrl = 'http://proxy:port/'
        self.__ShowNormal = 1
        self.__ShowSystem = 0
        self.__DatawarehouseAliasName = 'KeyDW'

    def getJedoxHost(self):
        return self.__JedoxHost

    def getJedoxPort(self):
        return self.__JedoxPort

    def getJedoxUser(self):
        return self.__JedoxUser

    def getJedoxPassword(self):
        return md5.new(self.__JedoxPassword).hexdigest()

    def getProxyUrl(self):
        return self.__ProxyUrl

    def useProxy(self):
        return self.__useProxy

    def getDatawarehouseAliasName(self):
        return self.__DatawarehouseAliasName

    def _setShowNormal(self, Val = True):
        self.__ShowNormal = 1 if Val else 0

    def _getShowNormal(self, Val = True):
        return self.__ShowNormal

    def _setShowSystem(self, Val = False):
        self.__ShowSystem = 1 if Val else 0

    def _getShowSystem(self, Val = False):
        return self.__ShowSystem

    ShowNormal = property(_getShowNormal, _setShowNormal)
    ShowSystem = property(_getShowSystem, _setShowSystem)
