from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

import tensorflow as tf

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = TFAutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def result_index(text):
    """Given a text, returns the index of the model's predicted classification for that text"""

    tokens = tokenizer.encode(text, return_tensors='tf')
    result = model(tokens)
    max_index = tf.argmax(result.logits, axis=1).numpy().item() + 1
    return max_index












