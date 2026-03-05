# 🩺 SmartSkin AI – Skin Disease Classifier

**MobileNetV2 CNN** with **82% validation accuracy** | TensorFlow + Keras | Streamlit UI | Hugging Face Deployment

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

### Features
- 4-class skin lesion classification (`nv, mel, bkl, df`)
- Data augmentation + preprocessing
- Offline CPU-only app (Windows ready)
- One-click installer for clients

### Live Demo
- **Hugging Face Space** → [SmartSkin Demo](https://huggingface.co/Researcher-Gourav/SmartSkin-AI-Deep-Learning)
- **Streamlit local** → `streamlit run app/streamlit_app.py`

### Quick Start
```bash
git clone https://github.com/Gourav-512/SmartSkin-AI-Deep-Learning.git
cd SmartSkin-AI-Deep-Learning
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py

,,..
