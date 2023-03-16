# kmi2122-dataset: A Collection of Korea Macroeconomic Indicators from 2021-2022 (Monthly, 24 Sequences)
## Description
This dataset merges monthly economic indicators provided by the Korean Statistical Information Service (KOSIS) into a single data frame. The data covers a total of 24 sequences from January 2021 to December 2022 and includes information in 24 columns.

To solve the problem of encoding Korean characters and having many columns in one data frame, the column names were changed to table{int}_col{int}. This change is reflected in the data, making it easy to use, as demonstrated in the following example.

This dataset provides valuable information for time series data analysis and modeling, enabling users to extract information on which indicators require more focus and predict values using several economic indicators. It is expected that this data and lagging techniques will enable the identification of the successors of economic indicators.

<br>

## What is the Korean Statistical Information Service (KOSIS)?
The Korean Statistical Information Service [(KOSIS)](https://kosis.kr/serviceInfo/kosisIntroduce.do) is a one-stop statistical service provided by the National Statistical Office. It helps users find the statistics they need by collecting key domestic, international, and North Korean statistics in one place. KOSIS contains all government-approved statistics on the economy, society, and environment from over 400 organizations. It also provides the latest statistics on international finance and economy from the IMF, Worldbank, and OECD.

Through an easy and convenient search function, various contents, and statistical explanatory data services that even the general public can understand, KOSIS allows users to quickly and accurately find the statistical data they need.