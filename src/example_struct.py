from abc import ABCMeta, abstractmethod

class IPaloWebAPIInterface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"
    @abstractmethod
    def connect(self): raise NotImplementedError
	  @abstractmethod
    def disconnect(self): raise NotImplementedError

class IPaloWebAPIInterfaceServer:
    __metaclass__ = ABCMeta

	  @abstractmethod
    def activate_license(self): raise NotImplementedError
	
	  @abstractmethod
    def change_password(self): raise NotImplementedError
	
	  @abstractmethod
    def databases(self): raise NotImplementedError
	
	  @abstractmethod
    def info(self): raise NotImplementedError
	
	  @abstractmethod
    def licenses(self): raise NotImplementedError
	
	  @abstractmethod
    def load(self): raise NotImplementedError
	
	  @abstractmethod
    def login(self): raise NotImplementedError
	
	  @abstractmethod
    def logout(self): raise NotImplementedError
	
	  @abstractmethod
    def save(self): raise NotImplementedError
	
	  @abstractmethod
    def shutdown(self): raise NotImplementedError
	
	  @abstractmethod
    def user_info(self): raise NotImplementedError
		
	
class IPaloWebAPIInterfaceDatabase:
    __metaclass__ = ABCMeta
	
	  @abstractmethod
    def create(self): raise NotImplementedError
	
	  @abstractmethod
    def cubes(self): raise NotImplementedError
	
	  @abstractmethod
    def destroy(self): raise NotImplementedError
	
	  @abstractmethod
    def dimensions(self): raise NotImplementedError
	
	  @abstractmethod
    def info(self): raise NotImplementedError
	
	  @abstractmethod
    def load(self): raise NotImplementedError
	
	  @abstractmethod
    def rename(self): raise NotImplementedError
	
	  @abstractmethod
    def save(self): raise NotImplementedError
	
	  @abstractmethod
    def unload(self): raise NotImplementedError
	
	
class IPaloWebAPIInterfaceDimension:
    __metaclass__ = ABCMeta
	
	  @abstractmethod
    def clear(self): raise NotImplementedError
	
	  @abstractmethod
    def create(self): raise NotImplementedError
	
	  @abstractmethod
    def cubes(self): raise NotImplementedError
	
	  @abstractmethod
    def destroy(self): raise NotImplementedError
	
	  @abstractmethod
    def dfilter(self): raise NotImplementedError
	
	  @abstractmethod
    def element(self): raise NotImplementedError
	
	  @abstractmethod
    def elements(self): raise NotImplementedError
	
	  @abstractmethod
    def info(self): raise NotImplementedError
	
	  @abstractmethod
    def rename(self): raise NotImplementedError			
	

class IPaloWebAPIInterfaceElement:
    __metaclass__ = ABCMeta
	
	  @abstractmethod
    def append(self): raise NotImplementedError
	
	  @abstractmethod
    def create(self): raise NotImplementedError
	
	  @abstractmethod
    def create_bulk(self): raise NotImplementedError
	
	  @abstractmethod
    def destroy(self): raise NotImplementedError
	
	  @abstractmethod
    def destroy_bulk(self): raise NotImplementedError
	
	  @abstractmethod
    def info(self): raise NotImplementedError
	
	  @abstractmethod
    def move(self): raise NotImplementedError
	
	  @abstractmethod
    def move_bulk(self): raise NotImplementedError
	
	  @abstractmethod
    def rename(self): raise NotImplementedError
	
	  @abstractmethod
    def replace(self): raise NotImplementedError
	
	  @abstractmethod
    def replace_bulk(self): raise NotImplementedError
	

class IPaloWebAPIInterfaceCube:
    __metaclass__ = ABCMeta

	  @abstractmethod
    def clear(self): raise NotImplementedError
	
	  @abstractmethod
    def clear_cache(self): raise NotImplementedError
	
	  @abstractmethod
    def commit(self): raise NotImplementedError
	
	  @abstractmethod
    def convert(self): raise NotImplementedError
	
	  @abstractmethod
    def create(self): raise NotImplementedError
	
	  @abstractmethod
    def destroy(self): raise NotImplementedError
	
	  @abstractmethod
    def info(self): raise NotImplementedError
	
	  @abstractmethod
    def load(self): raise NotImplementedError
	
	  @abstractmethod
    def lock(self): raise NotImplementedError
	
	  @abstractmethod
    def locks(self): raise NotImplementedError
	
	  @abstractmethod
    def rename(self): raise NotImplementedError
	
	  @abstractmethod
    def rollback(self): raise NotImplementedError
	
	  @abstractmethod
    def rules(self): raise NotImplementedError
	
	  @abstractmethod
    def save(self): raise NotImplementedError
	
	  @abstractmethod
    def unload(self): raise NotImplementedError
	
	
class IPaloWebAPIInterfaceCell:
    __metaclass__ = ABCMeta

	  @abstractmethod
    def area(self): raise NotImplementedError
	
	  @abstractmethod
    def copy(self): raise NotImplementedError
	
	  @abstractmethod
    def drillthrough(self): raise NotImplementedError
	
	  @abstractmethod
    def export(self): raise NotImplementedError
	
	  @abstractmethod
    def goalseek(self): raise NotImplementedError
	
	  @abstractmethod
    def replace(self): raise NotImplementedError
	
	  @abstractmethod
    def replace_bulk(self): raise NotImplementedError
	
	  @abstractmethod
    def value(self): raise NotImplementedError
	
	  @abstractmethod
    def values(self): raise NotImplementedError
	
	
class IPaloWebAPIInterfaceEvents:
    __metaclass__ = ABCMeta
	
	  @abstractmethod
    def begin(self): raise NotImplementedError
	
	  @abstractmethod
    def end(self): raise NotImplementedError
		

class IPaloWebAPIInterfaceRules:
    __metaclass__ = ABCMeta
	
	  @abstractmethod
    def create(self): raise NotImplementedError
	
	  @abstractmethod
    def destroy(self): raise NotImplementedError
	
	  @abstractmethod
    def functions(self): raise NotImplementedError
	
	  @abstractmethod
    def info(self): raise NotImplementedError
	
	  @abstractmethod
    def modify(self): raise NotImplementedError
	
	  @abstractmethod
    def parse(self): raise NotImplementedError
		

class IPaloWebAPIInterfaceSupervisionServer:
    __metaclass__ = ABCMeta
	
	  @abstractmethod
    def info(self): raise NotImplementedError
	
	  @abstractmethod
    def restart(self): raise NotImplementedError
	
	
class PaloWebAPIErrorCodes(object):
    PALO_ERRORCODE_1 =	"unknown"
    PALO_ERRORCODE_2 =	"internal error"
    PALO_ERRORCODE_1000 = "identifier not found"
    PALO_ERRORCODE_1001 = "invalid filename"
    PALO_ERRORCODE_1002 = "cannot create directory"
    PALO_ERRORCODE_1003 = "cannot rename file"
    PALO_ERRORCODE_1004 = "authorization failed"
    PALO_ERRORCODE_1005 = "invalid type"
    PALO_ERRORCODE_1006 = "invalid coordinates"
    PALO_ERRORCODE_1007 = "conversion failed"
    PALO_ERRORCODE_1008 = "file not found"
    PALO_ERRORCODE_1009 = "not authorized for operation"
    PALO_ERRORCODE_1010 = "corrupt file"
    PALO_ERRORCODE_1011 = "already within event"
    PALO_ERRORCODE_1012 = "not within event"
    PALO_ERRORCODE_1013 = "invalid permission entry"
    PALO_ERRORCODE_1014 = "invalid server path"
    PALO_ERRORCODE_1015 = "invalid session"
    PALO_ERRORCODE_1016 = "missing parameter"
    PALO_ERRORCODE_1017 = "server token outdated"
    PALO_ERRORCODE_1018 = "invalid splash mode"
    PALO_ERRORCODE_1019 = "worker authorization failed"
    PALO_ERRORCODE_1020 = "worker error"
    PALO_ERRORCODE_1021 = "api call not implemented"
    PALO_ERRORCODE_1022 = "insecure communication disabled"
    PALO_ERRORCODE_1023 = "not enough memory"
    PALO_ERRORCODE_1024 = "ssl failed"
    PALO_ERRORCODE_1025 = "gpu server not enabled"
    PALO_ERRORCODE_1026 = "invalid string"
    PALO_ERRORCODE_1027 = "invalid version"
    PALO_ERRORCODE_1028 = "invalid function"
    PALO_ERRORCODE_1029 = "invalid expand type"
    PALO_ERRORCODE_1030 = "invalid function"
    PALO_ERRORCODE_1031 = "invalid area"
    PALO_ERRORCODE_1032 = "SSO authentication failed"
    PALO_ERRORCODE_1033 = "copy operation failed"
    PALO_ERRORCODE_1034 = "zip operation failed"
    PALO_ERRORCODE_2000 = "invalid database name"
    PALO_ERRORCODE_2001 = "database not found"
    PALO_ERRORCODE_2002 = "database not loaded"
    PALO_ERRORCODE_2003 = "database not saved"
    PALO_ERRORCODE_2004 = "database still loaded"
    PALO_ERRORCODE_2005 = "database name in use"
    PALO_ERRORCODE_2006 = "database is not deletable"
    PALO_ERRORCODE_2007 = "database in not renamable"
    PALO_ERRORCODE_2008 = "database token outdated"
    PALO_ERRORCODE_2009 = "invalid database type"
    PALO_ERRORCODE_2010 = "database backup error"
    PALO_ERRORCODE_3000 = "dimension empty"
    PALO_ERRORCODE_3001 = "dimension already exists"
    PALO_ERRORCODE_3002 = "dimension not found"
    PALO_ERRORCODE_3003 = "invalid dimension name"
    PALO_ERRORCODE_3004 = "dimension is not changable"
    PALO_ERRORCODE_3005 = "dimension name in use"
    PALO_ERRORCODE_3006 = "dimension in use"
    PALO_ERRORCODE_3007 = "dimension not deletable"
    PALO_ERRORCODE_3008 = "dimension not renamable"
    PALO_ERRORCODE_3009 = "dimension token outdated"
    PALO_ERRORCODE_3010 = "dimension is locked"
    PALO_ERRORCODE_4000 = "element already exists"
    PALO_ERRORCODE_4001 = "cirular reference"
    PALO_ERRORCODE_4002 = "element name in use"
    PALO_ERRORCODE_4003 = "element name not unique"
    PALO_ERRORCODE_4004 = "element not found"
    PALO_ERRORCODE_4005 = "element is no child"
    PALO_ERRORCODE_4006 = "invalid element name"
    PALO_ERRORCODE_4007 = "invalid element offset"
    PALO_ERRORCODE_4008 = "invalid element type"
    PALO_ERRORCODE_4009 = "invalid element position"
    PALO_ERRORCODE_4010 = "element not deletable"
    PALO_ERRORCODE_4011 = "element not renamable"
    PALO_ERRORCODE_4012 = "element not changable"
    PALO_ERRORCODE_4013 = "invalid mode"
    PALO_ERRORCODE_5000 = "cube not found"
    PALO_ERRORCODE_5001 = "invalid cube name"
    PALO_ERRORCODE_5002 = "cube not loaded"
    PALO_ERRORCODE_5003 = "cube empty"
    PALO_ERRORCODE_5004 = "cube not saved"
    PALO_ERRORCODE_5005 = "splash disabled"
    PALO_ERRORCODE_5006 = "copy path must be numeric"
    PALO_ERRORCODE_5007 = "invalid copy value"
    PALO_ERRORCODE_5008 = "cube name in use"
    PALO_ERRORCODE_5009 = "cube is not deletable"
    PALO_ERRORCODE_5010 = "cube is not renamable"
    PALO_ERRORCODE_5011 = "cube token outdated"
    PALO_ERRORCODE_5012 = "splashing is not possible"
    PALO_ERRORCODE_5013 = "cube lock not found"
    PALO_ERRORCODE_5014 = "wrong user for locked area"
    PALO_ERRORCODE_5015 = "could not create lock"
    PALO_ERRORCODE_5016 = "is blocked because of a locked area"
    PALO_ERRORCODE_5017 = "not enough rollback capacity"
    PALO_ERRORCODE_5018 = "goalseek error"
    PALO_ERRORCODE_5019 = "cube is system cube"
    PALO_ERRORCODE_5020 = "copy operation not possible"
    PALO_ERRORCODE_5021 = "invalid cube type"
    PALO_ERRORCODE_5022 = "defragmentation error"
    PALO_ERRORCODE_6000 = "legacy error"
    PALO_ERRORCODE_6001 = "legacy error"
    PALO_ERRORCODE_6002 = "legacy error"
    PALO_ERRORCODE_6003 = "legacy error"
    PALO_ERRORCODE_6004 = "legacy error"
    PALO_ERRORCODE_6005 = "legacy error"
    PALO_ERRORCODE_6006 = "legacy error"
    PALO_ERRORCODE_6007 = "legacy error"
    PALO_ERRORCODE_6008 = "legacy error"
    PALO_ERRORCODE_6009 = "legacy error"
    PALO_ERRORCODE_6010 = "legacy error"
    PALO_ERRORCODE_7000 = "illegal worker response"
    PALO_ERRORCODE_7001 = "invalid worker operation"
    PALO_ERRORCODE_8001 = "parse error in rule"
    PALO_ERRORCODE_8002 = "rule not found"
    PALO_ERRORCODE_8003 = "rule has circular reference"
    PALO_ERRORCODE_8004 = "division by zero"
    PALO_ERRORCODE_9000 = "Object is not checked out"
    PALO_ERRORCODE_9001 = "Object is already checked out"
    PALO_ERRORCODE_9002 = "Commit failed."
    PALO_ERRORCODE_10000 = "read request canceled on GPU"
    PALO_ERRORCODE_10001 = "write request canceled on GPU"
    PALO_ERRORCODE_10002 = "cuda runtime api error"
    PALO_ERRORCODE_10003 = "GPU memory full"
    PALO_ERRORCODE_11000 = "job stopped"
    PALO_ERRORCODE_11001 = "invalid job/session command received"
    PALO_ERRORCODE_12000 = "license expired"
    PALO_ERRORCODE_12001 = "no valid license found"
    PALO_ERRORCODE_12002 = "no free named license"
    PALO_ERRORCODE_12003 = "no license key specified"
    PALO_ERRORCODE_12004 = "no activation code specified"
    PALO_ERRORCODE_12005 = "activation code invalid"
    PALO_ERRORCODE_12006 = "license already activated"
    PALO_ERRORCODE_12007 = "no free concurrent license"
    PALO_ERRORCODE_12008 = "license API not supported"

class PaloWebAPI(IPaloWabAPIInterface):
    def connect(self):
        print 'Hello, World 1!'
		
	  def disconnect(self):
        print 'Hello, World 2!'
		
	  def version(self):
        print 'Palo Server 5.1'
		
# Beispiel
class MyPaloClient(object):

    def __init__(self, server):
        if not isinstance(server, IPaloWabAPIInterface): raise Exception('Bad interface')
        if not IPaloWabAPIInterface.version() == '1.0': raise Exception('Bad revision')

        self._server = server


    def client_test(self):
        self._server.connect()
        self._server.version()		
        self._server.disconnect()
