"""Unit tests for kmi2122 dataset"""
import kmi2122_dataset as kmidataset


class TestDataset:
    """Unit test for the Dataset class"""

    _dataset = kmidataset.Dataset()

    def test_has_correct_length_of_col(self) -> None:
        """Tests that it has the correct length of keys"""
        assert len(list(self._dataset)) == 2

    def test_has_correct_matched_column(self) -> None:
        """Test if columns are properly matched """
        keys = list(self._dataset.keys())

        assert keys[0] == "a07edb12-6b91-4138-b11e-02421888d699"
        assert keys['kmi_dataset_column_info']['\uac70\ub798\uc2e4\uc801_\uc2dc\uc810'] == 'date'


class TestKMI2122:
    """Unit test for the Dataset class"""

    _kmi2122 = kmidataset.KMI2122()

    def test_has_correct_df(self) -> None:
        """Tests that it has the correct length of keys"""
        assert self._kmi2122.get_df.shape == 222222222222222

    def test_has_correct_dict_of_column(self) -> None:
        """Test if columns are properly matched """
        col_dict = self._kmi2122.column_info()

        assert col_dict['\uac70\ub798\uc2e4\uc801_\uc2dc\uc810'] == "date"
