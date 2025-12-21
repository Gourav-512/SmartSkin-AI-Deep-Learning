# generate_labels.py

import pandas as pd
import os

# Load metadata
meta_path = 'dataset/HAM10000_metadata.csv'
df = pd.read_csv(meta_path)

# Final 1000_images folder
image_folder = 'dataset/1000_images'

# Get only available images
available_imgs = os.listdir(image_folder)
available_imgs = [f.replace(".jpg", "") for f in available_imgs]

# Filter metadata for available images
df_filtered = df[df['image_id'].isin(available_imgs)]

# Save labels.csv
output_csv = 'dataset/labels.csv'
df_out = pd.DataFrame({
    "filename": df_filtered["image_id"].astype(str) + ".jpg",
    "label": df_filtered["dx"]
})
df_out.to_csv(output_csv, index=False)

print("✅ labels.csv created with", len(df_out), "entries")
