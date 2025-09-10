import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def calculate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Calculate arithmetic sequence given first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): Number of terms to generate
    
    Returns:
        list: List of arithmetic sequence terms
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def calculate_geometric_sequence(first_term, common_ratio, num_terms):
    """
    Calculate geometric sequence given first term, common ratio, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_ratio (float): The common ratio between consecutive terms
        num_terms (int): Number of terms to generate
    
    Returns:
        list: List of geometric sequence terms
    """
    sequence = []
    for i in range(num_terms):
        term = first_term * (common_ratio ** i)
        sequence.append(term)
    return sequence

def calculate_geometric_series_sum(first_term, common_ratio, num_terms):
    """
    Calculate the sum of a finite geometric series.
    
    Args:
        first_term (float): The first term of the sequence
        common_ratio (float): The common ratio between consecutive terms
        num_terms (int): Number of terms to sum
    
    Returns:
        float: Sum of the geometric series
    """
    if common_ratio == 1:
        return first_term * num_terms
    else:
        return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)

def main():
    # App title and description
    st.title("🔢 Arithmetic Sequence Calculator")
    st.markdown("Calculate and display arithmetic sequences based on your input parameters.")
    
    # Add some spacing
    st.markdown("---")
    
    # Create sequence type selector
    st.subheader("Sequence Type")
    sequence_type = st.radio(
        "Choose sequence type:",
        ["Arithmetic Sequence", "Geometric Sequence"],
        horizontal=True,
        help="Select whether to calculate arithmetic or geometric sequences"
    )
    
    # Add some spacing
    st.markdown("---")
    
    # Create input section
    st.subheader("Input Parameters")
    
    # Create three columns for inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=1.0,
            help="The first term of the arithmetic sequence"
        )
    
    with col2:
        if sequence_type == "Arithmetic Sequence":
            common_difference = st.number_input(
                "Common Difference (d)",
                value=1.0,
                step=1.0,
                help="The constant difference between consecutive terms"
            )
            common_ratio = 1.0  # Default value when not used
        else:  # Geometric Sequence
            common_ratio = st.number_input(
                "Common Ratio (r)",
                value=2.0,
                step=0.1,
                help="The constant ratio between consecutive terms"
            )
            common_difference = 0.0  # Default value when not used
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to calculate (maximum 1000)"
        )
    
    # Add spacing
    st.markdown("---")
    
    # Validation and calculation
    if st.button("Calculate Sequence", type="primary"):
        try:
            # Convert num_terms to integer for validation
            num_terms = int(num_terms)
            
            # Input validation
            if num_terms <= 0:
                st.error("Number of terms must be a positive integer.")
                return
            
            if num_terms > 1000:
                st.error("Number of terms cannot exceed 1000.")
                return
            
            # Calculate the sequence based on type
            if sequence_type == "Arithmetic Sequence":
                sequence = calculate_arithmetic_sequence(first_term, common_difference, num_terms)
                series_sum = sum(sequence)  # Simple sum for arithmetic
            else:  # Geometric Sequence
                sequence = calculate_geometric_sequence(first_term, common_ratio, num_terms)
                series_sum = calculate_geometric_series_sum(first_term, common_ratio, num_terms)
            
            # Display results
            st.subheader("Results")
            
            # Show sequence formulas
            col_form1, col_form2 = st.columns(2)
            with col_form1:
                if sequence_type == "Arithmetic Sequence":
                    st.markdown(f"**Explicit Formula:** aₙ = {first_term} + (n-1) × {common_difference}")
                else:  # Geometric Sequence
                    st.markdown(f"**Explicit Formula:** aₙ = {first_term} × {common_ratio}^(n-1)")
            with col_form2:
                if sequence_type == "Arithmetic Sequence":
                    st.markdown(f"**Recursive Formula:** a₁ = {first_term}, aₙ = aₙ₋₁ + {common_difference}")
                else:  # Geometric Sequence
                    st.markdown(f"**Recursive Formula:** a₁ = {first_term}, aₙ = aₙ₋₁ × {common_ratio}")
            
            # Display sequence in multiple formats
            tab1, tab2, tab3, tab4 = st.tabs(["List View", "Table View", "Charts", "Summary"])
            
            with tab1:
                st.markdown(f"**{sequence_type}:**")
                # Display sequence as a formatted string
                sequence_str = ", ".join([str(term) for term in sequence])
                st.code(sequence_str, language=None)
                
                # Display series sum
                st.markdown(f"**Series Sum:** {series_sum}")
            
            with tab2:
                # Create a table with term number and value
                import pandas as pd
                df = pd.DataFrame({
                    'Term Number (n)': range(1, num_terms + 1),
                    'Term Value (aₙ)': sequence
                })
                st.dataframe(df, width='stretch')
            
            with tab3:
                # Create interactive charts
                st.markdown("**Sequence Visualization:**")
                
                # Create chart type selector
                chart_col1, chart_col2 = st.columns(2)
                
                with chart_col1:
                    # Line chart
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(
                        x=list(range(1, num_terms + 1)),
                        y=sequence,
                        mode='lines+markers',
                        name=sequence_type,
                        line=dict(color='#1f77b4', width=3),
                        marker=dict(size=8, color='#ff7f0e')
                    ))
                    fig_line.update_layout(
                        title='Sequence Line Plot',
                        xaxis_title='Term Number (n)',
                        yaxis_title='Term Value (aₙ)',
                        height=400,
                        showlegend=False
                    )
                    st.plotly_chart(fig_line, use_container_width=True)
                
                with chart_col2:
                    # Bar chart
                    fig_bar = go.Figure()
                    fig_bar.add_trace(go.Bar(
                        x=list(range(1, num_terms + 1)),
                        y=sequence,
                        name=sequence_type,
                        marker_color='#2ca02c'
                    ))
                    fig_bar.update_layout(
                        title='Sequence Bar Chart',
                        xaxis_title='Term Number (n)',
                        yaxis_title='Term Value (aₙ)',
                        height=400,
                        showlegend=False
                    )
                    st.plotly_chart(fig_bar, use_container_width=True)
                
                # Pattern analysis
                st.markdown("**Pattern Analysis:**")
                if len(sequence) > 1:
                    if sequence_type == "Arithmetic Sequence":
                        differences = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
                        st.markdown(f"• **Common Difference:** {common_difference} (consistent across all terms)")
                        st.markdown(f"• **Sequence Type:** {'Increasing' if common_difference > 0 else 'Decreasing' if common_difference < 0 else 'Constant'}")
                        if num_terms >= 3:
                            slope = (sequence[-1] - sequence[0]) / (num_terms - 1)
                            st.markdown(f"• **Average Rate of Change:** {slope:.2f} per term")
                    else:  # Geometric Sequence
                        ratios = [sequence[i+1] / sequence[i] if sequence[i] != 0 else 0 for i in range(len(sequence)-1)]
                        st.markdown(f"• **Common Ratio:** {common_ratio} (consistent across all terms)")
                        st.markdown(f"• **Sequence Type:** {'Increasing' if (common_ratio > 1 and first_term > 0) or (0 < common_ratio < 1 and first_term < 0) else 'Decreasing' if (0 < common_ratio < 1 and first_term > 0) or (common_ratio > 1 and first_term < 0) else 'Alternating' if common_ratio < 0 else 'Constant'}")
                        if num_terms >= 2:
                            growth_factor = (abs(sequence[-1]) / abs(sequence[0])) ** (1/(num_terms-1)) if sequence[0] != 0 else 0
                            st.markdown(f"• **Growth Factor:** {growth_factor:.3f} per term")
            
            with tab4:
                # Display summary statistics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("First Term", f"{sequence[0]}")
                
                with col2:
                    st.metric("Last Term", f"{sequence[-1]}")
                
                with col3:
                    st.metric("Sum of Series", f"{series_sum}")
                
                with col4:
                    st.metric("Range", f"{sequence[-1] - sequence[0]}")
        
        except ValueError as e:
            st.error(f"Invalid input: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    # Add information section
    st.markdown("---")
    st.subheader("About Sequences")
    
    with st.expander("Learn More"):
        st.markdown("""
        **Arithmetic Sequence:** A sequence where each term after the first is obtained by adding a constant value (common difference) to the previous term.
        
        **Arithmetic Formula:** aₙ = a₁ + (n-1)d
        
        **Geometric Sequence:** A sequence where each term after the first is obtained by multiplying the previous term by a constant value (common ratio).
        
        **Geometric Formula:** aₙ = a₁ × r^(n-1)
        
        **Geometric Series Sum:** S = a₁ × (1 - r^n) / (1 - r) when r ≠ 1, or S = a₁ × n when r = 1
        
        Where:
        - aₙ = nth term
        - a₁ = first term  
        - d = common difference (arithmetic)
        - r = common ratio (geometric)
        - n = term number
        
        **Examples:**
        - Arithmetic: 2, 4, 6, 8, 10... (first term = 2, common difference = 2)
        - Arithmetic: 10, 7, 4, 1, -2... (first term = 10, common difference = -3)
        - Geometric: 2, 6, 18, 54... (first term = 2, common ratio = 3)
        - Geometric: 100, 50, 25, 12.5... (first term = 100, common ratio = 0.5)
        """)

if __name__ == "__main__":
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Calculator",
        page_icon="🔢",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    main()
