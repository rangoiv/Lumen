from fastai.data.all import *
from fastai.vision.all import *
from IPython.utils import io
import librosa
sys.path.append('../')

train_path = Path("C:/Users/Ivkalu/Documents/LumenDataset/Dataset/IRMAS_Training_Data")

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
    aplen = sample_rate*3 - len(song)
    if aplen < 0: aplen = 0
    song = np.concatenate([song, np.zeros(aplen, dtype="float32")])
    return song
class RandomClip(Transform):
    split_idx=0
    def encodes(self, song):
        maxran = len(song)-sample_rate*3 + 1
        if maxran <= 0: maxran = 1

        i = np.random.randint(maxran)
        # i=0
        song = song[i:i+sample_rate*3]
        return extend_to_3sr(song)
        
class CenterClip(Transform):
    split_idx=1
    def encodes(self, song):
        i = int((len(song) - sample_rate*3) / 2)
        song = song[i:i+sample_rate*3]
        return extend_to_3sr(song)

random_clip = RandomClip().encodes
center_clip = CenterClip().encodes
def get_spec(song):
    stft = librosa.stft(song, n_fft=n_fft, hop_length=hop_length)
    S_db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    return S_db
class ToSpec(ItemTransform):
    def __init__(self):
        self.pipe = Pipeline([get_spec, PILImage.create])
    def encodes(self, item):
        x = item[0]
        return [self.pipe(x)] + item[1:]
def AccuracyMulti(tresh=0.5):
    def acc(x, y):
        return 1 - (((x > tresh).float() - y).abs()).float().mean()
    return acc
get_song_tfms = [ToSong(), RandomClip(), CenterClip()]
get_label_tfms = [get_label, MultiCategorize(), OneHotEncode()]
def get_dataset(items, splitter=RandomSplitter()):
    splits = splitter(items)
    return Datasets(items, [get_song_tfms, get_label_tfms], splits=splits)
splitter = FuncSplitter(lambda x: is_IRMAS_test(x))
items = get_song_files(train_path)
train_dset = get_dataset(items)

after_augm = [
    ToSpec(),
    Resize((256, 156), method=ResizeMethod.Squish),
]

def get_dataloader(ds, after_augm=after_augm):
    after_item = after_augm + [ToTensor(), IntToFloatTensor()]
    return ds.dataloaders(bs=64, after_item=after_item, shuffle=True)

dls = get_dataloader(train_dset)
learn = vision_learner(dls, resnet18, pretrained=True)
learn.load('MLBLCLA_model');

def get_sl_windows(song, step=sample_rate):
    ran = range(0, len(song)-sample_rate-step, step)
    if len(ran) == 0: yield extend_to_3sr([0])
    for i in ran: 
        yield extend_to_3sr(song[i:i+sample_rate*3])
def predict(learn, song, step=sample_rate, tresh=0.8, perc=0.25):
    instr = np.zeros(len(learn.dls.vocab))
    for n, sl in enumerate(get_sl_windows(song)):
        with io.capture_output() as captured:
            instr[learn.predict(sl)[1] > tresh] += 1
    return learn.dls.vocab[instr > (n+1)*perc]

print("MODEL LOADED!")