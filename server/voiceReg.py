
from oic.utils.http_util import Response
import base64
import six
from future.backports.urllib.parse import parse_qs
import zeep
from zeep import Client


VVOPS='https://vv.sestek.com/VVOperations.asmx'
userData = ['SECAS_', 'English', 'Mixed', 'my voice is my password']


class BiometricEnrollment():

    def __init__(self, get_userData,nsuccess=0,nerror=0):
        """
        :param srv: The server instance
        :return:
        """
        self.username = get_userData[0]
        self.content = get_userData[1]
        self.channel = get_userData[2]
        self.utteranceText = get_userData[3]


        self.nerrors = nerror
        self.nsuccess = nsuccess
        self.elimit = 3
        self.slimit = 3
        self.clientwsdl = Client(VVOPS+'?WSDL')

    def __call__(self):

        return self.enrollVoicePrintBegin()


    def enrollVoicePrintBegin(self,username,content,channel,x=False):

        result = 0
        result = self.clientwsdl.service.DeleteVoicePrints(username)

        result = self.clientwsdl.service.EnrollVoicePrintBeginNoResume(username, content, channel)

        a = zeep.helpers.serialize_object(result)
        if (a['ResultCode'] == 0):
            return True, False, 1
        return False, False, 1

    def enrollVoicePrintData(self,username,utteranceText,wav):

        result = 0
        result = self.clientwsdl.service.EnrollVoicePrintData(username,utteranceText, wav)
        a = zeep.helpers.serialize_object(result)

        if ( a['ResultCode'] == 0):
            self.nsuccess=self.nsuccess+1
            return True,True, 1
        elif ((a['ResultCode'] == 1) or (a['ResultCode'] == 2)):
            self.nsuccess=self.nsuccess+1
            return True, False, 1
        else:
            self.nerrors=self.nerrors+1
            return False,self.nerrors==self.elimit, 1

    def getvoiceStatus(self,username,content,channel,x=False):
        result = 0
        result = self.clientwsdl.service.GetVoicePrintStatus(username, content, channel)

        a = zeep.helpers.serialize_object(result)
        if (a['ResultCode'] == 0):
            return True, False, 1
        return False, False, 1

    def _cancel(self):

        return False

    def _success(self):

        return True