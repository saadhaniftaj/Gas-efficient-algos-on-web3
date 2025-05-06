import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page configuration - Apple-inspired styling
st.set_page_config(
    page_title="Web2 vs Web3 Sorting Algorithm Benchmark",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for improved color scheme
st.markdown("""
<style>
    /* Modern color scheme */
    :root {
        --primary: #4F46E5;
        --primary-light: #818CF8;
        --primary-dark: #3730A3;
        --secondary: #10B981;
        --accent: #F59E0B;
        --dark: #1F2937;
        --light: #F9FAFB;
        --light-gray: #F3F4F6;
        --mid-gray: #E5E7EB;
        --text-dark: #111827;
        --text-mid: #4B5563;
        --text-light: #9CA3AF;
    }
    
    .main-title {
        font-size: 48px;
        font-weight: 600;
        text-align: center;
        margin-bottom: 30px;
        color: var(--primary);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }
    .subtitle {
        font-size: 28px;
        font-weight: 500;
        margin-top: 40px;
        margin-bottom: 15px;
        color: var(--dark);
        border-bottom: 1px solid var(--mid-gray);
        padding-bottom: 8px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }
    .author-info {
        text-align: center;
        background-color: var(--light-gray);
        padding: 20px;
        border-radius: 12px;
        margin: 30px 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }
    .insights {
        background-color: var(--light-gray);
        padding: 25px;
        border-radius: 12px;
        margin-top: 40px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }
    .highlight {
        font-weight: 600;
        color: var(--primary);
    }
    /* Button and interactive elements */
    .stButton>button {
        background-color: var(--primary);
        color: white;
        border-radius: 8px;
        padding: 5px 15px;
        border: none;
        font-weight: 500;
    }
    .stSelectbox, .stMultiSelect {
        border-radius: 8px;
    }
    /* Overall page styling */
    .stApp {
        background-color: var(--light);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
    }
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 24px;
        border-radius: 10px 10px 0px 0px;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--light-gray);
        color: var(--primary);
    }
</style>
""", unsafe_allow_html=True)

# Modern gradient header
st.markdown("""
<div style="background: linear-gradient(90deg, #4F46E5 0%, #818CF8 100%); padding: 40px 20px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <div class="main-title" style="color: white;">Web2 vs Web3 Sorting Algorithm Benchmark</div>
    <div style="text-align: center; font-size: 20px; color: #E5E7EB; margin-bottom: 20px; font-weight: 400;">
        Comparing performance metrics across traditional and blockchain environments
    </div>
</div>
""", unsafe_allow_html=True)

# Author information with modern design
st.markdown("""
<div class="author-info" style="background: white; border: 1px solid #E5E7EB; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
    <p style="color: #4B5563; font-size: 16px; margin-bottom: 5px;">PROJECT BY</p>
    <p style="font-size: 18px; font-weight: 500; margin-bottom: 20px; color: #1F2937;">Saad (2022509) and Ahmed Ali Khan (2022054)</p>
    <p style="color: #4B5563; font-size: 16px; margin-bottom: 5px;">PURPOSE</p>
    <p style="font-size: 18px; font-weight: 400; color: #1F2937;">Comparative analysis of sorting algorithms in Web2 (Python) vs Web3 (Solidity/EVM) environments</p>
</div>
""", unsafe_allow_html=True)

# Modern sidebar styling
st.sidebar.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <h2 style="color: #4F46E5; font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
        Dashboard
    </h2>
</div>
""", unsafe_allow_html=True)

# Modern navigation options
page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Data Explorer", "Performance Visualization", "Comparative Analysis", "Insights"],
    label_visibility="collapsed"
)

# Add a subtle separator
st.sidebar.markdown("<hr style='margin: 30px 0; opacity: 0.3; border-color: #E5E7EB;'>", unsafe_allow_html=True)

# Add sidebar footer with project info
st.sidebar.markdown("""
<div style="position: fixed; bottom: 30px; width: 250px; text-align: center; color: #6B7280; font-size: 12px;">
    <p>Project Version 1.0</p>
    <p style="color: #4F46E5;">© 2025 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    web3 = pd.read_csv("../web3_gas.csv")
    web2 = pd.read_csv("../web2_benchmarks.csv")
    return web3, web2

web3, web2 = load_data()

# Get unique algorithms for selection
web3_algos = web3["Algorithm"].unique()
web2_algos = web2["Algorithm"].unique()
all_algos = sorted(list(set(list(web3_algos) + list(web2_algos))))

# Overview page
if page == "Overview":
    st.markdown('<div class="subtitle" style="font-weight: 600;">Project Overview</div>', unsafe_allow_html=True)
    
    # Apple-style intro text
    st.markdown("""
    <div style="font-size: 18px; line-height: 1.5; margin-bottom: 40px; color: #555555;">
        Discover how sorting algorithms perform differently across traditional Web2 and blockchain Web3 environments. 
        This benchmark compares efficiency metrics to help developers make optimal choices for their applications.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Web2 Environment (Python)
        In traditional computing environments, algorithm efficiency is measured by:
        - Time complexity
        - Space complexity
        - CPU execution time
        
        Python implementations focus on optimizing these metrics for better performance.
        """)
    
    with col2:
        st.markdown("""
        ### Web3 Environment (Solidity/EVM)
        In blockchain environments, different constraints apply:
        - Gas usage (transaction costs)
        - Storage costs
        - Execution limits
        
        Solidity implementations must prioritize gas efficiency over raw speed.
        """)
    
    st.markdown('<div class="subtitle">Sorting Algorithms Compared</div>', unsafe_allow_html=True)
    
    algo_descriptions = {
        "Bubble Sort": "Simple comparison-based algorithm with O(n²) average time complexity",
        "Selection Sort": "In-place comparison sort with O(n²) time complexity regardless of input",
        "Insertion Sort": "Builds sorted array one item at a time with O(n²) average time complexity",
        "Merge Sort": "Divide and conquer algorithm with O(n log n) time complexity",
        "Quick Sort": "Divide and conquer algorithm with O(n log n) average time complexity",
        "Heap Sort": "Comparison-based sort using binary heap data structure with O(n log n) time complexity",
        "Counting Sort": "Non-comparative integer sorting algorithm with O(n+k) time complexity"
    }
    
    # Display algorithm information in a table format
    for algo in all_algos:
        if algo in algo_descriptions:
            st.markdown(f"**{algo}**: {algo_descriptions[algo]}")

# Data Explorer page
elif page == "Data Explorer":
    st.markdown('<div class="subtitle">Data Explorer</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Web3 (Gas Usage)", "Web2 (Execution Time)"])
    
    with tab1:
        st.subheader("Gas Usage Data (Web3/EVM)")
        
        # Add filtering options
        selected_web3_algos = st.multiselect("Select Algorithms", web3_algos, default=web3_algos)
        
        # Filter data
        filtered_web3 = web3[web3["Algorithm"].isin(selected_web3_algos)]
        
        # Display filtered dataframe
        st.dataframe(filtered_web3)
        
        # Show basic stats
        st.markdown("### Summary Statistics")
        st.dataframe(filtered_web3.groupby("Algorithm")["Gas"].describe())
    
    with tab2:
        st.subheader("Execution Time Data (Web2/Python)")
        
        # Add filtering options
        selected_web2_algos = st.multiselect("Select Algorithms", web2_algos, default=web2_algos)
        
        # Filter data
        filtered_web2 = web2[web2["Algorithm"].isin(selected_web2_algos)]
        
        # Display filtered dataframe
        st.dataframe(filtered_web2)
        
        # Show basic stats
        st.markdown("### Summary Statistics")
        st.dataframe(filtered_web2.groupby("Algorithm")["Time (ms)"].describe())

# Performance Visualization page
elif page == "Performance Visualization":
    st.markdown('<div class="subtitle">Performance Visualization</div>', unsafe_allow_html=True)
    
    # Add selectbox for visualization type
    viz_type = st.selectbox("Select Visualization Type", 
                           ["Gas Usage (Web3)", "Execution Time (Web2)", "Side-by-Side Comparison"])
    
    if viz_type == "Gas Usage (Web3)":
        # Gas usage plot with modern color scheme
        st.markdown('<h3 style="font-size: 24px; font-weight: 600; margin-bottom: 20px; color: #1F2937;">Gas Usage by Algorithm (Web3)</h3>', unsafe_allow_html=True)
        
        # Create two columns for controls
        control_col1, control_col2 = st.columns([3, 1])
        
        # Allow user to select algorithms
        with control_col1:
            selected_algos = st.multiselect("Select Algorithms to Display", web3_algos, default=web3_algos)
        
        # Use log scale option with toggle
        with control_col2:
            use_log = st.checkbox("Log Scale", value=False)
        
        # Create plot with modern aesthetics
        fig1, ax1 = plt.subplots(figsize=(10, 6), facecolor='#FFFFFF')
        
        # Modern color palette
        colors = ['#4F46E5', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899', '#3B82F6']
        
        # Plot the selected algorithms with improved styling
        for i, algo in enumerate(selected_algos):
            d = web3[web3["Algorithm"] == algo]
            ax1.plot(d["Size"], d["Gas"], marker='o', linewidth=2.5, 
                   label=algo, color=colors[i % len(colors)])
        
        ax1.set_xlabel("Array Size", fontsize=12, fontweight='medium')
        ax1.set_ylabel("Gas Used", fontsize=12, fontweight='medium')
        
        if use_log:
            ax1.set_yscale('log')
            ax1.set_title("Gas Usage by Array Size (Log Scale)", fontsize=16, fontweight='medium', pad=20)
        else:
            ax1.set_title("Gas Usage by Array Size", fontsize=16, fontweight='medium', pad=20)
            
        # Modern grid and frame
        ax1.grid(True, linestyle='-', alpha=0.1)
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['left'].set_color('#E5E7EB')
        ax1.spines['bottom'].set_color('#E5E7EB')
        
        # Improve legend
        ax1.legend(fontsize=10, frameon=False, loc='upper left')
        
        # Improve appearance
        plt.tight_layout()
        
        # Add container with subtle shadow for the plot
        st.markdown('<div style="padding: 20px; border-radius: 12px; box-shadow: 0px 3px 10px rgba(0,0,0,0.05); background-color: white; border: 1px solid #F3F4F6;">', unsafe_allow_html=True)
        st.pyplot(fig1)
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif viz_type == "Execution Time (Web2)":
        # Time plot with modern color scheme
        st.markdown('<h3 style="font-size: 24px; font-weight: 600; margin-bottom: 20px; color: #1F2937;">Execution Time by Algorithm (Web2)</h3>', unsafe_allow_html=True)
        
        # Create two columns for controls
        control_col1, control_col2 = st.columns([3, 1])
        
        # Allow user to select algorithms
        with control_col1:
            selected_algos = st.multiselect("Select Algorithms to Display", web2_algos, default=web2_algos)
        
        # Use log scale option with modern toggle
        with control_col2:
            use_log = st.checkbox("Log Scale", value=False)
        
        # Create plot with modern aesthetics
        fig2, ax2 = plt.subplots(figsize=(10, 6), facecolor='#FFFFFF')
        
        # Modern color palette
        colors = ['#10B981', '#4F46E5', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899', '#3B82F6']
        
        # Plot the selected algorithms with improved styling
        for i, algo in enumerate(selected_algos):
            d = web2[web2["Algorithm"] == algo]
            ax2.plot(d["Size"], d["Time (ms)"], marker='o', linewidth=2.5, 
                   label=algo, color=colors[i % len(colors)])
        
        ax2.set_xlabel("Array Size", fontsize=12, fontweight='medium')
        ax2.set_ylabel("Time (ms)", fontsize=12, fontweight='medium')
        
        if use_log:
            ax2.set_yscale('log')
            ax2.set_title("Execution Time by Array Size (Log Scale)", fontsize=16, fontweight='medium', pad=20)
        else:
            ax2.set_title("Execution Time by Array Size", fontsize=16, fontweight='medium', pad=20)
            
        # Modern grid and frame
        ax2.grid(True, linestyle='-', alpha=0.1)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['left'].set_color('#E5E7EB')
        ax2.spines['bottom'].set_color('#E5E7EB')
        
        # Improve legend
        ax2.legend(fontsize=10, frameon=False, loc='upper left')
        
        # Improve appearance
        plt.tight_layout()
        
        # Add container with subtle shadow for the plot
        st.markdown('<div style="padding: 20px; border-radius: 12px; box-shadow: 0px 3px 10px rgba(0,0,0,0.05); background-color: white; border: 1px solid #F3F4F6;">', unsafe_allow_html=True)
        st.pyplot(fig2)
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:  # Side-by-Side Comparison
        st.subheader("Web2 vs Web3 Side-by-Side Comparison")
        
        # Find common algorithms between both datasets
        common_algos = list(set(web2_algos).intersection(set(web3_algos)))
        
        # Allow user to select algorithms
        selected_algo = st.selectbox("Select Algorithm", common_algos)
        
        # Create two-column layout
        col1, col2 = st.columns(2)
        
        with col1:
            # Gas usage (Web3)
            st.markdown("### Gas Usage (Web3)")
            fig_web3, ax_web3 = plt.subplots(figsize=(8, 5))
            
            d = web3[web3["Algorithm"] == selected_algo]
            ax_web3.plot(d["Size"], d["Gas"], marker='o', color='#1E3A8A', linewidth=2)
            
            ax_web3.set_xlabel("Array Size", fontsize=12)
            ax_web3.set_ylabel("Gas Used", fontsize=12)
            ax_web3.set_title(f"{selected_algo}: Gas Usage", fontsize=14)
            ax_web3.grid(True, linestyle='--', alpha=0.7)
            
            plt.tight_layout()
            st.pyplot(fig_web3)
            
        with col2:
            # Execution time (Web2)
            st.markdown("### Execution Time (Web2)")
            fig_web2, ax_web2 = plt.subplots(figsize=(8, 5))
            
            d = web2[web2["Algorithm"] == selected_algo]
            ax_web2.plot(d["Size"], d["Time (ms)"], marker='o', color='#DC2626', linewidth=2)
            
            ax_web2.set_xlabel("Array Size", fontsize=12)
            ax_web2.set_ylabel("Time (ms)", fontsize=12)
            ax_web2.set_title(f"{selected_algo}: Execution Time", fontsize=14)
            ax_web2.grid(True, linestyle='--', alpha=0.7)
            
            plt.tight_layout()
            st.pyplot(fig_web2)

# Comparative Analysis page
elif page == "Comparative Analysis":
    st.markdown('<div class="subtitle">Comparative Analysis</div>', unsafe_allow_html=True)
    
    # Array size slider
    size_options = sorted(list(set(web3["Size"].tolist())))
    selected_size = st.select_slider("Select Array Size", options=size_options)
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"Gas Usage at Size {selected_size}")
        
        # Filter data for the selected size
        size_data_web3 = web3[web3["Size"] == selected_size]
        
        # Create bar chart
        fig_gas, ax_gas = plt.subplots(figsize=(8, 6))
        
        # Sort algorithms by gas usage
        sorted_data = size_data_web3.sort_values("Gas")
        
        bars = ax_gas.barh(sorted_data["Algorithm"], sorted_data["Gas"], color='#1E3A8A')
        
        # Add data labels to bars
        for bar in bars:
            width = bar.get_width()
            label_x_pos = width * 1.01
            ax_gas.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{int(width):,}', 
                      va='center', fontsize=10)
        
        ax_gas.set_xlabel("Gas Used", fontsize=12)
        ax_gas.set_title(f"Gas Usage at Size {selected_size}", fontsize=14)
        ax_gas.grid(True, axis='x', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        st.pyplot(fig_gas)
    
    with col2:
        st.subheader(f"Execution Time at Size {selected_size}")
        
        # Filter data for the selected size
        size_data_web2 = web2[web2["Size"] == selected_size]
        
        # Create bar chart
        fig_time, ax_time = plt.subplots(figsize=(8, 6))
        
        # Sort algorithms by execution time
        sorted_data = size_data_web2.sort_values("Time (ms)")
        
        bars = ax_time.barh(sorted_data["Algorithm"], sorted_data["Time (ms)"], color='#DC2626')
        
        # Add data labels to bars
        for bar in bars:
            width = bar.get_width()
            label_x_pos = width * 1.01
            ax_time.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width:.2f}', 
                       va='center', fontsize=10)
        
        ax_time.set_xlabel("Time (ms)", fontsize=12)
        ax_time.set_title(f"Execution Time at Size {selected_size}", fontsize=14)
        ax_time.grid(True, axis='x', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        st.pyplot(fig_time)
    
    # Create efficiency comparison
    st.markdown("### Efficiency Ranking")
    
    # Calculate relative efficiency at the selected size
    web3_at_size = web3[web3["Size"] == selected_size].copy()
    web2_at_size = web2[web2["Size"] == selected_size].copy()
    
    # Normalize values (lower is better)
    if not web3_at_size.empty:
        min_gas = web3_at_size["Gas"].min()
        web3_at_size["Efficiency"] = min_gas / web3_at_size["Gas"]
    
    if not web2_at_size.empty:
        min_time = web2_at_size["Time (ms)"].min()
        web2_at_size["Efficiency"] = min_time / web2_at_size["Time (ms)"]
    
    # Display efficiency table
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Web3 Efficiency (Gas)")
        if not web3_at_size.empty:
            efficiency_web3 = web3_at_size[["Algorithm", "Gas", "Efficiency"]]
            efficiency_web3 = efficiency_web3.sort_values("Efficiency", ascending=False)
            efficiency_web3["Efficiency"] = efficiency_web3["Efficiency"].apply(lambda x: f"{x:.3f}")
            st.dataframe(efficiency_web3)
    
    with col2:
        st.markdown("#### Web2 Efficiency (Time)")
        if not web2_at_size.empty:
            efficiency_web2 = web2_at_size[["Algorithm", "Time (ms)", "Efficiency"]]
            efficiency_web2 = efficiency_web2.sort_values("Efficiency", ascending=False)
            efficiency_web2["Efficiency"] = efficiency_web2["Efficiency"].apply(lambda x: f"{x:.3f}")
            st.dataframe(efficiency_web2)

# Insights page
elif page == "Insights":
    st.markdown('<div class="subtitle">Key Insights & Trade-offs</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insights">
        <h3>Web3 (Solidity/EVM) Environment</h3>
        <ul>
            <li><span class="highlight">Gas cost</span> is the primary constraint in blockchain environments</li>
            <li>Simpler algorithms like <span class="highlight">Insertion Sort</span> or <span class="highlight">Bubble Sort</span> may outperform more complex ones for small arrays due to lower EVM overhead</li>
            <li>Gas costs increase significantly with array size, making on-chain sorting expensive for large datasets</li>
            <li>Storage operations are particularly expensive in the EVM environment</li>
        </ul>
        
        <h3>Web2 (Python) Environment</h3>
        <ul>
            <li><span class="highlight">Time complexity</span> is the main consideration in traditional computing</li>
            <li>Algorithms like <span class="highlight">Merge Sort</span> and <span class="highlight">Quick Sort</span> scale better for large arrays</li>
            <li>Python's built-in optimizations can make certain algorithms perform better than their theoretical complexity suggests</li>
        </ul>
        
        <h3>Key Takeaways</h3>
        <ul>
            <li>The best algorithm choice depends on the specific environment and constraints</li>
            <li>On-chain (Web3), <span class="highlight">minimizing gas usage</span> is critical</li>
            <li>Off-chain (Web2), <span class="highlight">minimizing execution time</span> is key</li>
            <li>Consider preprocessing data off-chain when possible to reduce on-chain costs</li>
            <li>For small arrays (n < 10), simple algorithms may be more efficient in both environments</li>
            <li>For large arrays (n > 100), the efficiency gap between algorithms becomes more pronounced</li>
        </ul>
        
        <h3>Practical Applications</h3>
        <ul>
            <li>Use these insights when developing dApps that require data sorting</li>
            <li>Consider hybrid approaches that leverage both environments' strengths</li>
            <li>For Web3 applications, prioritize minimizing on-chain operations whenever possible</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Add a section for recommendations
    st.markdown('<div class="subtitle">Recommendations</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Web3 Recommendations
        
        1. **Small Arrays (n < 10)**
           - Consider Insertion Sort for best gas efficiency
           
        2. **Medium Arrays (10 < n < 50)**
           - Evaluate the trade-off between gas costs and functionality
           - Consider off-chain sorting with on-chain verification
           
        3. **Large Arrays (n > 50)**
           - Avoid on-chain sorting entirely if possible
           - Use merkle proofs or other cryptographic methods for verification
        """)
    
    with col2:
        st.markdown("""
        ### Web2 Recommendations
        
        1. **Small Arrays (n < 10)**
           - Simple algorithms like Insertion Sort may be sufficient
           
        2. **Medium Arrays (10 < n < 1000)**
           - Quick Sort or Merge Sort provide good performance
           
        3. **Large Arrays (n > 1000)**
           - Select algorithms with O(n log n) complexity
           - Consider specialized algorithms based on data characteristics
           - Utilize parallelization for very large datasets
        """)

# Modern style footer
st.markdown("""
<div style="text-align: center; margin-top: 60px; padding: 40px 20px; background: linear-gradient(90deg, #4F46E5 0%, #818CF8 100%); border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <div style="max-width: 800px; margin: 0 auto;">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; margin-bottom: 30px;">
            <div style="flex: 1; min-width: 200px; margin-bottom: 20px;">
                <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 15px; color: white;">Project</h3>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Web2 vs Web3 Benchmark</p>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Analysis & Visualization</p>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Performance Metrics</p>
            </div>
            <div style="flex: 1; min-width: 200px; margin-bottom: 20px;">
                <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 15px; color: white;">Created By</h3>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Saad (2022509)</p>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Ahmed Ali Khan (2022054)</p>
            </div>
            <div style="flex: 1; min-width: 200px; margin-bottom: 20px;">
                <h3 style="font-size: 16px; font-weight: 600; margin-bottom: 15px; color: white;">Technologies</h3>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Python / Streamlit</p>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Matplotlib</p>
                <p style="font-size: 14px; color: #E5E7EB; margin-bottom: 8px;">Pandas</p>
            </div>
        </div>
        <div style="border-top: 1px solid rgba(255, 255, 255, 0.2); padding-top: 20px;">
            <p style="font-size: 12px; color: #E5E7EB;">© 2025 Saad (2022509) and Ahmed Ali Khan (2022054). All rights reserved.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)