# Scalable Music Genre Classification & Recommendation System (Spark)

Course: Scalable Data Science (DATA420)  
University of Canterbury  

---

## Overview

This project implemented large-scale machine learning and collaborative filtering using Apache Spark on the Million Song Dataset.

The work involved distributed data processing, genre classification, and user-based recommendation modeling using Spark ML.

Due to university policy, source code and raw datasets cannot be shared publicly. This repository contains the analytical report summarizing architecture, methodology, and results.

---

## Dataset Scale

- Audio Features Dataset: ~97.8 GB (HDFS)
- Taste Profile Dataset: 48M+ user-song interactions
- 1M+ users
- 384K+ unique songs

---

## Part 1: Audio Similarity & Genre Classification

### Binary Classification
Task: Identify "Electronic" genre (9.67% minority class)

Algorithms evaluated:
- Logistic Regression
- Random Forest
- Gradient Boosted Trees (Best performer)

Evaluation Metrics:
- Precision
- Recall
- F1 Score
- Accuracy

GBT achieved highest F1 score and handled class imbalance effectively.

---

### Multiclass Classification (21 Genres)

- Random Forest classifier
- Stratified sampling
- Macro-averaged Precision, Recall, F1
- Addressed genre imbalance (Pop_Rock dominant)

---

## Part 2: Collaborative Filtering Recommendation System

Built using user-song interaction data.

Key steps:
- Filtering low-activity users & low-play songs (N=10, M=10)
- Ensuring test set coverage
- Repartitioning & caching for performance
- Handling long-tail distribution

### Evaluation Metrics:
- Precision@10
- NDCG@10
- MAP (Mean Average Precision)

Model achieved strong ranking performance in test evaluation.

---

## Big Data Engineering Concepts Applied

- HDFS directory management
- Schema inference using StructType
- Spark partition optimization
- Repartitioning vs caching tradeoffs
- Handling large-scale joins
- Class imbalance strategies
- Distributed ML training

---

## Skills Demonstrated

- PySpark & Spark ML
- Distributed computing
- Large-scale data engineering
- Classification modeling
- Recommender systems
- Performance optimization
- Model evaluation under imbalance

---

## Note

This project was completed as part of university coursework.  
