import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

# Dummy training data
X = np.random.rand(100, 10)
y = np.random.rand(100, 4)

# Train dummy model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(4)
])
model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError())  # <-- FIXED
model.fit(X, y, epochs=5)

# Save model
model.save('genomic_model.h5')

# Save scaler
scaler = StandardScaler()
scaler.fit(X)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)