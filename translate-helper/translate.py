# -*- coding: utf-8 -*-
import importlib
import logging
import logging.config
from pydoc import locate

import pandas as pd
import requests

import exporter
import importer
import settings

_GLOBAL_JSON_SETTINGS_FILE = 'settings/global_settings.json'
_JSON_SETTINGS_FILE = 'settings/settings.json'
# ------ no changes beyond this point --------

class TranslateHelper(object):

  def __init__(self, source_language, target_language, translator_settings):
    self.source_language = source_language
    self.target_language = target_language
    self.translator_settings = translator_settings
    self.translators = []
  
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

  def GetTranslation(self, words):
    df = pd.DataFrame()
    df['Word'] = words
    for translator in self.translators:
      df[translator.name] = list(map(translator.GetTranslation, words))
    return df


def main():
  logging.info("-" * 30)
  logging.info("Starting translate-helper")

  global_settings = settings.LoadSettings(_GLOBAL_JSON_SETTINGS_FILE)
  ts = settings.LoadSettings(_JSON_SETTINGS_FILE)
  logging.info("Successfully read settings")

  translate_helper = TranslateHelper(
    source_language = ts.source_language,
    target_language = ts.target_language,
    translator_settings = global_settings.translators
  )
  translate_helper.SetupTranslators()

  words = importer.read_csv(ts.word_list_file)
  logging.info("Word list loaded")

  df = translate_helper.GetTranslation(words)
  logging.info("Translation retrieved successfully")

  exporter.export(df, ts.output_file)
  logging.info("Output file created at [{0}]".format(ts.output_file))

  logging.info("Finished translate-helper")
  logging.info("-" * 30)


if __name__ == "__main__":
  logging.config.fileConfig('logging.conf')
  main()
