from operator import index
from unittest import result
import numpy as np
import streamlit as st
from PIL import Image
import pickle


# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Diabetics  Predictor")
img=Image.open("diabetics.jpg")
st.image(img, width=200)

# Number of Pregnency
No_pregent = st.selectbox('Pregnancies',df['Pregnancies'].unique(),index=2 )

# Level  of Glucose
Glucose_level = st.selectbox('Glucose',df['Glucose'].unique())

# # Ram
blood_pressure = st.number_input('Blood Pressure)', min_value=1,step=1)

# weight
skinThickness= st.number_input('SkinThickness	', min_value=1,step=1)

# # Touchscreen
insulin_level= st.number_input('nsulin	', min_value=1,step=1)

# # IPS
bmi= st.number_input('BMI', min_value=1,step=1)
	
# # screen size
diabetes_pedigree_function= st.number_input('DiabetesPedigreeFunction', min_value=1,step=1)

# # resolution
age= st.number_input('Age', min_value=1,step=1)


if st.button('Predict Status') :
    
    try:
        query = np.array([Glucose_level,insulin_level,bmi,age])

        # query = query.reshape(1,4)
        # st.title(print(type(pipe.predict([query]))))
        # st.title(print(pipe.predict([query])))
        result=int(pipe.predict([query]))
        ans=""
        if result ==0:
            print("Zreo")
            print("Zreo")
            print("Zreo")
            ans="Non Dieabetic"
        else:
            ans="Dieabetic"
            print("one")
            print("one")
        st.title("The predicted price of this configuration is "+ str(int(pipe.predict([query]))))
        st.title("The predicted price of this configuration is "+ ans)
    except Exception as ep:
        st.title(type(ep))
        print(type(ep))
        error=str(ep)
        error=error.title()
#         st.title( error+" Not Possible Please Enter a valid Configration ")
#         # st.title("Weight of the Laptop Cannot Be Zero")


