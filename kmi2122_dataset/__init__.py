# coding=utf-8
# Copyright 2023 parkminwoo Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# # limitations under the License.


"""Korea Macroeconomic Indicators 2021-2022(monthly, 24 sequences)"""
import os
import json
import pandas as pd


_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dataset.json")


class Dataset(dict):
    """kmi2122 dataset"""
    def __init__(self, path: str = _PATH) -> None:
        """Instantiates a new Dataset object"""
        self.path = path
        with open(self.path, 'r') as j:
            self._rawdata = json.loads(j.read())
        super(Dataset, self).__init__(self._rawdata)


class KMI2122:
    """kmi2122 dataset"""

    def __init__(self, path: str = _PATH) -> None:
        """Instantiates a new ConversationDataset object."""
        self.path = path
        with open(self.path, 'r') as j:
            self._data = json.loads(j.read())

    def get_df(self):
        parsed = json.loads(self._data['kmi_dataset_main'])
        return pd.DataFrame(parsed)
    
    def column_info(self):
        return self._data['kmi_dataset_column_info']
    
    def __call__(self, *args: any, **kwds: any) -> dict:
        return self._data