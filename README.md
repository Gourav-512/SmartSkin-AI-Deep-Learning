# 🧠 SmartSkin AI

SmartSkin AI is a skin lesion classification system that uses deep learning to predict disease class from an image. It includes a **trained MobileNetV2 model** and a sleek **Streamlit interface**.

---

## 📁 Project Structure

SmartSkin_AI/
├── app/
│ └── streamlit_app.py # Streamlit frontend
├── dataset/ # (Optional) Used only during training
│ ├── 1000_images/
│ └── labels.csv
├── saved_models/
│ └── skin_model_1000.h5 # Trained model
├── train_model.py # Model training script
├── requirements.txt # All required libraries
└── README.md # You're reading it now!


---

## 🛠️ Installation & Setup

### Step 1: Create Virtual Environment

```bash
python -m venv venv

### Step 2: Activate Virtual Environment
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

### Step 3: Install All Required Packages

pip install -r requirements.txt

🚀 How to Run the App
Once setup is done, start the web app using:

streamlit run app/streamlit_app.py

Then open in your browser:

http://localhost:8501


🧠 About the Model
 ____________________________________________________
| Detail         | Value                             |
| -------------- | --------------------------------- |
| Architecture   | MobileNetV2                       |
| Input Size     | 224x224                           |
| Trained On     | 1000 Skin Images (HAM10K)         |
| Output Classes | `bkl`, `df`, `mel`, `nv`          |
| File           | `saved_models/skin_model_1000.h5` |
|____________________________________________________|


📷 How to Use

Upload a .jpg, .png, or .jpeg skin image.

The AI will analyze and show the predicted class.

Prediction appears below the image (e.g. Predicted Class: MEL).


🔍 Class Labels Explained  
 _______________________________________
| Label | Meaning                       |
| ----- | ----------------------------- |
| `nv`  | Melanocytic nevi (non-cancer) |
| `mel` | Melanoma (cancerous)          |
| `bkl` | Benign keratosis              |
| `df`  | Dermatofibroma                |
|_______|_______________________________|


🧾 Notes 

💡 This app works fully offline

🧪 No GPU needed — it uses CPU

🎯 Tested on Windows 10, Python 3.9

Future features: PDF reports, API version, web hosting

🔐 License
MIT License – You’re free to use and customize. 
