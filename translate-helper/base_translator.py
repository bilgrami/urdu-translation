# from abc import ABC
from abc import ABCMeta, abstractmethod

_CHARACTOR_ENCODING = "utf-8"

class BaseTranslator:
  __metaclass__ = ABCMeta

  Character_Encoding = _CHARACTOR_ENCODING

  def __init__(self, name, source_language, target_language, *args, **kwargs):
    self.name = name
    self.source_language = source_language
    self.target_language = target_language
    
  @abstractmethod
  def SetupTranslator(self):
    pass

  @abstractmethod
  def GetTranslation(self, text_to_translate):
    pass
  
  @abstractmethod
  def TearDownTranslator(self):
    pass 

  @abstractmethod
  def PrintSettings(self):
    pass 
