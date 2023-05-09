import nbformat as nbf
from nbconvert.exporters import PythonExporter
from nbconvert.preprocessors import TagRemovePreprocessor
import warnings
from fastai.data.all import *
from fastai.vision.all import *
import warnings
import sys

notebook_path = "../main.ipynb"
file_path = "./api/main.py"

def convert(notebook_path, file_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        the_notebook_nodes = nbf.read(f, as_version=4)
    trp = TagRemovePreprocessor()
    trp.remove_cell_tags = ("remove",)
    pexp = PythonExporter()
    pexp.register_preprocessor(trp, enabled=True)
    the_python_script, meta = pexp.from_notebook_node(the_notebook_nodes)
    with open(file_path, "w", encoding='utf-8') as file:
        file.writelines(the_python_script)

def run_only_once():
    warnings.filterwarnings('ignore')
    print("-"*30)
    print(f"- Converting {notebook_path} to {file_path}")
    convert(notebook_path, file_path)

    sys.path.append('../')
    train_path = Path("../Dataset/Dataset/IRMAS_Training_Data")
    model_path = '../../models/MLBLCLA2_model'

    print(f"- Loading model from {model_path}")

    from api.main import get_learner, ToSpec, get_spec, test_splitter, get_song_files
    learn = get_learner(items=[train_path/"cel"/"[cel][cla]0001__1.wav"],
                    augm=[], tfms=[ToSpec(get_spec)], arch=models.resnet18,
                    splitter=test_splitter,
                    resize=Resize((256, 156), method=ResizeMethod.Squish)
                    ).load(model_path)
    print("-"*30)
    return learn

