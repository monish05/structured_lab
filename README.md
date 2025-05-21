# ⚡ EV Insights Dashboard — Powered by Preswald

An interactive, data-rich electric vehicle analytics dashboard built entirely using **Preswald**, a product of StructuredLabs.

This dashboard highlights my ability to quickly understand and apply Preswald’s declarative design model, custom layout components, and SQL-based data querying. It also demonstrates thoughtful use of the framework’s flexibility to build a user-friendly and insight-driven application.

---

## 🎯 Project Purpose

This project was developed as part of an interview submission to StructuredLabs to showcase:

- My ability to understand and extend Preswald's API and philosophy
- Skill in building composable, modular dashboards with modern UX
- Effective application of SQL and Plotly within the Preswald environment
- Practical use of Preswald’s sidebar, slider, data querying, and configuration tools

---

## 🚀 Features Implemented with Preswald

| Feature                                | Preswald Implementation                                          |
|----------------------------------------|------------------------------------------------------------------|
| **Sidebar Branding**                   | `sidebar(defaultopen, logo, name)` for identity and UX           |
| **Dynamic Filtering**                  | `slider()` to filter EV data by year                             |
| **SQL-Based Data Queries**             | `query()` with formatted parameters (`f"""..."""`)               |
| **Multiple Linked Visuals**            | `plotly()` to render bar, pie, and line charts with Plotly       |
| **Data Table Component**               | `table()` used with `query()` results                            |
| **Visual Theming & Layout**            | Custom colors + layout via `preswald.toml`                       |

---

## 🧠 How I Used Preswald Beyond the Basics

While Preswald offers a smooth on-ramp, I aimed to **go beyond the example-driven use** by:

- Designing a flexible layout with chart types tailored to the data's narrative (e.g., pie chart for powertrain breakdown, line charts for growth trends)
- Using the `sidebar()` not just for layout but as a visual anchor for branding and navigation
- Replacing traditional dropdowns with a `slider()` to give smoother filtering experience
- Structuring queries and visuals modularly, allowing them to adapt to user inputs without redundancy
- Applying SQL to filter, group, and clean data within Preswald's declarative structure

I made use of the following documentation from the [Preswald GitHub repository](https://github.com/StructuredLabs/preswald):

- [Sidebar Layout](https://github.com/StructuredLabs/preswald/blob/main/docs/layout/sidebar.mdx)
- [Slider Input](https://github.com/StructuredLabs/preswald/blob/main/docs/layout/sizing.mdx)
- [Querying CSV Data](https://github.com/StructuredLabs/preswald/blob/main/docs/data/query.mdx)
- [Display Components](https://github.com/StructuredLabs/preswald/blob/main/docs/displays/plotly.mdx)

---

## 📊 Dashboard Features

- **EV Sales by Region** (Bar chart)
- **EV Sales by Powertrain** (Pie chart)
- **EV Sales Trend Over Time** (Line chart for top 5 regions)
- **EV Stock Growth Over Time** (Line chart)
- **Custom Sidebar + Year Filter Slider**
- **Fully configured `preswald.toml` for branding, colors, and data**

---

## 🧱 Project Structure

```
ev-insights-dashboard/
├── hello.py               # Preswald app
├── preswald.toml          # Config: branding, ports, dataset
├── data/
│   └── EV_sales.csv       # Core dataset
├── images/
│   └── favicon.ico             # Favicon
│   └── logo.png                # logo
├── requirements.txt
└── README.md
```

---

## 🧰 Requirements

- Python 3.10+
- preswald
- pandas
- plotly

Install with:

```bash
pip install -r requirements.txt
```

Run with:

```bash
preswald run
```

Open in your browser at [http://localhost:8501](http://localhost:8501)

---

## ✅ Why Preswald Worked So Well

Preswald allowed me to focus on **storytelling through data**, not boilerplate code. The declarative syntax, SQL compatibility, and component API let me build an application that’s both intuitive to use and powerful under the hood.

From clean visuals to flexible layout, this project reflects how **deeply I understand Preswald’s value and how it can be used effectively in real-world data applications**.

---

## 🙌 Thank You

Thank you for reviewing this submission! I genuinely enjoyed exploring Preswald and would love the opportunity to contribute to its continued success at StructuredLabs.
