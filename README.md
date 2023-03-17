# kmi2122-dataset: A Collection of Korea Macroeconomic Indicators from 2021-2022 (Monthly, 24 Sequences)
## Description
This dataset merges monthly economic indicators provided by the Korean Statistical Information Service (KOSIS) into a single data frame. The data covers a total of 24 sequences from January 2021 to December 2022 and includes information in 24 columns.

To solve the problem of encoding Korean characters and having many columns in one data frame, the column names were changed to table{int}_col{int}. This change is reflected in the data, making it easy to use, as demonstrated in the following example.

This dataset provides valuable information for time series data analysis and modeling, enabling users to extract information on which indicators require more focus and predict values using several economic indicators. It is expected that this data and lagging techniques will enable the identification of the successors of economic indicators.

<br>

## Contents



- This dataset has a total of 2201 columns with 24 sequences (monthly from 2021.01 to 2022.12) as the number of columns. 
- Those 2201 columns were extracted from 57 tables.
- Missing values do not exist.
- The published statistical data were original, and no separate preprocessing was performed.

|    | file_name   | description                                 | description_in_eng                                                     |
|---:|:------------|:--------------------------------------------|:-----------------------------------------------------------------------|
|  0 | table0      | ELW 거래실적                                | ELW Trading Volume                                                     |
|  1 | table1      | ELW 투자자별 거래실적                       | ELW Investor Trading Volume                                            |
|  2 | table2      | ETF 거래실적                                | ETF Trading Volume                                                     |
|  3 | table3      | ETF 투자자별 거래실적                       | ETF Investor Trading Volume                                            |
|  4 | table4      | ETN 거래실적                                | ETN Trading Volume                                                     |
|  5 | table5      | ETN 투자자별 거래실적                       | ETN Investor Trading Volume                                            |
|  6 | table6      | KRX 100                                     | KRX 100                                                                |
|  7 | table7      | KRX 300                                     | KRX 300                                                                |
|  8 | table8      | KRX 배당수익률                              | KRX Dividend Yield                                                     |
|  9 | table9      | KRX 상장주식 거래실적                       | KRX Listed Stock Trading Volume                                        |
| 10 | table10     | KRX 상장주식 총괄                           | KRX Listed Stock Summary                                               |
| 11 | table11     | KRX 상장주식 투자자별 거래실적              | KRX Listed Stock Investor Trading Volume                               |
| 12 | table12     | KRX 주가순자산비율  PBR                     | KRX Price to Book Ratio (PBR)                                          |
| 13 | table13     | KRX 주가이익비율  PER                       | KRX Price to Earnings Ratio (PER)                                      |
| 14 | table14     | KRX 주요주가지수                            | KRX Major Price Index                                                  |
| 15 | table15     | KTOP 30                                     | KTOP 30                                                                |
| 16 | table16     | 경기종합지수 2015100   10차                 | Composite Stock Price Index 2015100 10th                               |
| 17 | table17     | 경기종합지수 2015100  구성지표 시계열  10차 | Composite Stock Price Index 2015100 Composition Index Time Series 10th |
| 18 | table18     | 기대인플레이션율 전국  월                   | Expected Inflation Rate National Monthly                               |
| 19 | table19     | 생산확산지수                                | Production Diffusion Index                                             |
| 20 | table20     | 생활물가지수 2020100                        | Consumer Price Index 2020100                                           |
| 21 | table21     | 소비자물가지수 2020100                      | Consumer Price Index Including Self-Contained Housing 2020100          |
| 22 | table22     | 월별 소비자물가 등락률                      | Monthly Consumer Price Index Fluctuation Rate                          |
| 23 | table23     | 유가증권 거래건수 및 1거래당 거래규모       | Korea Exchange Securities Trading Volume and Trading Volume per Trade  |
| 24 | table24     | 유가증권 거래실적                           | Korea Exchange Securities Trading Volume                               |
| 25 | table25     | 유가증권 산업별 시가총액                    | Korea Exchange Securities Industry Market Capitalization               |
| 26 | table26     | 유가증권 상장사 배당현황                    | Korea Exchange Securities Listed Company Dividend Status               |
| 27 | table27     | 유가증권 상장사 수익현황                    | Korea Exchange Securities Listed Company Revenue Status                |
| 28 | table28     | 유가증권 상장주식 총괄                      | Korea Exchange Securities Listed Stock Summary                         |
| 29 | table29     | 유가증권 투자자별 거래실적                  | Korea Exchange Securities Investor Trading Volume                      |
| 30 | table30     | 유가증권 프로그램매매 거래실적              | Korea Exchange Securities Program Trading Trading Volume               |
| 31 | table31     | 자가주거비포함 소비자물가지수 2020100       | Consumer Price Index Including Self-Contained Housing 2020100          |
| 32 | table32     | 지출목적별 소비자물가지수 품목포함  2020100 | Consumer Price Index by Expenditure Purpose Including Items 2020100    |
| 33 | table33     | 코스닥 150 섹터 지수                        | KOSDAQ 150 Sector Index                                                |
| 34 | table34     | 코스닥 거래실적                             | KOSDAQ Trading Volume                                                  |
| 35 | table35     | 코스닥 배당수익률                           | KOSDAQ Dividend Yield                                                  |
| 36 | table36     | 코스닥 산업별 수익현황                      | KOSDAQ Industry Revenue Status                                         |
| 37 | table37     | 코스닥 산업별 재무현황                      | KOSDAQ Industry Financial Status                                       |
| 38 | table38     | 코스닥 산업별 주가지수                      | KOSDAQ Industry Stock Price Index                                      |
| 39 | table39     | 코스닥 산업별 투자지표                      | KOSDAQ Industry Investment Indicators                                  |
| 40 | table40     | 코스닥 상장사 배당현황                      | KOSDAQ Listed Company Dividend Status                                  |
| 41 | table41     | 코스닥 상장사 수익현황                      | KOSDAQ Listed Company Revenue Status                                   |
| 42 | table42     | 코스닥 주가순자산비율  PBR                  | KOSDAQ Price to Book Ratio (PBR)                                       |
| 43 | table43     | 코스닥 주가이익비율  PER                    | KOSDAQ Price to Earnings Ratio (PER)                                   |
| 44 | table44     | 코스닥 주요주가지수                         | KOSDAQ Major Price Index                                               |
| 45 | table45     | 코스닥 지수                                 | KOSDAQ Index                                                           |
| 46 | table46     | 코스닥 투자자별 거래실적                    | KOSDAQ Investor Trading Volume                                         |
| 47 | table47     | 코스피 200 섹터 지수                        | KOSPI 200 Sector Index                                                 |
| 48 | table48     | 코스피 200 지수                             | KOSPI 200 Index                                                        |
| 49 | table49     | 코스피 배당수익률                           | KOSPI Dividend Yield                                                   |
| 50 | table50     | 코스피 산업별 주가지수                      | KOSPI Industry Stock Price Index                                       |
| 51 | table51     | 코스피 산업별 투자지표                      | KOSPI Industry Investment Indicators                                   |
| 52 | table52     | 코스피 주가순자산비율  PBR                  | KOSPI Price to Book Ratio (PBR)                                        |
| 53 | table53     | 코스피 주가이익비율  PER                    | KOSPI Price to Earnings Ratio (PER)                                    |
| 54 | table54     | 코스피 주요주가지수                         | KOSPI Major Price Index                                                |
| 55 | table55     | 코스피 지수                                 | KOSPI Index                                                            |
| 56 | table56     | 품목별 소비자물가지수 품목성질별 2020100    | Consumer Price Index by Item and Item Characteristic 2020100           |
| 57 | table57     | 품목성질별 소비자물가지수 2020100           | Consumer Price Index by Item Characteristic 2020100                    |

## What is the Korean Statistical Information Service (KOSIS)?
The Korean Statistical Information Service [(KOSIS)](https://kosis.kr/serviceInfo/kosisIntroduce.do) is a one-stop statistical service provided by the National Statistical Office. It helps users find the statistics they need by collecting key domestic, international, and North Korean statistics in one place. KOSIS contains all government-approved statistics on the economy, society, and environment from over 400 organizations. It also provides the latest statistics on international finance and economy from the IMF, Worldbank, and OECD.

Through an easy and convenient search function, various contents, and statistical explanatory data services that even the general public can understand, KOSIS allows users to quickly and accurately find the statistical data they need.
