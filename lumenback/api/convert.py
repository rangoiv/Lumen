import nbformat as nbf
from nbconvert.exporters import PythonExporter
from nbconvert.preprocessors import TagRemovePreprocessor


def convert(notebook_path, file_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        the_notebook_nodes = nbf.read(f, as_version=4)

    trp = TagRemovePreprocessor()

    trp.remove_cell_tags = ("remove",)

    pexp = PythonExporter()

    pexp.register_preprocessor(trp, enabled=True)

    the_python_script, meta = pexp.from_notebook_node(the_notebook_nodes)

    with open(file_path, 'w+', encoding='utf-8') as f:
        f.writelines(the_python_script)
