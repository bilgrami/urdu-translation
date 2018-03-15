import json 

SOURCE_LANGUAGE = ''
TARGET_LANGUAGE = ''
MICROSOFT_TRANSLATOR_CLIENT_SECRET = ''
WORD_LIST_FILE = ''
OUTPUT_EXCEL_FILE = ''

def _read_settings(file_name):
	with open(file_name, encoding='utf-8') as fh:
		data = json.load(fh)
		return data 

def load_settings(file_name):
	global SOURCE_LANGUAGE
	global TARGET_LANGUAGE
	global MICROSOFT_TRANSLATOR_CLIENT_SECRET
	global WORD_LIST_FILE
	global OUTPUT_EXCEL_FILE

	json_settings = _read_settings(file_name)

	SOURCE_LANGUAGE = json_settings["source_language"]
	TARGET_LANGUAGE = json_settings["target_language"]
	MICROSOFT_TRANSLATOR_CLIENT_SECRET = json_settings["microsoft_translator_client_secret"]
	WORD_LIST_FILE = json_settings["word_list_file"]
	OUTPUT_EXCEL_FILE = json_settings["output_excel_file"]
