## IMDb 50k Movie Dataset Sentiment Analysis

The project aims to perform sentiment analysis on the IMDb 50k movie dataset using deep learning techniques. The dataset consists of movie reviews labeled with sentiment (positive or negative). The objective is to train a deep learning model that can accurately classify the sentiment of movie reviews as positive or negative.

### Key Steps

1. **Tokenization**: The text data is tokenized using the `Tokenizer` class from the Keras library. This step involves converting the text data into integer values, where each word in the dataset is assigned a unique integer. The `Tokenizer` is configured to consider the top 5000 most common words in the dataset.

2. **Padding Sequences**: After tokenization, the text sequences are padded to ensure uniform length. This is done using the `pad_sequences` function, which pads or truncates sequences to a specified length (in this case, 200 tokens).

3. **Model Compilation**: A deep learning model is compiled using the Adam optimizer and binary cross-entropy loss function. The model is configured to optimize for accuracy during training.

4. **Prediction Function**: A prediction function is defined to classify the sentiment of movie reviews. The function tokenizes and pads the input review, passes it through the trained model, and predicts the sentiment as either positive or negative based on the model's output probability.

### Example Usage

```python
review = "The movie was fantastic, I loved it!"
sentiment = prediction([review])
print(sentiment)  # Output: "Positive"
