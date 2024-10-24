from .reader import Reader
from docx import Document

class Docx_Reader(Reader):
    def __init__(self, read_file):
        super().__init__(read_file)

    def open(self):
        try:
            raise Exception('Docx_Reader is still in development! Download latest version or wait for update.')
        except Exception as err:
            raise Exception('An error ocuured while opening file \''+self.file_name+'\'('+f"{type(err).__name__}: {err}"+')')

    def readline(self) -> tuple[str, dict]:
        try:
            raise Exception('Docx_Reader is still in development! Download latest version or wait for update.')
            curr_text = ''
            curr_attribs = None
        except Exception as err:
            raise Exception('Something went wrong with Docx_Reader('+f"{type(err).__name__}: {err}"+')')
        return curr_text, curr_attribs