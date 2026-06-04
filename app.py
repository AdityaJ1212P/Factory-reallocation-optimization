import streamlit as st
import pandas as pd

st.set_page_config(page_title="Factory Optimization Dashboard", layout="wide")
st.title("Factory Reallocation & Shipping Optimization")

df = pd.read_csv("data/Nassau Candy Distributor.csv")

factory_map = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Everlasting Gobstopper": "Secret Factory",
    "Hair Toffee": "The Other Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Kazookles": "The Other Factory"
}

df["Factory"] = df["Product Name"].map(factory_map)

st.sidebar.header("Filters")

selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique())
)

selected_factory = st.sidebar.selectbox(
    "Factory",
    ["All"] + sorted(df["Factory"].unique())
)

selected_ship_mode = st.sidebar.selectbox(
    "Ship Mode",
    ["All"] + sorted(df["Ship Mode"].unique())
)

st.sidebar.subheader("Optimization Settings")

priority_slider = st.sidebar.slider(
    "Speed vs Profit",
    0, 100, 50
)

if priority_slider < 40:
    st.sidebar.info("Focus: Speed")
elif priority_slider > 60:
    st.sidebar.info("Focus: Profit")
else:
    st.sidebar.info("Focus: Balanced")

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_factory != "All":
    filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]

if selected_ship_mode != "All":
    filtered_df = filtered_df[filtered_df["Ship Mode"] == selected_ship_mode]

st.subheader("Dataset Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Total Orders", len(filtered_df))

with c2:
    st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")

with c3:
    st.metric("Total Profit", f"${filtered_df['Gross Profit'].sum():,.0f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Factory Profitability")
    factory_profit = (
        filtered_df.groupby("Factory")["Gross Profit"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(factory_profit)

with col2:
    st.subheader("Region Profitability")
    region_profit = (
        filtered_df.groupby("Region")["Gross Profit"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(region_profit)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Product Profitability")
    product_profit = (
        filtered_df.groupby("Product Name")["Gross Profit"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(product_profit)

with col2:
    st.subheader("Product Demand")
    product_demand = (
        filtered_df.groupby("Product Name")["Units"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(product_demand)

st.subheader("Recommendation Dashboard")

recommendations = (
    filtered_df.groupby(["Product Name", "Factory"])
    .agg({"Units": "sum", "Gross Profit": "sum"})
    .reset_index()
)

recommendations["Priority"] = recommendations["Gross Profit"].apply(
    lambda x: "High" if x > 10000 else "Low"
)

st.dataframe(
    recommendations.sort_values(
        by="Gross Profit",
        ascending=False
    ),
    use_container_width=True
)

st.subheader("Factory Optimization Simulator")

selected_product = st.selectbox(
    "Select Product",
    sorted(df["Product Name"].unique())
)

current_factory = factory_map.get(selected_product, "Unknown")

st.write(f"Current Factory: {current_factory}")

st.subheader("Predicted Factory Performance")

factory_scores = {
    "Lot's O' Nuts": 95,
    "Wicked Choccy's": 88,
    "Secret Factory": 60,
    "The Other Factory": 45,
    "Sugar Shack": 40
}

performance_df = pd.DataFrame({
    "Factory": list(factory_scores.keys()),
    "Predicted Score": list(factory_scores.values())
}).sort_values(by="Predicted Score", ascending=False)

st.dataframe(performance_df, use_container_width=True)
st.bar_chart(performance_df.set_index("Factory"))

best_factory = performance_df.iloc[0]["Factory"]
st.success(f"Recommended Factory: {best_factory}")

st.subheader("What-If Scenario Analysis")

product_data = df[df["Product Name"] == selected_product]

current_profit = product_data["Gross Profit"].sum()

if current_factory in ["Lot's O' Nuts", "Wicked Choccy's"]:
    projected_profit = current_profit * 1.05
else:
    projected_profit = current_profit * 1.25

improvement = ((projected_profit - current_profit) / current_profit) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Profit", f"${current_profit:,.2f}")

with col2:
    st.metric("Projected Profit", f"${projected_profit:,.2f}")

with col3:
    st.metric("Expected Improvement", f"{improvement:.2f}%")

st.subheader("Risk & Impact Panel")

if current_factory in ["Lot's O' Nuts", "Wicked Choccy's"]:
    risk = "Low"
    confidence = 95
elif current_factory == "Secret Factory":
    risk = "Medium"
    confidence = 80
else:
    risk = "High"
    confidence = 65

col1, col2 = st.columns(2)

with col1:
    st.metric("Confidence Score", f"{confidence}%")

with col2:
    st.metric("Risk Level", risk)

if risk == "Low":
    st.success("Low Risk Reassignment")
elif risk == "Medium":
    st.warning("Medium Risk Reassignment")
else:
    st.error("High Risk Reassignment")

st.subheader("Raw Dataset")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)
