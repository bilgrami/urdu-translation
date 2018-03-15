# translate-helper
Given a word list in csv format, returns translations in Excel format. Though the tool can be used to translate from/to any language, the focus is especially on Indic langauges (especially Urdu).

## Translation sources
1. Google Translator
2. Bing Translator
3. *Amazon Translator  (support will be added soon)*
4. *udb.gov.pk for Urdu (support will be added soon)*

### System requirements
**Python version**: 	3.6.1+

**Third Party Python modules**: 
- googletrans
- pandas


Execute "run_first.bat" file to install dependencies

---

## Usage

### 1) Review Parameter Settings
Review "settings.json" file. 

Below are list of parameters

| Parameter Name                     	| Description                                                                                                                                                                                                                                              	| Default Value              	| Data Type 	|
|:------------------------------------	| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	| :----------------------------	| :-----------	|
| source_language                    	|  The source language code of the word list. Use a supported language code, generally consisting of its ISO 639-1 identifier. (E.g. 'en', 'ja'). In certain cases, BCP-47 codes including language + region identifiers can be used (e.g. 'zh-TW' and 'zh-CH') 	| en                    | string    	|
| target_language                    	| The target language code for the results. Use a supported language code, generally consisting of its ISO 639-1 identifier. (E.g. 'en', 'ja'). In certain cases, BCP-47 codes including language + region identifiers can be used (e.g. 'zh-TW' and 'zh-CH')    	| ur                    | string    	|
| microsoft_translator_client_secret 	| The Microsoft API Translator key. For more information, read this https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-info-overview                                                                                          	|                            	| string    	|
| word_list_file                     	| Path to word list file in CSV format. Words should be listed once per line. CSV file columns are Origin,Category                                                                                                                                         	| data\\input_data_small.csv 	| string    	|
| output_excel_file                  	| Path to output result file in Excel format.   Excel file columns are Word,Category,GoogleTranslation,BingTranslation                                                                                                                                     	| data\\output_data.xlsx     	| string    	|

### 2) Define word list
Define word list in a CSV file. The file path is specified in "word_list_file" parameter from settings.json file. Default value is "data\input_data_small.csv"

### 3) Make sure you have microsoft_translator_client_secret

### 4) Run
python translate.py
