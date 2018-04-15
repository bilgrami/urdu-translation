# translate-helper
-----

The tool can be used to translate from/to any language. Our current focus is on Indic languages (especially Urdu).
Input Word list is provided in CSV format, and output translation is returned in Json/Csv/Excel (xls) format.

## Translation sources (Current)
----
1. Google Translator
2. Bing Translator

## Setup Instructions
----
Execute "run_first.bat" file to install dependencies



## Usage
----

### 1) Review settings/settings.json File 

Below are list of parameters

| Parameter Name                     	| Description                                                                                                                                                                                                                                              	            |
|:-----------------------------------	| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source_language                    	| The source language code of the word list. Use a supported language code, generally consisting of its ISO 639-1 identifier. (E.g. 'en', 'ja'). In certain cases, BCP-47 codes including language + region identifiers can be used (e.g. 'zh-TW' and 'zh-CH') 	        |
| target_language                    	| The target language code for the results. Use a supported language code, generally consisting of its ISO 639-1 identifier. (E.g. 'en', 'ja'). In certain cases, BCP-47 codes including language + region identifiers can be used (e.g. 'zh-TW' and 'zh-CH')           |
| word_list_file                     	| Path to word list file in CSV format. Words should be listed once per line. CSV file columns are Origin,Category                                                                                                                                         	            |
| output_file                         | Path to output file. File format can be csv, json or xls                                                                                                                                                                                                              |
| required_packages                   | list of packages that need to installed prior to running this program                                                                                                                                                                                                 |

### 2) Review settings/global_settings.json File (optional)

Use settings/global_settings.json to configure translators. Below are list of parameters

| Parameter Name                     	| Description                                                                                                                                                                                                                                              	              |
|:------------------------------------	| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| translators                        	| Contains the list of configured translator modules and their settings. Following attributes are required: "name", "module_name", "class_name", "enabled". Please look at GoogleTranslatorHelper and BingTranslatorHelper and associated modules for more information.   |
| microsoft_translator_client_secret 	| Represents Microsoft API Translator key. This setting is used by BingTranslatorHelper. For more information, read this https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-info-overview                            			                  |

### 3) Create input word list
Prepare word list in a CSV file. The file path is specified in "word_list_file" parameter in settings.json. Default value is "data\input_data_small.csv"

## Running the program
----

```python translate.py```

Check ./data folder for the output file as specified in "output_file" parameter in settings.json.


## To Do
----
### Add more Urdu Translation sources 

We plan to add support for following translation sources 

1. Urdu Dictionary Board of Pakistan(http://udb.gov.pk)
2. HamwariWeb Online dictionary (http://hamariweb.com/dictionaries)