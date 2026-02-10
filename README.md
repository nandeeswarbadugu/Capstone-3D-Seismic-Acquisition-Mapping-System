# 🛰️ Seismic Acquisition Survey Simulator

A Python-based desktop application that simulates **seismic survey acquisition geometry**, visualizes **source–receiver layouts**, and computes **midpoint bins, offset distribution, and multiplicity (fold coverage)**.

This tool is designed for **geophysics students, seismic engineers, and survey planners** to understand and optimize seismic data acquisition layouts before field deployment.

---

## 📌 Overview

Seismic data quality depends heavily on how **sources** and **geophones (receivers)** are arranged in the field. This application allows users to define survey geometry and instantly visualize how acquisition parameters affect:

- Receiver and source positioning  
- Common Midpoints (CMP bins)  
- Fold (multiplicity) coverage  
- Offset distribution  

It acts as both a **survey planning tool** and an **educational simulator** for seismic acquisition concepts.

---

## 🎯 Why This Project Is Useful

### ✔ Survey Planning
Helps design acquisition geometry before actual field operations, saving cost and time.

### ✔ Fold (Multiplicity) Analysis
Calculates how many traces contribute to each subsurface bin. Higher fold improves signal quality and imaging reliability.

### ✔ Midpoint (CMP) Visualization
Displays reflection points used in seismic processing to better understand subsurface coverage.

### ✔ Offset Distribution Study
Analyzes source–receiver distance variation, which impacts resolution and depth penetration.

### ✔ Educational Tool
Great for teaching seismic acquisition fundamentals in universities and training programs.

---

## 🛠 Features

- Interactive GUI built with **Tkinter**
- Automatic source and receiver grid generation
- Midpoint (CMP) calculation
- Multiplicity (fold) computation
- Offset distribution plotting
- Survey geometry visualization
- Export multiplicity results to **.docx**

---

## 🧮 Input Parameters

| Parameter | Description |
|----------|-------------|
| Survey Length (X) | Total length of survey area |
| Survey Width (Y) | Total width of survey area |
| Geophone Distance | Spacing between receivers |
| Geophone Line Distance | Spacing between receiver lines |
| Source Distance | Spacing between sources |
| Source Line Distance | Spacing between source lines |

---

## 📊 Output Visualizations

### 1️⃣ Survey Geometry Plot
Shows:
- 🔺 Geophones (Receivers)
- 🔴 Sources
- 🟢 Midpoint Bins with multiplicity values

### 2️⃣ Offset Distribution Plot
Displays how source–receiver distances vary across the survey.

---

## 💾 Output File

The program generates:
