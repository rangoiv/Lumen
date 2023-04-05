from fastai.data.all import *
from fastai.vision.all import *
import librosa
import re
import itertools
import matplotlib.pyplot as plot

sys.path.append('../')

train_path = Path("../Dataset/Dataset/IRMAS_Training_Data")
noise_path = Path("../Dataset/Dataset/IRMAS_Training_Data/noi")
valid_path = Path("../Dataset/Dataset/IRMAS_Validation_Data")
test_path = Path("../Dataset/Dataset/IRMAS_Test_Data")
grand_path = Path("../Dataset/Dataset")

get_song_files = FileGetter(extensions='.wav', recurse=True)

def is_IRMAS_train(pat: Path):
    return str(pat).find("IRMAS_Training_Data") != -1


def is_IRMAS_valid(pat: Path):
    return str(pat).find("IRMAS_Validation_Data") != -1


def is_IRMAS_test(pat: Path):
    return str(pat).find("IRMAS_Test_Data") != -1


def get_IRMAS_train_label(pat: Path):
    r = re.search("\[[^(\[\])]+\]", pat.name)
    if r:
        return [r.group()[1:-1]]
    return []


def get_IRMAS_valid_label(pat: Path):
    with open(os.path.splitext(str(pat))[0] + ".txt") as file:
        return file.read().split()


def get_label(pat: Path):
    if is_IRMAS_train(pat):
        return get_IRMAS_train_label(pat)
    return get_IRMAS_valid_label(pat)


def get_single_label(pat: Path):
    return get_label(pat)[:1]


n_fft = 512  # 1024
hop_length = 256  # 512
f_min = 20
f_max = 8000
sample_rate = 44100


def get_song(pat: Path):
    return librosa.load(pat, sr=None)[0]


class ToSong(Transform):
    def encodes(self, song):
        if isinstance(song, Path):
            return get_song(song)
        return song


def extend_to_3sr(song):
    aplen = sample_rate * 3 - len(song)
    if aplen < 0: aplen = 0
    song = np.concatenate([song, np.zeros(aplen, dtype="float32")])
    return song


class RandomClip(Transform):
    split_idx = 0

    def encodes(self, song):
        maxran = len(song) - sample_rate * 3 + 1
        if maxran <= 0: maxran = 1

        i = np.random.randint(maxran)
        # i=0
        song = song[i:i + sample_rate * 3]
        return extend_to_3sr(song)


class CenterClip(Transform):
    split_idx = 1

    def encodes(self, song):
        i = int((len(song) - sample_rate * 3) / 2)
        song = song[i:i + sample_rate * 3]
        return extend_to_3sr(song)


def get_stft(song):
    stft = librosa.stft(song, n_fft=n_fft, hop_length=hop_length)
    return stft


def get_spec(song):
    stft = librosa.stft(song, n_fft=n_fft, hop_length=hop_length)
    S_db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    return S_db


def get_mag(song):
    M = librosa.feature.melspectrogram(y=song, sr=sample_rate)
    M_db = librosa.power_to_db(M, ref=np.max)
    return M_db


def AccuracyMulti(tresh=0.5):
    def acc(x, y):
        return 1 - (((x > tresh).float() - y).abs()).float().mean()

    return acc


get_song_tfms = [ToSong(), RandomClip(), CenterClip()]
get_label_tfms = [get_label, MultiCategorize(), OneHotEncode()]
get_single_label_tfms = [get_single_label, Categorize()]

get_spec_tfms = [get_spec, PILImage.create]
get_mag_tfms = [get_mag, PILImage.create]


def get_subset(x, p=0.9):
    return [x[i] for i in RandomSplitter(p)(x)[0]]


class AddRandomSongs(ItemTransform):
    split_idx = 0

    def __init__(self, items, augm=[], num=1, perc=0.5):
        self.items = np.array(items)
        self.get_song_pipe = Pipeline(get_song_tfms)
        self.augm_pipe = Pipeline(augm)
        self.get_label_pipe = Pipeline(get_label_tfms)
        self.num = num
        self.perc = perc

    def get_random_songs(self, k):
        files = np.random.choice(self.items, k)
        self.augm_pipe.split_idx = 0
        self.get_song_pipe.split_idx = 0
        X = [self.augm_pipe([self.get_song_pipe(f)])[0] for f in files]
        Y = [self.get_label_pipe(f) for f in files]
        return X, Y

    def encodes(self, item):
        if np.random.rand() >= self.perc: return item
        x, y = item
        l = np.random.poisson(self.num)
        X, Y = self.get_random_songs(l)
        X.append(x)
        Y.append(y)
        x = sum(X)
        y = TensorMultiCategory([min(i, 1) for i in sum(Y)])
        return [x, y]


class PitchShift(ItemTransform):
    split_idx = 0

    def __init__(self, perc=0.5):
        self.perc = perc

    def encodes(self, item):
        if np.random.rand() >= self.perc: return item
        x = item[0]
        n_steps = np.random.rand() * 10 - 5
        x = librosa.effects.pitch_shift(x, sr=sample_rate, n_steps=n_steps)
        return [x] + item[1:]


class GaussianNoise(ItemTransform):
    split_idx = 0

    def __init__(self, perc=0.5):
        self.perc = perc

    def encodes(self, item):
        if np.random.rand() >= self.perc: return item
        x = item[0]
        noise = np.random.randn(len(x))
        x = x + 0.005 * noise
        return [x] + item[1:]


class RandomRotate(ItemTransform):
    split_idx = 0

    def __init__(self, l=1):
        self.l = l

    def encodes(self, item):
        x = item[0]
        maxran = int(self.l * sample_rate)
        i = np.random.randint(-maxran, maxran + 1)
        x = np.roll(x, i)
        return [x] + item[1:]


class RandomEdgeSilence(ItemTransform):
    split_idx = 0

    def __init__(self, l=1):
        self.l = l

    def encodes(self, item):
        x = item[0]
        maxran = int(sample_rate * self.l)
        i = np.random.randint(-maxran, maxran + 1)
        if i < 0:
            x[i:] = 0
        else:
            x[:i] = 0
        return [x] + item[1:]


class RandomAmp(ItemTransform):
    split_idx = 0

    def __init__(self, rng=[0.6, 2]):
        self.rng = rng

    def encodes(self, item):
        x = item[0]
        x = x * np.random.uniform(self.rng[0], self.rng[1])
        return [x] + item[1:]


class ToSpec(ItemTransform):
    def __init__(self, tfms):
        self.pipe = Pipeline(tfms)

    def encodes(self, item):
        x = item[0]
        return [self.pipe(x)] + item[1:]


class ShowSong(ItemTransform):
    split_idx = 0
    def __init__(self, k=10):
        self.cnt = 0
        self.k = k

    def encodes(self, item):
        return item


def get_dataset(items, splitter=RandomSplitter()):
    splits = splitter(items)
    return Datasets(items, [get_song_tfms, get_label_tfms], splits=splits)


irmas_splitter = FuncSplitter(lambda x: is_IRMAS_test(x))
irmas_splitter(get_song_files(grand_path))


def change_shape(x):
    return np.reshape(x, (len(x), 1))


class ChangeShape(ItemTransform):
    def encodes(self, item):
        x = item[0]
        return [change_shape(x)] + item[1:]


items = get_song_files(grand_path)
train_dset = get_dataset(items, irmas_splitter)
augm_items = get_song_files(train_path)  # [train_dset.items[i] for i in train_dset.splits[0]]

augm = [
    RandomRotate(l=1.5),
    RandomEdgeSilence(l=1),
    PitchShift(perc=0.5),
    GaussianNoise(perc=0.6),
    RandomAmp(rng=[0.8, 1.2])
]
after_augm = [
    AddRandomSongs(augm_items, augm=augm, num=2.5),
    ShowSong(3),
    ToSpec(get_spec_tfms),
    Resize((256, 156), method=ResizeMethod.Squish),
]


def get_dataloader(ds, augm=augm, after_augm=after_augm):
    after_item = augm + after_augm + [ToTensor(), IntToFloatTensor()]
    return ds.dataloaders(bs=64, after_item=after_item, shuffle=True)


dls = get_dataloader(train_dset)

# In[185]:

# In[191]:


# learn = vision_learner(dls, lambda **args: learn_backup.model, metrics=AccuracyMulti(tresh=0.8))
learn = load_learner('./models/laim_model.pkl', cpu=False)
# learn = vision_learner(dls, resnet18, pretrained=True)  # , metrics=AccuracyMulti(tresh=0.8))
# valid
# no valid 0.878
print(learn.predict(get_song(valid_path/"(02) dont kill the whale-1.wav")))


# In[187]:


# learn.fine_tune(4)

# In[192]: