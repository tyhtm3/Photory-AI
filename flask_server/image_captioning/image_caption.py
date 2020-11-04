import pickle

class Image_caption():
    def __init__(self):
        with open('checkpoints/train3/train_captions.pickle','rb') as fr:
            self.train_captions = pickle.load(fr)