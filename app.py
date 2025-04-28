import streamlit as st
import requests

def main():
    st.title("Titanic Feature Selection")

    # Dropdown for 'pclass'
    pclass = st.selectbox("Select Passenger Class (pclass):", [3, 2, 1])

    # Dropdown for 'sex'
    sex = st.selectbox("Select Sex:", ['male', 'female'])

    # Dropdown for 'sibsp'
    sibsp = st.selectbox("Select Number of Siblings/Spouses Aboard (sibsp):", [0, 1, 8, 3, 4, 2, 5])

    # Dropdown for 'parch'
    parch = st.selectbox("Select Number of Parents/Children Aboard (parch):", [0, 1, 2, 5, 3, 4, 6])

    # Text input for 'fare'
    fare = st.text_input("Enter Fare Value:", "")

    # Dropdown for 'embarked'
    embarked = st.selectbox("Select Port of Embarkation (embarked):", ['S', 'C', 'Q'])

    # # Submit button
    # if st.button("Submit"):
    #     st.success(f"You selected: \n- Pclass: {pclass} \n- Sex: {sex} \n- SibSp: {sibsp} \n- Parch: {parch} \n- Embarked: {embarked} \n- Fare: {fare}")

    # Submit button
    if st.button("Submit"):
        try:
            # Prepare the payload
            payload = {
                "pclass": pclass,
                "sex": sex,
                "sibsp": sibsp,
                "parch": parch,
                "fare": fare,
                "embarked": embarked
                
            }

            # Send the data to the REST API
            response = requests.post("http://localhost:5000/predict", json=payload)

            # Handle the response
            if response.status_code == 200:
                result = response.json()
                st.success(f"API Response: {result['prediction']}")
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
