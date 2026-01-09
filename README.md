# AI Resume Screening System (End-to-End ML Project)

An end-to-end Machine Learning system that automatically evaluates how well a resume matches a given job description using NLP and supervised learning.  
The system exposes a REST API that returns a **match score**, **matching skills**, and **missing skills**, simulating a real-world Applicant Tracking System (ATS).

---

## Problem Statement

Recruiters receive hundreds of resumes for a single job opening.  
Manual screening is time-consuming, inconsistent, and prone to bias.

This project aims to:
- Automate resume screening
- Reduce recruiter effort
- Provide explainable matching insights

---

## Solution Overview

Given:
- Resume text
- Job description text

The system:
1. Cleans and processes text using NLP
2. Extracts features using TF-IDF / embeddings
3. Predicts a resume–job match score using ML
4. Extracts matching and missing skills
5. Serves predictions via a REST API

## Input
   1. Resume text (string)
   2. Job description text (string)
## Output
   1. Match score (0–100)
   2. Matching skills
   3. Missing skills