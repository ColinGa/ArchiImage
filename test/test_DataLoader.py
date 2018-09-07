import os
import json
import shutil

import pytest
import numpy as np

import archi as arc; from archi import im_proc, dal
from archi.dal import DataLoader

@pytest.fixture
def images_list_ref():
    return [np.array([[[0,0,0],       [0,0,0]],
                [[255,255,255], [255,255,255]]], dtype=np.uint8),
            np.array([[[0,0,0], [255,255,255]], 
                    [[0,0,0], [0,0,0]]], dtype=np.uint8),
            np.array([[[255,255,255], [0,0,0]], 
                    [[255,255,255], [255,255,255]]], dtype=np.uint8),
            np.array([[[255,255,255], [0,0,0]], 
                    [[0,0,0], [0,0,0]]], dtype=np.uint8)]

@pytest.yield_fixture
def temporary_dir():
    path = os.path.join("test_data", "temp_dir")
    os.mkdir(path)
    yield path
    shutil.rmtree(path)

def test_save_load_image():
    arr_ref = np.array([[[0,0,0],         [0,0,0]],
                        [[255,255,255], [255,255,255]]], dtype=np.uint8)
    directory = "test_data"
    name = "image_test_dal.png"
    path = os.path.join(directory, name)
    DataLoader.save_image(arr_ref, directory, name)
    image = DataLoader.load_image(path)
    assert np.all(arr_ref == image)

def test_load_images_as_list(images_list_ref):
    images_list = DataLoader.load_images_as_list(r"test_data/")
    res = []
    for im_ref, im in zip(images_list_ref, images_list):
        res += [np.all(im_ref == im)]
    assert np.all(res)

def test_load_images_as_generator(images_list_ref):
    images_generator_ref = (arr for arr in images_list_ref)
    images_generator = DataLoader.load_images_as_generator(r"test_data/")
    res = []
    for im_ref, im in zip(images_generator_ref, images_generator):
        res += [np.all(im_ref == im)]
    assert np.all(res)

def test_save_and_load_sequence():
    seq = im_proc.CommandSequence.Sequence([])
    dm = im_proc.ImageCommand.DummyCommand()
    cvg = im_proc.ImageCommand.ConvertToGrayCommand()
    seq.add_command(dm)
    seq.add_command(cvg)
    DataLoader.save_sequence("test_data", "json_test.json", seq)
    path = os.path.join("test_data", "json_test.json")
    seq_loaded = DataLoader.load_sequence(path)
    assert seq == seq_loaded

def test_save_images_list(images_list_ref, temporary_dir):
    DataLoader.save_images_list(images_list_ref, temporary_dir, "test_name")
