# -*- coding: utf-8 -*-
import pandas as pd
import requests
import settings
from auth import AzureAuthClient
from googletrans import Translator as GoogleTranslator
from xml.etree import ElementTree

_INPUT_WORD_CSV_FILE = 'data\input_data.csv' # file format: word,category
_OUTPUT_WORD_EXCEL_FILE = 'data\output_data.xlsx'
_SOURCE_LANGAUGE = 'en'
_TARGET_LANGUAGE = 'ur'
_CHARACTOR_ENCODING = "utf-8"

# ------ no changes beyond this point --------

class TranslateHelper(object):
	microsoft_bearer_token = ''
	source_language = '',
	target_language = ''
	google_translator = None

	def __init__(self, source_language, target_language):
		self.source_language = source_language
		self.target_language = target_language

	def SetupTranslation(self):
		self.google_translator = GoogleTranslator()
		self.microsoft_bearer_token = self._get_microsoft_auth_token();
	
	def _get_microsoft_auth_token(self):
		auth_client = AzureAuthClient(settings.MICROSOFT_TRANSLATOR_CLIENT_SECRET)
		access_token = auth_client.get_access_token()
		return "Bearer " + access_token.decode(_CHARACTOR_ENCODING) 

	def GetMicrosoftTranslation(self, textToTranslate):
		headers = {"Authorization ": self.microsoft_bearer_token}
		translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, self.target_language)
		translationData = requests.get(translateUrl, headers = headers)
		translation = ElementTree.fromstring(translationData.text.encode(_CHARACTOR_ENCODING))
		return translation.text or ""

	def GetGoogleTranslation(self, textToTranslate):
		t = self.google_translator.translate(textToTranslate, src = self.source_language, dest = self.target_language)
		return t.text or ""

def save_to_excel(df, file_name):
	writer = pd.ExcelWriter(file_name)
	df.to_excel(writer,'Sheet1')

def save_to_csv(df, file_name):
	df.to_csv(path_or_buf=file_name, encoding=_CHARACTOR_ENCODING)

def GetTranslation(translator, words, category):
	df = pd.DataFrame()
	df['Word'] = words
	df['Category'] = category
	df['GoogleTranslation'] = list(map(translator.GetGoogleTranslation, words))
	df['BingTranslation'] = list(map(translator.GetMicrosoftTranslation, words))
	return df

def read_csv(file_name):
	columns=['Word','Category','GoogleTranslation','BingTranslation']
	df_in = pd.read_csv(file_name, names=columns, header=None, skiprows=1)
	# df_in = pd.read_csv(file_name, names=columns, header=None, skiprows=1, nrows=5)
	words = df_in['Word'].tolist()
	category = df_in['Category'].tolist()
	return words, category

def main():
	translator = TranslateHelper(source_language = _SOURCE_LANGAUGE, target_language = _TARGET_LANGUAGE)
	translator.SetupTranslation()
	words, category = read_csv(_INPUT_WORD_CSV_FILE)
	words_lower = [x.lower() for x in words]
	
	df1 = GetTranslation(translator, words, category)
	df_lowercase = GetTranslation(translator, words_lower, category)
	df_out = pd.concat([df1, df_lowercase]).sort_index()
	save_to_excel(df_out, _OUTPUT_WORD_EXCEL_FILE)
	print ("Finished")

if __name__ == "__main__":
	main()