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
    imcol = aim.ImageCollectionProcessed([aim.Image(arr) for arr in array_list])
    return imcol

@pytest.fixture()
def dummy_command(image_collection):
    dummy_command = aim.DummyCommand(image_collection.list_images[0])
    return dummy_command

def test_store_and_execute(image_collection, dummy_command):
    image_collection.store_and_execute(dummy_command)
    executed = image_collection.list_images[0].preuve_dummy_command == "J'existe !"
    stored = len(image_collection.sequence.list_commands()) == 1
    assert [executed, stored] == [True, True]

def test_store(image_collection, dummy_command):
    image_collection.store(dummy_command)
    stored = len(image_collection.sequence.list_commands()) == 1
    assert stored == True

def test_execute_last(image_collection, dummy_command):
    pass

def test_execute_all(image_collection, dummy_command):
    pass
