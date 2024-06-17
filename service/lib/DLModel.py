import torch
import torch.nn as nn
from transformers import BertTokenizer, BertModel


class NewsClassifier(nn.Module):
    def __init__(self, n_classes):
        super(NewsClassifier, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-multilingual-cased')
        self.drop = nn.Dropout(p=0.5)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        pooled_output = outputs[1]  # Пуллинг-слой [CLS] токена
        output = self.drop(pooled_output)
        return self.out(output)


def load_model(model_path):
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model = NewsClassifier(n_classes=2)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    return model, tokenizer

def predict_news(model, tokenizer, text, max_len=512):
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model = model.eval()

    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=max_len,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
        truncation=True
    )

    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        _, preds = torch.max(outputs, dim=1)

    return preds.cpu().numpy()[0], probabilities.cpu().numpy()[0][1]