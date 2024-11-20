
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split
import torch
import pandas as pd
from transformers import BertForSequenceClassification
from utils.training_ai.dataset_definition import SimilarityDataSet

class TrainModelView(APIView):
    def post(self, request):
        try:
            dataframe = pd.DataFrame(request.data['dataframe'])
        except KeyError:
            return Response({"error": "Dataframe is required"}, status=status.HTTP_400_BAD_REQUEST)

        similarity_df = self.calculate_similarity(dataframe)

        x_train, x_text, y_train, y_test = train_test_split(
            similarity_df[['Texto A', 'Texto B']],
            similarity_df['Similaridade'],
            test_size=0.2,
            random_state=42
        )
        
        train_dataset = SimilarityDataSet(x_train['Texto A'].tolist(), x_train['Texto B'].tolist(), y_train.tolist())
        train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)

        model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=1)
        optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        model.train()
        for epoch in range(3):
            print('1')
            total_loss = 0
            for batch in train_loader:
                print('2')
                optimizer.zero_grad()
                input_ids = batch['input_ids'].to(device)
                attention_mask = batch['attention_mask'].to(device)
                labels = batch['labels'].to(device)

                outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss
                total_loss += loss.item()

                loss.backward()
                optimizer.step()

            print(f'Epoch {epoch + 1}, Loss: {total_loss / len(train_loader)}')

        model.save_pretrained('potas_recommend')
        return Response({"message": "Model trained and saved successfully"}, status=status.HTTP_200_OK)

    def calculate_similarity(self, dataframe):
        similarities = []
        for index_a, row_a in dataframe.iterrows():
            print('3')
            for index_b, row_b in dataframe.iterrows():
                print('4')
                if index_a != index_b:
                    similarity_score = 0
                    if row_a['Área'] == row_b['Área']:
                        similarity_score += 1
                    if row_a['Subárea'] == row_b['Subárea']:
                        similarity_score += 1
                    
                    similarities.append({
                        'Área A': row_a['Área'],
                        'Subárea A': row_a['Subárea'],
                        'Área B': row_b['Área'],
                        'Subárea B': row_b['Subárea'],
                        'Texto A': f"{row_a['Área']} {row_a['Subárea']} {row_a['Target Audience']} {row_a['Category']}",
                        'Texto B': f"{row_b['Área']} {row_b['Subárea']} {row_b['Target Audience']} {row_b['Category']}",
                        'Similaridade': similarity_score
                    })
        
        return pd.DataFrame(similarities)
