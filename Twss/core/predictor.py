import pickle
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
MAX_SEQUENCE_LENGTH = 100 
model = load_model("core/models/twss_model.h5")

with open("core/models/tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)

def check(sentence):
    sequence = tokenizer.texts_to_sequences([sentence])
    data = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)
    result = model.predict(data)
    if np.argmax(result) == 1:
        return True
    else:
        return False
    

