from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from core.perfil.models import Perfil
from transformers import BertForSequenceClassification, BertTokenizer
import torch

model = BertForSequenceClassification.from_pretrained('potas_recommend')
tokenizer = BertTokenizer.from_pretrained('potas_recommend')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

class CreateAdsModelMixin:

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        audience = serializer.validated_data.get('target audience')
        category = serializer.validated_data.get('category')
        list_recommend = []

        for c in Perfil.objects.all():
            area = c.area.name
            sub_area = c.sub_area.name

            text = (
                f"This ads is focused in: {audience}. "
                f"This category is: {category}. "
                f"This area is: {area}. "
                f"This sub area of ads: {sub_area}."
            )

            inputs = tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                return_tensors='pt',
                padding='max_length',
                truncation=True,
                max_length=512,
            )

            input_ids = inputs['input_ids'].to(device)
            attention_mask = inputs['attention_mask'].to(device)

            with torch.no_grad():
                outputs = model(input_ids, attention_mask=attention_mask)
                logits = outputs.logits

            
            if logits > 0.92: 
                list_recommend.append({
                    "perfil": c.pk,
                    "similarity": logits
                })

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(list_recommend, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
