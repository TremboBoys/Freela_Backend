import pandas as pd
import torch
from transformers import BertTokenizer
from torch.utils.data import Dataset

class SimilarityDataSet(Dataset):
    def __init__(self, text_a, text_b, labels):
        self.text_a = text_a
        self.text_b = text_b
        self.labels = labels
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        text_a = self.text_a[index]
        text_b = self.text_b[index]
        labels = self.labels[index]

        encoding = self.tokenizer.encode_plus(
            text_a,
            text_b,
            add_special_tokens=True,
            padding="max_length",
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(labels, dtype=torch.float)
        }
