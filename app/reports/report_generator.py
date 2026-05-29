from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from PIL import Image
from datetime import datetime
import os

def generate_pdf_report(
    patient_name,
    prediction,
    confidence,
    image_path
):

    report_id = (
        "BFC-" +
        datetime.now().strftime(
            "%Y%m%d-%H%M%S"
        )
    )

    pdf_filename = (
        f"{patient_name.replace(' ', '_')}"
        "_BFC_Report.pdf"
    )

    c = canvas.Canvas(
        pdf_filename,
        pagesize=(595, 842)
    )

    width = 595
    height = 842

    # =====================================
    # PAGE 1 HEADER
    # =====================================

    c.setFillColor(
        colors.HexColor("#0F4C81")
    )

    c.rect(
        0,
        height - 90,
        width,
        90,
        fill=1,
        stroke=0
    )

    c.setFillColor(colors.white)

    c.setFont(
        "Helvetica-Bold",
        22
    )

    c.drawString(
        30,
        height - 40,
        "AI BONE FRACTURE ANALYSIS REPORT"
    )

    c.setFont(
        "Helvetica",
        11
    )

    c.drawString(
        30,
        height - 62,
        "Advanced Deep Learning Diagnostic System"
    )

    # =====================================
    # REPORT INFO CARDS
    # =====================================

    c.setFillColor(
        colors.HexColor("#EAF3FF")
    )

    c.roundRect(
        30,
        height - 160,
        240,
        50,
        10,
        fill=1
    )

    c.roundRect(
        320,
        height - 160,
        240,
        50,
        10,
        fill=1
    )

    c.setFillColor(colors.black)

    c.setFont(
        "Helvetica-Bold",
        10
    )

    c.drawString(
        40,
        height - 130,
        "REPORT ID"
    )

    c.drawString(
        330,
        height - 130,
        "SCAN DATE"
    )

    c.setFont(
        "Helvetica",
        10
    )

    c.drawString(
        40,
        height - 145,
        report_id
    )

    c.drawString(
        330,
        height - 145,
        datetime.now().strftime(
            "%d-%b-%Y %I:%M %p"
        )
    )

    # =====================================
    # PATIENT CARD
    # =====================================

    c.setFillColor(colors.white)

    c.roundRect(
        30,
        height - 250,
        530,
        70,
        10,
        fill=1
    )

    c.setFillColor(
        colors.HexColor("#0F4C81")
    )

    c.setFont(
        "Helvetica-Bold",
        12
    )

    c.drawString(
        45,
        height - 205,
        "PATIENT INFORMATION"
    )

    c.setFillColor(colors.black)

    c.setFont(
        "Helvetica",
        11
    )

    c.drawString(
        45,
        height - 225,
        f"Patient Name: {patient_name}"
    )
    
    # =====================================
    # X-RAY SECTION
    # =====================================

    c.setFillColor(
        colors.HexColor("#0F4C81")
    )

    c.setFont(
        "Helvetica-Bold",
        12
    )

    c.drawString(
        30,
        height - 275,
        "UPLOADED X-RAY SCAN"
    )

    try:

        img = Image.open(image_path)

        img_width, img_height = img.size

        max_width = 265

        scale = max_width / img_width

        new_width = img_width * scale
        new_height = img_height * scale

        c.drawImage(
            image_path,
            30,
            height - 590,
            width=new_width,
            height=new_height,
            preserveAspectRatio=True
        )

    except Exception as e:

        print("Image Error:", e)

    # =====================================
    # DIAGNOSIS CARD
    # =====================================

    if "Fractured" in prediction:

        diagnosis_color = colors.HexColor("#D32F2F")

        diagnosis_text = "FRACTURE DETECTED"

        risk_level = "HIGH"

    else:

        diagnosis_color = colors.HexColor("#2E7D32")

        diagnosis_text = "NO FRACTURE DETECTED"

        risk_level = "LOW"

    c.setFillColor(
        diagnosis_color
    )

    c.roundRect(
        320,
        height - 420,
        240,
        90,
        12,
        fill=1
    )

    c.setFillColor(colors.white)

    c.setFont(
        "Helvetica-Bold",
        16
    )

    c.drawCentredString(
        440,
        height - 365,
        diagnosis_text
    )

    c.setFont(
        "Helvetica",
        11
    )

    c.drawCentredString(
        440,
        height - 390,
        f"Confidence: {confidence:.2f}%"
    )

    # =====================================
    # RISK LEVEL
    # =====================================

    c.setFillColor(
        colors.HexColor("#EAF3FF")
    )

    c.roundRect(
        320,
        height - 500,
        240,
        55,
        10,
        fill=1
    )

    c.setFillColor(colors.black)

    c.setFont(
        "Helvetica-Bold",
        11
    )

    c.drawString(
        335,
        height - 470,
        "RISK LEVEL"
    )

    c.setFont(
        "Helvetica",
        11
    )

    c.drawString(
        335,
        height - 488,
        risk_level
    )

    # =====================================
    # CONFIDENCE BAR
    # =====================================

    c.setFont(
        "Helvetica-Bold",
        11
    )

    c.drawString(
        320,
        height - 540,
        "CONFIDENCE SCORE"
    )

    c.setFillColor(
        colors.HexColor("#DCE3EB")
    )

    c.rect(
        320,
        height - 565,
        220,
        15,
        fill=1,
        stroke=0
    )

    c.setFillColor(
        colors.HexColor("#0F4C81")
    )

    progress_width = (
        confidence / 100
    ) * 220

    c.rect(
        320,
        height - 565,
        progress_width,
        15,
        fill=1,
        stroke=0
    )

    c.setFillColor(colors.black)

    c.drawString(
        320,
        height - 585,
        f"{confidence:.2f}%"
    )

    # =====================================
    # RELIABILITY SCORE
    # =====================================

    if confidence >= 95:

        reliability = "★★★★★  EXCELLENT"

    elif confidence >= 85:

        reliability = "★★★★☆  VERY GOOD"

    else:

        reliability = "★★★☆☆  GOOD"

    c.setFillColor(
        colors.HexColor("#EAF3FF")
    )

    c.roundRect(
        320,
        height - 660,
        240,
        60,
        10,
        fill=1
    )

    c.setFillColor(colors.black)

    c.setFont(
        "Helvetica-Bold",
        11
    )

    c.drawString(
        335,
        height - 625,
        "DIAGNOSTIC RELIABILITY"
    )

    c.setFont(
        "Helvetica",
        11
    )

    c.drawString(
        335,
        height - 645,
        reliability
    )
    c.setFont(
        "Helvetica",
        9
    )

    c.drawRightString(
        570,
        20,
        "Page 1 of 2"
    )
    
    # =====================================
    # PAGE 2
    # =====================================

    c.showPage()

    width = 595
    height = 842

    # =====================================
    # PAGE 2 HEADER
    # =====================================

    c.setFillColor(
        colors.HexColor("#0F4C81")
    )

    c.rect(
        0,
        height - 70,
        width,
        70,
        fill=1,
        stroke=0
    )

    c.setFillColor(colors.white)

    c.setFont(
        "Helvetica-Bold",
        18
    )

    c.drawString(
        25,
        height - 42,
        "AI MEDICAL INTERPRETATION"
    )

    # =====================================
    # INTERPRETATION SECTION
    # =====================================

    if "Fractured" in prediction:

        interpretation = [
            "The uploaded X-ray demonstrates structural",
            "patterns associated with a possible bone fracture.",
            "",
            "The AI model identified abnormal bone",
            "continuity and fracture-like characteristics.",
            "",
            "Professional radiological review",
            "is strongly recommended."
        ]

    else:

        interpretation = [
            "The uploaded X-ray does not show",
            "significant fracture-related characteristics.",
            "",
            "No major abnormalities were detected",
            "by the AI model.",
            "",
            "Professional medical consultation",
            "is still recommended when required."
        ]

    c.setFillColor(
        colors.HexColor("#F8FAFC")
    )

    c.roundRect(
        25,
        height - 330,
        545,
        220,
        10,
        fill=1
    )

    c.setFillColor(colors.black)

    c.setFont(
        "Helvetica-Bold",
        13
    )

    c.drawString(
        40,
        height - 145,
        "AI Interpretation"
    )

    y = height - 185

    c.setFont(
        "Helvetica",
        11
    )

    for line in interpretation:

        c.drawString(
            40,
            y,
            line
        )

        y -= 18

    # =====================================
    # MODEL INFORMATION
    # =====================================

    c.setFillColor(
        colors.HexColor("#EAF3FF")
    )

    c.roundRect(
        25,
        height - 520,
        545,
        160,
        10,
        fill=1
    )

    c.setFillColor(colors.black)

    c.setFont(
        "Helvetica-Bold",
        13
    )

    c.drawString(
        40,
        height - 390,
        "MODEL INFORMATION"
    )

    c.setFont(
        "Helvetica",
        11
    )

    c.drawString(
        40,
        height - 425,
        "Model Architecture: ResNet50 Transfer Learning"
    )

    c.drawString(
        40,
        height - 450,
        "Framework: TensorFlow / Keras"
    )

    c.drawString(
        40,
        height - 475,
        "Input Resolution: 224 x 224"
    )

    c.drawString(
        40,
        height - 500,
        "Test Accuracy: 92.73%"
    )

    # =====================================
    # DISCLAIMER
    # =====================================

    c.setFillColor(
        colors.HexColor("#FFF4E5")
    )

    c.roundRect(
        25,
        height - 680,
        545,
        120,
        10,
        fill=1
    )

    c.setFillColor(colors.black)

    c.setFont(
        "Helvetica-Bold",
        12
    )

    c.drawString(
        40,
        height - 590,
        "DISCLAIMER"
    )

    c.setFont(
        "Helvetica",
        10
    )

    c.drawString(
        40,
        height - 620,
        "This report was generated using an AI-assisted diagnostic model."
    )

    c.drawString(
        40,
        height - 645,
        "It should not be considered a final medical diagnosis."
    )
    

    # =====================================
    # FOOTER
    # =====================================

    c.setFillColor(
        colors.HexColor("#0F4C81")
    )

    c.rect(
        0,
        0,
        width,
        100,
        fill=1,
        stroke=0
    )

    c.setFillColor(colors.white)

    c.setFont(
        "Helvetica-Bold",
        12
    )

    c.drawString(
        25,
        80,
        f"Generated For: {patient_name}"
    )

    c.drawString(
        25,
        60,
        "Generated By: Shivansh Deshwal"
    )
    
    c.drawString(
        25,
        40,
        "AI Bone Fracture Classification System"
    )

    c.drawString(
        25,
        20,
        "Powered by TensorFlow • Keras • ResNet50"
    )

    c.setFont(
        "Helvetica",
        10
    )

    c.drawRightString(
        570,
        20,
        "Version 1.0"
    )
    
    c.setFont(
        "Helvetica",
        9
    )

    c.drawRightString(
        570,
        100,
        "Page 2 of 2"
    )

    # =====================================
    # SAVE PDF
    # =====================================

    c.save()

    return pdf_filename