*Copyright (c) 2023 MinWoo Park*
<br>

# KMI2122-dataset: A Collection of Korea Macroeconomic Indicators from 2021-2022 (Monthly, 24 Sequences)
![kmi2122-dataset](https://img.shields.io/badge/pypi-kmi2122-orange)
![Pypi Version](https://img.shields.io/pypi/v/kmi2122.svg)
[![Contributor Covenant](https://img.shields.io/badge/contributor%20covenant-v2.0%20adopted-black.svg)](code_of_conduct.md)
[![Python Version](https://img.shields.io/badge/python->=3.6-black.svg)](code_of_conduct.md)
![wheel](https://img.shields.io/badge/wheel-included-black)
<!-- ![Code convention](https://img.shields.io/badge/code%20convention-pep8-black) -->
The data covers a total of 24 sequences from January 2021 to December 2022 and includes information in 24 columns.

<br>

## Quick Start
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ETKhELKSwmo4YP5Cpsbx-xGmWmmurcI4?usp=sharing)  <br>
Please, check this before use. 

<br>

## Installation

```
pip install kmi2122
```

or simply download the raw dataset:
```
curl -LO https://raw.githubusercontent.com/DSDanielPark/kmi2122-dataset/master/kmi2122_dataset/dataset.json
```

Alternatively, you can use the dataset uploaded to Hugging Face as follows.
```python
from datasets import load_dataset

dataset = load_dataset("danielpark/KMI2122-v1", "csv")
df = pd.DataFrame(dataset['train'])
```

<br>

## Usage

```python
import kmi2122_dataset as kd

raw_dataset = kd.Dataset() # you can see raw dataset (dict)

kmi = kd.KMI2122()
df = kmi.get_df() # you can get a dataframe (pandas.DataFrame)
column_dict = dict(kmi.column_info()) # information of columns (dict) 
```
- tutorial: https://github.com/DSDanielPark/kmi2122-dataset/blob/main/docs/tutorial.ipynb
- file list: https://github.com/DSDanielPark/kmi2122-dataset/blob/main/docs/file_list.csv
You can check the list of KOSIS statistical files used to create the following dataframe at the above url. 

<br>

## Stats
- 24 monthly sequences from Jan, 2022 to Dec, 2023
- 2,593 Korean statistical columns from 57 tables in one dataframe

<br>

## Description
This dataset merges monthly economic indicators provided by the Korean Statistical Information Service (KOSIS) into a single data frame. The data covers a total of 24 sequences from January 2021 to December 2022 and includes information in 24 columns.

To solve the problem of encoding Korean characters and having many columns in one data frame, the column names were changed to table{int}_col{int}. This change is reflected in the data, making it easy to use, as demonstrated in the following example.

This dataset provides valuable information for time series data analysis and modeling, enabling users to extract information on which indicators require more focus and predict values using several economic indicators. It is expected that this data and lagging techniques will enable the identification of the successors of economic indicators.

<br>

## Contents
- This dataset has a total of 2593 columns with 24 sequences (monthly from 2021.01 to 2022.12) as the number of columns. 
- Those 2593 columns were extracted from 57 tables.
- Missing values do not exist.
- The published statistical data were original, and no separate preprocessing was performed.



|    | file_name   | description_in_eng                                                     |
|---:|:------------|:-----------------------------------------------------------------------|
|  0 | table0      | ELW Trading Volume                                                     |
|  1 | table1      | ELW Investor Trading Volume                                            |
|  2 | table2      | ETF Trading Volume                                                     |
|  3 | table3      | ETF Investor Trading Volume                                            |
|  4 | table4      | ETN Trading Volume                                                     |
|  5 | table5      | ETN Investor Trading Volume                                            |
|  6 | table6      | KRX 100                                                                |
|  7 | table7      | KRX 300                                                                |
|  8 | table8      | KRX Dividend Yield                                                     |
|  9 | table9      | KRX Listed Stock Trading Volume                                        |
| 10 | table10     | KRX Listed Stock Summary                                               |
| 11 | table11     | KRX Listed Stock Investor Trading Volume                               |
| 12 | table12     | KRX Price to Book Ratio (PBR)                                          |
| 13 | table13     | KRX Price to Earnings Ratio (PER)                                      |
| 14 | table14     | KRX Major Price Index                                                  |
| 15 | table15     | KTOP 30                                                                |
| 16 | table16     | Composite Stock Price Index 2015100 10th                               |
| 17 | table17     | Composite Stock Price Index 2015100 Composition Index Time Series 10th |
| 18 | table18     | Expected Inflation Rate National Monthly                               |
| 19 | table19     | Production Diffusion Index                                             |
| 20 | table20     | Consumer Price Index 2020100                                           |
| 21 | table21     | Consumer Price Index Including Self-Contained Housing 2020100          |
| 22 | table22     | Monthly Consumer Price Index Fluctuation Rate                          |
| 23 | table23     | Korea Exchange Securities Trading Volume and Trading Volume per Trade  |
| 24 | table24     | Korea Exchange Securities Trading Volume                               |
| 25 | table25     | Korea Exchange Securities Industry Market Capitalization               |
| 26 | table26     | Korea Exchange Securities Listed Company Dividend Status               |
| 27 | table27     | Korea Exchange Securities Listed Company Revenue Status                |
| 28 | table28     | Korea Exchange Securities Listed Stock Summary                         |
| 29 | table29     | Korea Exchange Securities Investor Trading Volume                      |
| 30 | table30     | Korea Exchange Securities Program Trading Trading Volume               |
| 31 | table31     | Consumer Price Index Including Self-Contained Housing 2020100          |
| 32 | table32     | Consumer Price Index by Expenditure Purpose Including Items 2020100    |
| 33 | table33     | KOSDAQ 150 Sector Index                                                |
| 34 | table34     | KOSDAQ Trading Volume                                                  |
| 35 | table35     | KOSDAQ Dividend Yield                                                  |
| 36 | table36     | KOSDAQ Industry Revenue Status                                         |
| 37 | table37     | KOSDAQ Industry Financial Status                                       |
| 38 | table38     | KOSDAQ Industry Stock Price Index                                      |
| 39 | table39     | KOSDAQ Industry Investment Indicators                                  |
| 40 | table40     | KOSDAQ Listed Company Dividend Status                                  |
| 41 | table41     | KOSDAQ Listed Company Revenue Status                                   |
| 42 | table42     | KOSDAQ Price to Book Ratio (PBR)                                       |
| 43 | table43     | KOSDAQ Price to Earnings Ratio (PER)                                   |
| 44 | table44     | KOSDAQ Major Price Index                                               |
| 45 | table45     | KOSDAQ Index                                                           |
| 46 | table46     | KOSDAQ Investor Trading Volume                                         |
| 47 | table47     | KOSPI 200 Sector Index                                                 |
| 48 | table48     | KOSPI 200 Index                                                        |
| 49 | table49     | KOSPI Dividend Yield                                                   |
| 50 | table50     | KOSPI Industry Stock Price Index                                       |
| 51 | table51     | KOSPI Industry Investment Indicators                                   |
| 52 | table52     | KOSPI Price to Book Ratio (PBR)                                        |
| 53 | table53     | KOSPI Price to Earnings Ratio (PER)                                    |
| 54 | table54     | KOSPI Major Price Index                                                |
| 55 | table55     | KOSPI Index                                                            |
| 56 | table56     | Consumer Price Index by Item and Item Characteristic 2020100           |
| 57 | table57     | Consumer Price Index by Item Characteristic 2020100                    |

<br>
The column names of the dataset have been maintained in Korean. In addition, you can check the 57 statistics file names in Korean through the key value of table_list in kmi_dataset_column_info. We apologize for the inconvenience, but we do not provide English-translated values as changing Korean to English can make it difficult for users to compare with the original data on KOSIS.

Also, if there are columns with missing values in some tables, the columns with missing values have been removed. Therefore, please note that the entire dataset does not have any missing values.

<br>

## Format

```
{
    'kmi_dataset_column_info': {'table0_col1': 'Number of trading days',
                                'table0_col10': 'Trading volume',
                                'table0_col11': 'Trading value (unit: million KRW)',
                                'table0_col12': 'Trading value (unit: million KRW)',
                                'table0_col13': 'Trading value (unit: million KRW)',
                                ...

                                'table9_date': 'Trading volume of listed stocks'
                                },
    'kmi_dataset_main': '{"date":{"0":2021.01,"1":2021.02,"2":2021.03,"3":2021.04,"4" ....}' ....}
}
```


<br>

## How to Cite
If you extend or use this work, please cite using this.
```
Data provided by The Korean Statistical Information Service(KOSIS), "KMI-2122" dataset, accessed from the 'kmi2122-dataset' repository on GitHub (https://github.com/DSDanielPark/kmi2122-dataset) on {Data Citation Date}
```

Please use this badge.
```
![kmi2122-dataset](https://img.shields.io/badge/pypi-kmi2122-blue)
```


<br>

# Further Reading

## What is the Korean Statistical Information Service (KOSIS)?
The Korean Statistical Information Service [(KOSIS)](https://kosis.kr/serviceInfo/kosisIntroduce.do) is a one-stop statistical service provided by the National Statistical Office. It helps users find the statistics they need by collecting key domestic, international, and North Korean statistics in one place. KOSIS contains all government-approved statistics on the economy, society, and environment from over 400 organizations. It also provides the latest statistics on international finance and economy from the IMF, Worldbank, and OECD.

Through an easy and convenient search function, various contents, and statistical explanatory data services that even the general public can understand, KOSIS allows users to quickly and accurately find the statistical data they need.


<br>

## DataSets
You can find datasets on the latest macroeconomic indicators for Korea from official data providers such as the Bank of Korea (https://www.bok.or.kr/) or the Korea Statistics Portal (https://kosis.kr/)

1. Blockchain datasets
    - Blockchain.com (https://www.blockchain.com/): provides blockchain transaction data for cryptocurrencies such as Bitcoin and Ethereum.
    - Coinmetrics.io (https://coinmetrics.io/): collects and analyzes various blockchain data.
    - Kaggle (https://www.kaggle.com/datasets?tags=14120-blockchain): a platform that provides various blockchain datasets.
2. Macroeconomic indicators for each country
    - International Monetary Fund (IMF) (https://www.imf.org/en/Data): provides macroeconomic indicator data for countries around the world.
    - World Bank (https://data.worldbank.org/): provides data on macroeconomic indicators, population, poverty, and more for each country.
    - OECD (https://stats.oecd.org/): provides data on macroeconomic indicators, social issues, environmental issues, and more for OECD member countries.
3. Stock datasets
    - Yahoo Finance (https://finance.yahoo.com/): provides data for US stocks, futures, options, and more.
    - Google Finance (https://www.google.com/finance): provides data for US stocks, indices, and more.
    - Investing.com (https://www.investing.com/): provides data for stocks, indices, funds, and more worldwide.


