import archi.im_proc as aim
from archi.im_proc import ImageCommand, CommandSequence


if __name__=="__main__":
    path = r"D:\DataUsr\cgachet\Desktop\Detection_vert\resources\images\test_algo\original"
    disp = aim.Displayer()
    disp.set_auto_close(True, 0.5)
    im_col_processed = aim.ImageCollectionProcessed(path, load_in_memory=False)
    im_col_processed.register_observer(disp)
    # im_col_processed.current_image = im_col_processed[0]
    command = ImageCommand.DummyCommand(param_test="MWALLEZ")
    dcommand = ImageCommand.DummyCommand(param_test="MWALLEZ")
    im_col_processed.store(command)
    im_col_processed.execute_all_command_all_images(cmap="gray")
