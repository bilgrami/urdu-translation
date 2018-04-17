import logging

import requests
from lxml import html

import settings
from base_translator import BaseTranslator


class HamariWebTranslatorHelper(BaseTranslator):

  def __init__(self, name, source_language, target_language, settings):
    super(HamariWebTranslatorHelper, self).__init__(name, source_language, target_language)

  def SetupTranslator(self):
    if ((self.source_language in ["en"]) and (self.target_language in ["ur"])):
      return True
    else:
      return False

  def GetTranslation(self, text_to_translate):
    translation_text = ""
    try:
      url='http://www.hamariweb.com/dictionaries/urdu-english-dictionary.aspx?eu='+text_to_translate+'&sk=true' 
      response = requests.get(url)
      tree = html.fromstring(response.content)
      result = str(tree.xpath('//meta[@name="keywords"]/@content'))
      if result:
        translation_text_list = result.split(",")
        if len(translation_text_list) > 4:
          translation_text = translation_text_list[4]
    except Exception as e:
      print("error searching for " + text_to_translate, e)
    return translation_text.strip() or ""

  def TearDownTranslator(self):
    pass 

  def PrintSettings(self):
    pass
