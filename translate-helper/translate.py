# -*- coding: utf-8 -*-
import pandas as pd
import requests
import settings
from pydoc import locate
import logging
import logging.config
import importlib

_JSON_SETTINGS_FILE = 'settings.json'
_CHARACTOR_ENCODING = "utf-8"
# ------ no changes beyond this point --------

class TranslateHelper(object):
  source_language = '',
  target_language = ''
  translators = []
  
  def checkVersion(self, packages_to_check):
    
    for package in packages_to_check:
      version = importlib.util.find_spec(package)
      if not version:
        logging.error (("Missing package:", package))
        return False
    return True
    
  def __init__(self, source_language, target_language, translator_settings):
    self.source_language = source_language
    self.target_language = target_language
    self.translator_settings = translator_settings
      
  def SetupTranslators(self):
    for ts in self.translator_settings:
      if ts.enabled:
        translator = locate(ts.module_name + '.' + ts.class_name)
        translator = translator(ts.name, self.source_language, self.target_language, ts)
        if translator.SetupTranslator():
          self.translators.append(translator)
          logging.info ("[%s] Successfully setup." % ts.name)
          translator.PrintSettings()
        else:
          logging.warning ("[%s] Warning: Could not setup. Please check settings" % ts.name)

  def GetTranslation(self, words, category):
    df = pd.DataFrame()
    df['Word'] = words
    df['Category'] = category
    for translator in self.translators:
      df[translator.name] = list(map(translator.GetTranslation, words))
    return df

    
def save_to_excel(df, file_name):
  engine = 'openpyxl'
  writer = pd.ExcelWriter(file_name, engine)
  df.to_excel(writer,'Sheet1')

def save_to_csv(df, file_name):
  df.to_csv(path_or_buf=file_name, encoding=_CHARACTOR_ENCODING)

def read_csv(file_name):
  columns=['Word','Category']
  df_in = pd.read_csv(file_name, names=columns, header=None, skiprows=1)
  words = df_in['Word'].tolist()
  category = df_in['Category'].tolist()
  return words, category


def main():
  logging.info ("-" * 30)
  logging.info ("Starting translate-helper")
  translator_settings = settings.LoadSettings(_JSON_SETTINGS_FILE)
  logging.info ("Successfully read settings")
  translate_helper = TranslateHelper(
    source_language = translator_settings.source_language,
    target_language = translator_settings.target_language,
    translator_settings = translator_settings.translators
  )
  if translate_helper.checkVersion(translator_settings.required_packages):
    translate_helper.SetupTranslators()
    words, category = read_csv(translator_settings.word_list_file)
    logging.info ("Word list loaded")
    words_lower = [x.lower() for x in words]  
    df1 = translate_helper.GetTranslation(words, category)
    df2 = translate_helper.GetTranslation(words_lower, category)
    logging.info ("Translation retrieved successfully")
    df3 = pd.concat([df1, df2]).sort_index()
    save_to_excel(df3, translator_settings.output_excel_file)
    logging.info ("Output file created at [{0}]".format(translator_settings.output_excel_file))
  else:
    logging.error ("One or more required packages does not exist. Use run_first.bat to install")
  logging.info ("Finished translate-helper")
  logging.info ("-" * 30)

  
if __name__ == "__main__":
  logging.config.fileConfig('logging.conf')
  main()