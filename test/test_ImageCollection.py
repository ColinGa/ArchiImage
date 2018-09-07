import pytest
import numpy as np

import archi.im_proc as aim

@pytest.fixture()
def array_list():
    arr1 = np.array([[32, 14], [12, 54], [12, 54]])
    arr2 = np.array([[0, 0], [12, 1], [12, 89]])
    arr3 = np.array([[0], [12]])
    return [arr1, arr2, arr3]

@pytest.fixture()
def image_collection(array_list):
    imcol = aim.ImageCollection([aim.Image(arr) for arr in array_list])
    return imcol 

@pytest.fixture()
def image_collection_list(array_list):
    arr1, arr2, arr3 = array_list
    imcol1 = aim.ImageCollection([aim.Image(arr) for arr in [arr1, arr2, arr3]]) 
    imcol2 = aim.ImageCollection([aim.Image(arr) for arr in [arr2, arr3, arr3]])
    imcol3 = aim.ImageCollection([aim.Image(arr) for arr in [arr1, arr3, arr2]])
    imcol4 = aim.ImageCollection([aim.Image(arr) for arr in [arr1, arr2, arr3]])
    return [imcol1, imcol2, imcol3, imcol4]

def test_eq(image_collection_list):
    expected = [True, False, False, True]
    test1 = image_collection_list[0] == image_collection_list[0]
    test2 = image_collection_list[0] == image_collection_list[1]
    test3 = image_collection_list[0] == image_collection_list[2]
    test4 = image_collection_list[0] == image_collection_list[3]
    assert expected == [test1, test2, test3, test4]
