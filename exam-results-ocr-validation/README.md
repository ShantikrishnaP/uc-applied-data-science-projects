# ExamCV – Automated Exam Results Extraction & Validation

## Overview

ExamCV is an automated exam processing system built using Computer Vision and Transformer-based OCR. 

The system extracts student information and question scores from scanned exam sheets, validates them against a student database, verifies score totals, and flags mismatches for manual review.

This project was developed as part of my MSc in Applied Data Science at the University of Canterbury.

---

## Problem Statement

Manual exam result processing is:
- Time-consuming
- Error-prone
- Difficult to scale
- Dependent on manual validation

The goal of this project was to automate:
- Student information extraction
- Score extraction
- Database validation
- Total score verification

---

## Key Features

- Image preprocessing and perspective correction using OpenCV
- OCR for student names and scores using Microsoft TrOCR
- Student number extraction using Gemini API
- Fuzzy matching for database validation
- Automatic total score verification
- Manual correction interface for mismatched totals
- Streamlit-based interactive web application

---

## Technology Stack

- Python
- Streamlit
- OpenCV
- Transformers (TrOCR)
- Google Gemini API
- Pandas & NumPy
- Fuzzy string matching (FuzzyWuzzy)

---

## System Workflow

1. Upload exam sheet image
2. Image preprocessing and normalization
3. Extract:
   - Family Name
   - First Name
   - Student Number
4. Validate against student database
5. If accuracy ≥ 50%:
   - Extract question scores
   - Verify total score consistency
6. Append validated results to database
7. Flag mismatches for manual inspection

---

## Results & Impact

- Reduced manual validation effort by approximately 70% (prototype environment)
- Automated mismatch detection
- Reduced human error in total score calculation
- Enabled scalable result processing workflow

---

## Project Structure

