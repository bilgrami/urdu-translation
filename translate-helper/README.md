# translate-helper
Given a word list in CSV format, returns translations in Excel (xls) format. The tool can be used to translate from/to any language, however our focus is on Indic languages (especially Urdu).

## Translation sources (Current)
1. Google Translator
2. Bing Translator

## System requirements
**Python version**: 	3.6.1+

**Third Party Python modules**: 
- googletrans
- pandas


## Setup Instructions
Execute "run_first.bat" file to install dependencies

---

## Usage

### 1) Review Settings.json File 
Below are list of parameters

| Parameter Name                     	| Description                                                                                                                                                                                                                                              	| Default Value              	| Data Type 	|
|:------------------------------------	| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	| :----------------------------	| :-----------	|
| source_language                    	| The source language code of the word list. Use a supported language code, generally consisting of its ISO 639-1 identifier. (E.g. 'en', 'ja'). In certain cases, BCP-47 codes including language + region identifiers can be used (e.g. 'zh-TW' and 'zh-CH') 	| en                    | string    	|
| target_language                    	| The target language code for the results. Use a supported language code, generally consisting of its ISO 639-1 identifier. (E.g. 'en', 'ja'). In certain cases, BCP-47 codes including language + region identifiers can be used (e.g. 'zh-TW' and 'zh-CH')    	| ur                    | string    	|
| word_list_file                     	| Path to word list file in CSV format. Words should be listed once per line. CSV file columns are Origin,Category                                                                                                                                         	| data\\input_data_small.csv 	| string    	|
| output_excel_file                  	| Path to output result file in Excel format.   Excel file columns are Word,Category,GoogleTranslation,BingTranslation                                                                                                                                     	| data\\output_data.xlsx     	| string    	|
| translators                        	| Contains the list of configured translator modules and their settings. Following attributes are required: "name", "module_name", "class_name", "enabled". Please look at GoogleTranslatorHelper and BingTranslatorHelper and associated modules for more information.   | ---							|				|
| microsoft_translator_client_secret 	| Represents Microsoft API Translator key. This setting is used by BingTranslatorHelper. For more information, read this https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-info-overview                            			|                            	| string    	|

### 2) Create input word list
Prepare word list in a CSV file. The file path is specified in "word_list_file" parameter in settings.json. Default value is "data\input_data_small.csv"

### 3) Run the program
python translate.py

---
## Future plans

### Add Translation sources 
We plan to add support for following translation sources 
1. Amazon Translator
2. udb.gov.pk for Urdu
3. HamwariWeb online dictionary (http://hamariweb.com/dictionaries/)

### Add output formats
Add support to save result in JSON format. 


