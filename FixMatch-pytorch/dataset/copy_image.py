import os
import shutil

def copy_to_label(selected):
    all_img0 = [f for f in os.listdir('training/0') if f.endswith('png')]
    all_img1 = [f for f in os.listdir('training/1') if f.endswith('png')]

    # delete training_labeled folder
    shutil.rmtree('training_labeled')
    # create new folders
    os.mkdir('training_labeled')
    os.mkdir('training_labeled/0')
    os.mkdir('training_labeled/1')

    # selected is directory containing my hand selected 50 images
    # Goal = copy images to training_labeled/0 and training_labeled/1
    for img in os.listdir(selected):
        if img in all_img0:
            # copy to training_labeled/0
            shutil.copyfile(os.path.join(selected,img), 'training_labeled/0')
        else:
            # copy to training_labeled/1
            shutil.copyfile(os.path.join(selected,img), 'training_labeled/1')

            