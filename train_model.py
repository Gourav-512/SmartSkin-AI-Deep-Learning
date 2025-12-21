# train_model.py

import os
import numpy as np
import pandas as pd
import cv2
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Paths
IMAGE_DIR = "dataset/1000_images"
LABELS_CSV = "dataset/labels.csv"

# Load CSV
df = pd.read_csv(LABELS_CSV)

# Classes to keep (4 most common)
selected_classes = ['nv', 'mel', 'bkl', 'df']
df = df[df['label'].isin(selected_classes)]

# Encode labels
lb = LabelBinarizer()
labels = lb.fit_transform(df['label'])

# Load and preprocess images
images = []
for fname in tqdm(df['filename'], desc="Loading Images"):
    path = os.path.join(IMAGE_DIR, fname)
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    img = img.astype("float32") / 255.0
    images.append(img)

images = np.array(images)
labels = np.array(labels)

# Split
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Build CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(lb.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Callbacks
os.makedirs("saved_models", exist_ok=True)
checkpoint = ModelCheckpoint("saved_models/skin_model_1000.h5", save_best_only=True, monitor="val_accuracy", mode="max")
early_stop = EarlyStopping(monitor="val_loss", patience=3)

# Train
model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=15,
    batch_size=32,
    callbacks=[checkpoint, early_stop]
)

print("✅ Training complete. Model saved as: saved_models/skin_model_1000.h5")
