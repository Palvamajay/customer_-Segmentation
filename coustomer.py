import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('logistic_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('🧠 Customer Segmentation Prediction App')

# ---- Personal Information ----
st.header("👤 Personal Information")
col1, col2, col3 = st.columns(3)
with col1:
    Education = st.selectbox('Education Level', ['Basic', 'Graduation', 'PhD', 'Master', '2n Cycle'])
with col2:
    Marital_Status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced', 'Widow', 'Together'])
with col3:
    Income = st.number_input('Annual Income (€)', value=0.0)

# ---- Family & Membership ----
st.header("👪 Family & Membership")
col1, col2, col3 = st.columns(3)
with col1:
    Kidhome = st.number_input('No. of Kids', value=0, min_value=0)
with col2:
    Teenhome = st.number_input('No. of Teenagers', value=0, min_value=0)
with col3:
    Recency = st.number_input('Days Since Last Purchase', value=0)

# ---- Spending ----
st.header("🛒 Spending on Products")
col1, col2, col3 = st.columns(3)
with col1:
    MntWines = st.number_input('Wine (€)', value=0)
    MntMeatProducts = st.number_input('Meat (€)', value=0)
with col2:
    MntFruits = st.number_input('Fruits (€)', value=0)
    MntFishProducts = st.number_input('Fish (€)', value=0)
with col3:
    MntSweetProducts = st.number_input('Sweets (€)', value=0)
    MntGoldProds = st.number_input('Gold (€)', value=0)

# ---- Purchases ----
st.header("🛍️ Purchases")
col1, col2, col3 = st.columns(3)
with col1:
    NumDealsPurchases = st.number_input('Deals', value=0)
    NumCatalogPurchases = st.number_input('Catalog', value=0)
with col2:
    NumWebPurchases = st.number_input('Web', value=0)
    NumStorePurchases = st.number_input('In-Store', value=0)
with col3:
    NumWebVisitsMonth = st.number_input('Web Visits/Month', value=0)

# ---- Campaigns ----
st.header("📢 Campaign Responses")
col1, col2, col3 = st.columns(3)
with col1:
    AcceptedCmp1 = st.checkbox('Campaign 1')
    AcceptedCmp2 = st.checkbox('Campaign 2')
with col2:
    AcceptedCmp3 = st.checkbox('Campaign 3')
    AcceptedCmp4 = st.checkbox('Campaign 4')
with col3:
    AcceptedCmp5 = st.checkbox('Campaign 5')
    Complain = st.checkbox('Customer Complained')

# ---- Overall Response ----
st.header("📈 Overall")
Response = st.checkbox('Responded to Campaign')

# --- Convert categorical values ---
Education_map = {'Basic': 0, 'Graduation': 1, 'PhD': 2, 'Master': 3, '2n Cycle': 4}
Marital_Status_map = {'Single': 0, 'Married': 1, 'Divorced': 2, 'Widow': 3, 'Together': 4}

Education = Education_map[Education]
Marital_Status = Marital_Status_map[Marital_Status]

# --- Convert checkboxes to int ---
AcceptedCmp1, AcceptedCmp2, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5 = map(int, [AcceptedCmp1, AcceptedCmp2, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5])
Complain = int(Complain)
Response = int(Response)

# --- Prepare input ---

input_data = np.array([[Education, Marital_Status, Income, Kidhome, Teenhome,
                        Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts,
                        MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases,
                        NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth,
                        AcceptedCmp1, AcceptedCmp2, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5]])


# --- Predict ---
if st.button('🔍 Predict Complaint Risk'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error('⚠️ This customer is likely to **file a complaint**.')
    else:
        st.success('✅ This customer is **not likely to complain**.')

st.markdown("---")
st.subheader("⭐ Rate This App")

rating = st.slider('How would you rate your experience?', min_value=1, max_value=5, value=3)

if st.button("Submit Rating"):
    if rating >= 3:
        st.success(f"🎉 Thank you for rating us {rating} out of 5!")
        st.write("We appreciate your feedback!")
        st.balloons()
    else:
        st.warning(f"Thank you for rating us {rating} out of 5.")
        st.write("We will work on improving the app. 😞")
 


