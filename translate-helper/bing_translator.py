import sys
import logging

import pandas as pd
import requests
import settings
from xml.etree import ElementTree
from base_translator import BaseTranslator
from auth import AzureAuthClient


class BingTranslatorHelper(BaseTranslator):
  microsoft_bearer_token = ''
  microsoft_translator_client_secret = ''

  def __init__(self, name, source_language, target_language, settings):
    super(BingTranslatorHelper, self).__init__(name, source_language, target_language)
    self.microsoft_translator_client_secret = settings.microsoft_translator_client_secret

  def _GetMicrosoftAuthToken(self):
    auth_client = AzureAuthClient(self.microsoft_translator_client_secret)
    access_token = auth_client.get_access_token()
    return "Bearer " + access_token.decode(self.Character_Encoding) 

  def SetupTranslator(self):
    if self.microsoft_translator_client_secret:
      self.microsoft_bearer_token = self._GetMicrosoftAuthToken()
      return True
    else:
      return False

  def GetTranslation(self, text_to_translate):
    headers = {"Authorization ": self.microsoft_bearer_token}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(text_to_translate, self.target_language)
    translationData = requests.get(translateUrl, headers = headers)
    translation = ElementTree.fromstring(translationData.text.encode(self.Character_Encoding))
    return translation.text or ""
  
  def TearDownTranslator(self):
    pass 
  
  def PrintSettings(self):
    logging.info ("[%s] Settings %s" % self.name)
    logging.info ("    microsoft_translator_client_secret: %s" % self.microsoft_translator_client_secret)
    