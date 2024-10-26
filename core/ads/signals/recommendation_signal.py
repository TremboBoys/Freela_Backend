"""from django.dispatch import receiver
from django.db.models.signals import post_save
from core.ads.models import Ads
from transformers import BertForSequenceClassification, BertTokenizer
import torch
from core.perfil.models import Perfil

model = BertForSequenceClassification.from_pretrained('potas_recommend')
tokenizer = BertTokenizer.from_pretrained('potas_recommend')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


@receiver(post_save, sender=Ads)
def recommendAi(sender, instance, created, **kwargs):
    listaRecommend = []
    for c in Perfil.objects.all():
        area = c.area.name
        sub_area = c.sub_area.name
        category = instance.ads_category.name
        audience = instance.target_audience
        
        text = (
            f"This is the target audience: {audience}, "
            f"This is the category: {category}, "
            f"This is the area of freelancer: {area}, "
            f"This is competence of freelancer: {sub_area}"
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

        reference_text = ("Ideal target audience: Example, category: Web Development, "
                          "area: IT, sub_area: Backend")
        
        reference_inputs = tokenizer.encode_plus(
            reference_text,
            add_special_tokens=True,
            return_tensors='pt',
            padding='max_length',
            truncation=True,
            max_length=512,
        )
        reference_input_ids = reference_inputs['input_ids'].to(device)
        reference_attention_mask = reference_inputs['attention_mask'].to(device)

        with torch.no_grad():
            reference_outputs = model(reference_input_ids, attention_mask=reference_attention_mask)
            reference_logits = reference_outputs.logits

        results = {
            "predicted_label": torch.argmax(logits, dim=1).item(),
        }

        results["similaridade_real"] = logits
        if logits >= 0.92:
            listaRecommend.append({
                "id": c.pk,
                "similarity": logits 
            })
    return listaRecommend
"""