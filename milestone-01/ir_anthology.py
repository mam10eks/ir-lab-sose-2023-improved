import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple
from ir_datasets.datasets.base import Dataset

class IrAnthologyDocument(NamedTuple):
    doc_id: str
    abstract: str
    title: str
    authors: list
    year: str
    booktitle: str

    def default_text(self):
        return self.title + ' ' + self.abstract

ir_datasets.registry.register('iranthology', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='datasets_in_progress/ir-anthology-documents.jsonl'), doc_cls=IrAnthologyDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='datasets_in_progress/topics.xml'), lang='en'),
    TrecQrels(ir_datasets.util.PackageDataFile(path='datasets_in_progress/qrels.txt'), {0: 'Not Relevant', 1: 'Relevant'})
))
