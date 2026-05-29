from reports.report_generator import generate_pdf_report

import gradio as gr
import tensorflow as tf
from PIL import Image
import numpy as np
import warnings
from datetime import datetime
import pandas as pd
import os
import tempfile


warnings.filterwarnings("ignore")

# =========================================
# Load Model
# =========================================
model = tf.keras.models.load_model(
    "../model/best_bone_fracture_model.keras"
)

IMG_SIZE = 224
THRESHOLD = 0.4

# =========================================
# Create History File
# =========================================
history_file = "prediction_history.csv"

if not os.path.exists(history_file):

    df = pd.DataFrame(
        columns=[
            "Timestamp",
            "Patient Name",
            "Prediction",
            "Confidence"
        ]
    )

    df.to_csv(history_file, index=False)

# =========================================
# Prediction Function
# =========================================
def predict_fracture(patient_name, image):
    
    if not patient_name or not patient_name.strip():

        return (
            "❌ Please enter patient name",
            "0%",
            0,
            "Patient name is required.",
            None
        )

    if image is None:

        return (
            "❌ No image uploaded",
            "0%",
            0,
            "No analysis available.",
            None
        )

    # Resize image
    resized_image = image.resize(
        (IMG_SIZE, IMG_SIZE)
    )

    # Convert image
    img_array = np.array(resized_image) / 255.0
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # =========================================
    # Prediction
    # =========================================
    prediction = model.predict(
        img_array,
        verbose=0
    )[0][0]
    
    # =========================================
    # Label Logic
    # =========================================
    if prediction >= THRESHOLD:

        label = "✅ No Fracture Detected"

        confidence = prediction * 100

        details = """
        ### Analysis Result

        - Bone structure appears normal
        - No visible fracture detected
        - AI confidence level is high
        - No abnormal crack pattern identified
        """

    else:

        label = "🦴 Fractured Bone Detected"

        confidence = (1 - prediction) * 100

        details = """
        ### Analysis Result

        - Possible fracture detected
        - Abnormal bone pattern identified
        - Fracture-sensitive regions highlighted
        - Medical review recommended
        """

    # =========================================
    # Save Prediction History
    # =========================================
    new_data = pd.DataFrame([{
        "Timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "Patient Name": patient_name,
        "Prediction": label,
        "Confidence": f"{confidence:.2f}%"
    }])

    new_data.to_csv(
        history_file,
        mode="a",
        header=False,
        index=False
    )

    # Generate PDF Report
    temp_image = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    resized_image.save(
        temp_image.name
    )

    pdf_file = generate_pdf_report(
        patient_name,
        label,
        confidence,
        temp_image.name
    )

    return (
        label,
        f"{confidence:.2f}%",
        confidence,
        details,
        pdf_file
    )

# =========================================
# Load History
# =========================================
def load_history():

    df = pd.read_csv(history_file)

    return df.tail(10)


# =========================================
# Custom CSS
# =========================================
custom_css = """

body {
    background: linear-gradient(
        to right,
        #0f172a,
        #111827
    );
}

.gradio-container {
    font-family: Arial, sans-serif;
    color: white;
}

h1, h2, h3 {
    text-align: center;
}

footer {
    visibility: hidden;
}

"""

# =========================================
# Dashboard UI
# =========================================
with gr.Blocks(
    css=custom_css,
    title="AI Bone Fracture Classification"
) as app:

    gr.Markdown("""

    # 🩻 AI Bone Fracture Classification Dashboard

    ### Deep Learning-Based Bone Fracture Detection using ResNet50

    """)

    with gr.Row():

        # =========================================
        # LEFT PANEL
        # =========================================
        with gr.Column(scale=1):
            
            patient_name = gr.Textbox(
                label="👤 Patient Name",
                placeholder="Enter patient name"
            )

            image_input = gr.Image(
                type="pil",
                label="Upload X-ray Image",
                height=450
            )

            predict_button = gr.Button(
                "🔍 Analyze X-ray",
                variant="primary"
            )

        # =========================================
        # RIGHT PANEL
        # =========================================
        with gr.Column(scale=1):

            prediction_output = gr.Textbox(
                label="Prediction Result"
            )

            confidence_output = gr.Textbox(
                label="Confidence Score"
            )

            confidence_bar = gr.Slider(
                minimum=0,
                maximum=100,
                label="Confidence Level",
                interactive=False
            )

            analysis_output = gr.Markdown()
            
            pdf_output = gr.File(
                label="📄 Download AI Report"
            )

    # =========================================
    # Prediction Button Action
    # =========================================
    predict_button.click(
        fn=predict_fracture,
        inputs=[    
            patient_name,
            image_input
        ],
        outputs=[
            prediction_output,
            confidence_output,
            confidence_bar,
            analysis_output,
            pdf_output
        ]
    )

    # =========================================
    # Prediction History
    # =========================================
    gr.Markdown("---")

    gr.Markdown("""
    ## 📜 Recent Prediction History
    """)

    history_table = gr.Dataframe(
        headers=[
            "Timestamp",
            "Patient Name",
            "Prediction",
            "Confidence"
        ],
        interactive=False
    )

    refresh_button = gr.Button(
        "🔄 Refresh History"
    )

    refresh_button.click(
        fn=load_history,
        outputs=history_table
    )

    # =========================================
    # Footer Section
    # =========================================
    gr.Markdown("""

    ---

    ## 📌 Project Information

    ### Technologies Used
    - TensorFlow / Keras
    - ResNet50 Transfer Learning
    - Gradio Interactive Dashboard
    - Prediction History Tracking
    - Deep Learning Medical Imaging

    ### Developed By
    ## Shivansh Deshwal

    """)

# =========================================
# Launch App
# =========================================
app.launch(
    inbrowser=True
)