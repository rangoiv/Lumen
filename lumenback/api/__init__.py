from fastai.data.all import *
from fastai.vision.all import *
import librosa
from api.convert import convert
import warnings
sys.path.append('../')

train_path = Path("../Dataset/Dataset/IRMAS_Training_Data")
model_path = '../../models/MLBLCLA2_model'
notebook_path = "../main.ipynb"
file_path = "./api/main.py"

print("-"*30)
print(f"- Converting {notebook_path} to {file_path}")
convert(notebook_path, file_path)
print(f"- Running {file_path}")
warnings.filterwarnings('ignore')
with open(file_path) as file:
    exec(file.read())

print("- Creating model")
learn = get_learner(items=get_song_files(train_path),
                    augm=[], tfms=[ToSpec(get_spec)], arch=models.resnet18,
                    splitter=test_splitter,
                    resize=Resize((256, 156), method=ResizeMethod.Squish))
print(f"- Loading saved weights {model_path}")
learn = learn.load(model_path)
print("- MODEL LOADED!")
print("-"*30)
