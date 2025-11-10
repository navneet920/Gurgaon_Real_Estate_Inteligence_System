import pandas as pd
import pickle
import streamlit as st

def recommended_system():
    # Load data
    location_df = pickle.load(open('model/location_distance.pkl', 'rb'))
    cosine_sim1 = pickle.load(open('model/cosine_sim1.pkl', 'rb'))
    cosine_sim2 = pickle.load(open('model/cosine_sim2.pkl', 'rb'))
    cosine_sim3 = pickle.load(open('model/cosine_sim3.pkl', 'rb'))

    # Recommendation function
    def recommend_properties_with_scores(property_name, top_n=5):
        cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
        sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
        sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
        top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
        top_properties = location_df.index[top_indices].tolist()
        recommendations_df = pd.DataFrame({
            'PropertyName': top_properties,
            'SimilarityScore': top_scores
        })
        return recommendations_df

    # UI Section
    st.title('Apartment Search & Recommendations')

    # Select location and radius
    selected_location = st.selectbox('Select Location', sorted(location_df.columns.to_list()))
    radius = st.number_input("Enter Radius (in Kms)", min_value=1)

    # When Search button clicked, store apartments in session_state
    if st.button('Search Apartments'):
        result_series = location_df[location_df[selected_location] < radius * 1000][selected_location]
        if not result_series.empty:
            st.session_state['apartments_list'] = result_series.index.tolist()
            st.success(f"Found {len(result_series)} apartments within {radius} Kms of {selected_location}")
        else:
            st.warning(f"No Apartments found within {radius} Kms from {selected_location}")
            st.session_state['apartments_list'] = []

    # If apartments exist in session_state, allow apartment selection and show recommendations
    if 'apartments_list' in st.session_state and st.session_state['apartments_list']:
        selected_apartment = st.radio('Select an Apartment:', st.session_state['apartments_list'])
        if selected_apartment:
            st.subheader(f"Top 5 Recommended Apartments for: {selected_apartment}")
            recommendation_df = recommend_properties_with_scores(selected_apartment)
            st.dataframe(recommendation_df['PropertyName'])
