from preswald import sidebar, connect, get_df, query, text, table, plotly, slider
import plotly.express as px

# ----------------------
# Sidebar with Branding
# ----------------------
sidebar(
    defaultopen=True,
    logo="images/logo.png",
    name="EV Insights Dashboard"
)

# ----------------------
# Connect and Load Data
# ----------------------
connect()
df = get_df("EV_sales")

# Year selection using slider
years = sorted(df["year"].dropna().unique())
selected_year = slider("Select Year", min_val=min(years), max_val=max(years), default=max(years), step=1)

# ----------------------
# Page Title
# ----------------------
text("# 🚗 EV Insights Dashboard")
text("Visualizing global electric vehicle adoption trends.")

# ----------------------
# EV Sales by Region
# ----------------------
sql_sales_by_region = f"""
SELECT region, SUM(CAST(value AS DOUBLE)) AS total_sales
FROM EV_sales
WHERE parameter = 'EV sales' AND year = {selected_year} AND region != 'World'
GROUP BY region
ORDER BY total_sales DESC
"""
sales_df = query(sql_sales_by_region, "EV_sales")

text(f"## 🔝 EV Sales by Region ({selected_year})")
table(sales_df, title=f"EV Sales in {selected_year} by Region")

fig_region = px.bar(sales_df, x="region", y="total_sales", title=f"Total EV Sales by Region ({selected_year})")
plotly(fig_region)

# ----------------------
# EV Sales by Powertrain
# ----------------------
sql_powertrain = f"""
SELECT powertrain, SUM(CAST(value AS DOUBLE)) AS total_sales
FROM EV_sales
WHERE parameter = 'EV sales' AND year = {selected_year} AND region != 'World'
GROUP BY powertrain
ORDER BY total_sales DESC
"""
powertrain_df = query(sql_powertrain, "EV_sales")

text(f"## ⚙️ EV Sales Share by Powertrain ({selected_year})")
fig_powertrain = px.pie(powertrain_df, names="powertrain", values="total_sales",
                        title=f"EV Sales by Powertrain ({selected_year})")
plotly(fig_powertrain)

# ----------------------
# EV Sales Trend (Top 5 Regions)
# ----------------------
top_regions = ['China', 'USA', 'Germany', 'France', 'United Kingdom']
sql_trend = f"""
SELECT year, region, SUM(CAST(value AS DOUBLE)) AS total_sales
FROM EV_sales
WHERE parameter = 'EV sales' AND region IN ({','.join([f"'{r}'" for r in top_regions])})
GROUP BY year, region
ORDER BY year
"""
trend_df = query(sql_trend, "EV_sales")

text("## 📈 EV Sales Trend (Top 5 Regions)")
fig_trend = px.line(trend_df, x="year", y="total_sales", color="region", markers=True,
                    title="EV Sales Trend Over Time")
plotly(fig_trend)

# ----------------------
# EV Stock Over Time (Top 5 Regions)
# ----------------------
sql_stock = f"""
SELECT year, region, SUM(CAST(value AS DOUBLE)) AS total_stock
FROM EV_sales
WHERE parameter = 'EV stock' AND region IN ({','.join([f"'{r}'" for r in top_regions])})
GROUP BY year, region
ORDER BY year
"""
stock_df = query(sql_stock, "EV_sales")

text("## ⚡ EV Stock Over Time (Top 5 Regions)")
fig_stock = px.line(stock_df, x="year", y="total_stock", color="region", markers=True,
                    title="EV Stock Accumulation Over Time")
plotly(fig_stock)