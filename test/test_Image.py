import pytest
import numpy as np

import archi.im_proc as aim

@pytest.fixture()
def image_list():
    arr1 = np.array([[32, 14], [12, 54], [12, 54]])
    arr2 = np.array([[0, 0], [12, 1], [12, 89]])
    arr3 = np.array([[0], [12]])
    arr4 = np.array([[0], [12]])
    return [aim.Image(arr) for arr in [arr1, arr2, arr3, arr4]]

def test_eq(image_list):
    expected = [True, False, False, True]
    test1 = image_list[0] == image_list[0]
    test2 = image_list[0] == image_list[1]
    test3 = image_list[0] == image_list[2]
    test4 = image_list[2] == image_list[3]
    assert expected == [test1, test2, test3, test4]
