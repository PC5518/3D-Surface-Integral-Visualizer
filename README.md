# 📌 3D Surface Integral Visualizer

A simple yet powerful Python project that **visualizes the concept of a surface integral** using 3D vector field rendering.

This tool illustrates how a vector field like **F(x, y, z) = ⟨x, y, 1⟩** flows through a flat surface in 3D space and helps you understand **flux**, **dot product**, and **surface normal** with clarity.

> 🎯 Designed with learners, Olympiad aspirants, and curious minds in mind!

---

## 🎥 Preview

![Surface Integral Visualization](./08913d2e-cb02-4663-80ee-7592a9dde032.png)

> Vector field arrows (in red) passing through a flat surface (cyan) in 3D space.

---

## 🧠 Why This Exists

Surface integrals are often introduced with tough math, making them hard to visualize. I built this project to bridge the gap between:

- **Pure mathematical formulas**  
  \[
  \Phi = \iint_S \vec{F} \cdot \hat{n} \, dA
  \]
- and **visual understanding**: how vectors “pierce” through a surface.

Many people learn the math, but **don’t develop intuition**. This project aims to fix that.

---

## 🔧 Features

- ✅ Define and visualize any vector field — here it's **F = ⟨x, y, 1⟩**
- ✅ Flat surface defined in the **xy-plane (z = 0)**
- ✅ Normal vectors are implicitly visualized using arrow directions
- ✅ Calculates the **flux** using numerical surface integral
- ✅ Fully 3D interactive plot (rotatable view)
- ✅ Built with **NumPy + Matplotlib**

---

## 📦 Dependencies

- Python 3.6+
- `numpy`
- `matplotlib`

Install using:

```bash
pip install numpy matplotlib
