import cv2
import numpy as np
import pandas as pd
import os
import shutil
import time
from PIL import Image
from fuzzywuzzy import fuzz
import google.generativeai as genai
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

# Load OCR Model
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Configure Gemini API
genai.configure(api_key="AIzaSyBaRBymbYyjnfKO6nmgJWOyE31HJhueW1U")

# Define coordinates for fields
student_info_coordinates = {
    "Family Name": (215, 64, 448, 103),
    "First Name": (216, 100, 446, 133),
    "Student Number": (216, 132, 364, 155),
}

score_coordinates = {
    "Q1": (673, 474, 734, 499),
    "Q2": (673, 503, 734, 528),
    "Q3": (673, 533, 734, 558),
    "Q4": (673, 563, 734, 588),
    "Q5": (673, 591, 734, 616),
    "Q6": (673, 620, 734, 647),
    "Q7": (673, 650, 734, 676),
    "Q8": (673, 680, 734, 706),
    "Q9": (673, 708, 734, 735),
    "Q10": (673, 739, 734, 765),
    "Q11": (673, 767, 734, 794),
    "Total": (659, 806, 742, 838),
}

# Image Preprocessing: Cropping & Resizing
def process_and_save_image(image_path, output_image_name, final_width=800, final_height=1000):
    """Processes the given image by detecting, cropping, and resizing the exam sheet."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    if contours:
        approx = cv2.approxPolyDP(contours[0], 0.02 * cv2.arcLength(contours[0], True), True)
        if len(approx) == 4:
            rect = np.float32(approx.reshape(4, 2))
            dst = np.float32([[0, 0], [final_width, 0], [final_width, final_height], [0, final_height]])
            matrix = cv2.getPerspectiveTransform(rect, dst)
            processed_image = cv2.warpPerspective(image, matrix, (final_width, final_height))
            cv2.imwrite(output_image_name, processed_image)
            return processed_image
    return None

def extract_text(image_path, coordinates):
    """Extracts text using OCR from specified fields."""
    image = cv2.imread(image_path)
    extracted_values = {}

    for field, (x1, y1, x2, y2) in coordinates.items():
        cropped_image = image[y1:y2, x1:x2]
        pil_image = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

        pixel_values = processor(images=pil_image, return_tensors="pt").pixel_values
        outputs = model.generate(pixel_values)
        extracted_text = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip().upper()
        extracted_values[field] = extracted_text

    return extracted_values

def extract_student_number(image_path):
    """Extracts Student Number using Gemini API."""
    x1, y1, x2, y2 = student_info_coordinates["Student Number"]
    image = cv2.imread(image_path)
    student_number_roi = image[y1:y2, x1:x2]

    temp_image_path = "temp_student_number.jpg"
    cv2.imwrite(temp_image_path, student_number_roi)

    pil_image = Image.open(temp_image_path)
    model = genai.GenerativeModel("gemini-1.5-flash")

    time.sleep(3)
    response = model.generate_content([pil_image, "Extract only the student number from this image. Return digits only."])
    return response.text.strip()

def fuzzy_match(extracted_info, df):
    """Performs fuzzy matching with a **threshold of 80%**."""
    extracted_family_name = extracted_info["Family Name"]
    extracted_first_name = extracted_info["First Name"]

    best_match = None
    best_score = 0
    student_index = None

    for index, row in df.iterrows():
        db_family_name = row["Family Name"]
        db_first_name = row["First Name"]

        match_score = (fuzz.ratio(extracted_family_name, db_family_name) + fuzz.ratio(extracted_first_name, db_first_name)) / 2

        if match_score > best_score:
            best_score = match_score
            best_match = row
            student_index = index

    return best_match, student_index, best_score

def handle_low_accuracy(image_path):
    """Moves images with **low match scores** to manual inspection folder."""
    folder_path = "manual_inspection"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.basename(image_path)
    new_filename = f"{timestamp}_{filename}"

    destination_path = os.path.join(folder_path, new_filename)
    shutil.copy(image_path, destination_path)

    print(f"⚠️ Image flagged for manual inspection: {destination_path}")
