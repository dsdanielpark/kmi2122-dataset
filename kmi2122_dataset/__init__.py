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
        super(Dataset, self).__init__(json.load(open(self.path)))


class KMI2122:
    """kmi2122 dataset"""

    def __init__(self, path: str = _PATH, end_of_utterance_token: str = " ") -> None:
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