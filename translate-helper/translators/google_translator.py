import logging

from googletrans import Translator as GoogleTranslator

from base_translator import BaseTranslator


class GoogleTranslatorHelper(BaseTranslator):

  def __init__(self, name, source_language, target_language, settings):
    super(GoogleTranslatorHelper, self).__init__(name, source_language, target_language)

  def SetupTranslator(self):
    self.google_translator = GoogleTranslator()
    return True

  def GetTranslation(self, text_to_translate):
    t = self.google_translator.translate(text_to_translate, src = self.source_language, dest = self.target_language)
    return t.text or ""
  
  def TearDownTranslator(self):
    pass 

  def PrintSettings(self):
    pass
