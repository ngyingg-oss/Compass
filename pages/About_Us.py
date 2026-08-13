import streamlit as st

st.set_page_config(page_title="About Compass", page_icon="🧭")

st.title("🧭 About Compass")

st.markdown("""
## About Compass

Compass is a prototype application designed to help Singapore public-service officers, managers and HR teams navigate a structured, developmental competency assessment cycle. It combines a guided self/manager assessment workflow with AI-generated competency insights for Reporting Officers.

This application is a prototype built to demonstrate a competency-assessment workflow with Retrieval-Augmented Generation (RAG) and AI-assisted insights, and is intended for evaluation and demonstration purposes. Its outputs, especially the AI-generated insights, are a developmental aid and are not official HR guidance or a basis for promotion, disciplinary, or performance-ranking decisions.

---

## 🎯 Project Overview

Running a competency assessment cycle typically involves several moving parts: a competency framework with level descriptors, a target matrix defining expectations by role and grade, an officer roster with reporting lines, a self-assessment stage, a manager-review stage, and a way to identify patterns across the completed results.

Compass brings these elements together into a single application. It combines conventional application logic for activities that require precision and auditability, such as ratings, target comparisons, standing calculations, and completion tracking, with a Generative AI feature that converts structured assessment outcomes into clear, development-focused insights.

The application consists of three primary user-facing areas:

### 📝 My Assessment
A guided self-assessment workflow where officers rate themselves against competencies relevant to their role.

### 👥 My Team
A Reporting Officer dashboard used to review and finalise assessments, monitor team competency outcomes, and generate AI-assisted insights.

### 🏢 Administration
An HR console for maintaining competencies, target expectations, officer rosters, reporting structures and assessment cycles.

---

## ❓ Problem Statement

Competency assessment cycles can be challenging to administer consistently. Managers need to track who reports to them, understand which competencies apply to each staff member, review self-assessments, conduct their own assessments, and identify meaningful development priorities across the team.

Without a dedicated platform, these activities are often spread across spreadsheets, forms and multiple documents, creating administrative effort for officers, managers and HR.

It can also be difficult for managers to interpret large volumes of assessment data and identify what development conversations should take priority.

Compass therefore aims to:

- consolidate competency frameworks, reporting structures and assessment data in a single platform;
- provide officers with a structured and intuitive self-assessment experience;
- enable managers to conduct competency reviews alongside employee self-assessments;
- distinguish actual competency gaps from situations where there is insufficient evidence for assessment;
- provide AI-assisted competency insights based on assessment outcomes and organisational expectations; and
- maintain a transparent and traceable link between AI insights and underlying assessment data.

---

## 👨‍👩‍👧 Target Users

The prototype is designed primarily for:

### 👤 Officers
Officers complete self-assessments and review their assessment outcomes across multiple assessment cycles.

### 👥 Reporting Officers
Managers review staff assessments, conduct their own assessments, identify development areas, and use AI Insights to understand team-wide patterns.

### 👨‍💼 HR Administrators
HR manages the competency framework, officer roster, target matrix and assessment cycles while monitoring organisation-wide participation.

---

## 🧩 Core Features

### 📝 1. My Assessment (Self-Assessment)

Officers rate themselves against competencies assigned to their division, section and grade.

Features include:

- step-by-step assessment wizard;
- role-specific competency descriptors;
- 1–5 rating scale;
- "Insufficient Exposure" option separated from low ratings;
- supporting evidence notes;
- draft autosave; and
- structured submission workflow.

### 👥 2. My Team (Manager Assessment + AI Insights)

Reporting Officers review and assess their staff.

Features include:

- side-by-side self and manager assessments;
- development comments;
- final assessment release workflow;
- competency standing calculations;
- self versus manager calibration indicators; and
- AI-generated team insights.

### 🏢 3. Administration (HR)

HR administrators manage:

- competency libraries;
- competency definitions and level descriptors;
- officer rosters;
- reporting structures;
- target competency profiles;
- assessment cycles;
- completion tracking; and
- bulk import/export functions.

---

## 🤖 AI Insights (RAG-Powered)

Compass includes a Retrieval-Augmented Generation (RAG) capability that helps Reporting Officers interpret competency assessment outcomes and prepare for meaningful development conversations.

The feature combines structured assessment data with competency-framework knowledge retrieved from a dedicated knowledge base.

```text
RO's team assessments (current cycle)
                    ↓
Deterministic assessment aggregation
                    ↓
Structured assessment digest (JSON)
                    ↓
Retrieve relevant competency definitions,
behavioural indicators and target expectations
from FAISS knowledge base
                    ↓
Combined context
(assessment digest + retrieved framework content)
                    ↓
Large Language Model
                    ↓
Development-focused manager insights
