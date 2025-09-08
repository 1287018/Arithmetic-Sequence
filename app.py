import streamlit as st

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

def main():
    # App title and description
    st.title("🔢 Arithmetic Sequence Calculator")
    st.markdown("Calculate and display arithmetic sequences based on your input parameters.")
    
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
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=1.0,
            help="The constant difference between consecutive terms"
        )
    
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
            
            # Calculate the arithmetic sequence
            sequence = calculate_arithmetic_sequence(first_term, common_difference, num_terms)
            
            # Display results
            st.subheader("Results")
            
            # Show sequence formula
            st.markdown(f"**Formula:** aₙ = {first_term} + (n-1) × {common_difference}")
            
            # Display sequence in multiple formats
            tab1, tab2, tab3 = st.tabs(["List View", "Table View", "Summary"])
            
            with tab1:
                st.markdown("**Arithmetic Sequence:**")
                # Display sequence as a formatted string
                sequence_str = ", ".join([str(term) for term in sequence])
                st.code(sequence_str, language=None)
            
            with tab2:
                # Create a table with term number and value
                import pandas as pd
                df = pd.DataFrame({
                    'Term Number (n)': range(1, num_terms + 1),
                    'Term Value (aₙ)': sequence
                })
                st.dataframe(df, use_container_width=True)
            
            with tab3:
                # Display summary statistics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("First Term", f"{sequence[0]}")
                
                with col2:
                    st.metric("Last Term", f"{sequence[-1]}")
                
                with col3:
                    st.metric("Sum of Terms", f"{sum(sequence)}")
                
                with col4:
                    st.metric("Range", f"{sequence[-1] - sequence[0]}")
        
        except ValueError as e:
            st.error(f"Invalid input: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    # Add information section
    st.markdown("---")
    st.subheader("About Arithmetic Sequences")
    
    with st.expander("Learn More"):
        st.markdown("""
        **Arithmetic Sequence:** A sequence where each term after the first is obtained by adding a constant value (common difference) to the previous term.
        
        **Formula:** aₙ = a₁ + (n-1)d
        
        Where:
        - aₙ = nth term
        - a₁ = first term  
        - d = common difference
        - n = term number
        
        **Examples:**
        - 2, 4, 6, 8, 10... (first term = 2, common difference = 2)
        - 10, 7, 4, 1, -2... (first term = 10, common difference = -3)
        - 5, 5, 5, 5, 5... (first term = 5, common difference = 0)
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
