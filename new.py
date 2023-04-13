import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from io import BytesIO
import pandas as pd
import re
import pickle
import time
import sqlite3
#DB management
import sqlite3
st.set_page_config(page_title="Neurotomy", page_icon=":tada:",layout="wide")
st.title(":violet[Neurotomy]")
conn=sqlite3.connect('new.db')
c=conn.cursor()

def create_usertable():
    c.execute("CREATE TABLE IF NOT EXISTS userstable(new_user TEXT,email TEXT,new_password TEXT,age INT,gender TEXT)")
def add_userdata(new_user,email,new_password,age,gender):
    c.execute('INSERT INTO userstable(new_user,email,new_password,age,gender)VALUES (?,?,?,?,?)',(new_user,email,new_password,age,gender))
    conn.commit()
def login_user(new_user,new_password):
    c.execute('SELECT * FROM userstable WHERE new_user =? AND new_password =?',(new_user,new_password))
    data=c.fetchall()
    return data
def view_all_users():
    c.execute('SELECT * FROM userstable')
    data=c.fetchall()
    return data

def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email)

def validate_password(new_password):
    pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'
    return re.match(pattern, new_password)

def validate_age(age):
    if not age.isdigit():
        return False
    age = int(age)
    if age < 0 or age > 150:
        return False
    return True

def validate_gender(gender):
    return gender.lower() in ['Male', 'Female', 'Other']



# Define a function to fetch a random image from the internet
def get_random_image():
    response = requests.get("https://source.unsplash.com/random")
    img = Image.open(BytesIO(response.content))
    return img

#sidebar for navigation
selected =option_menu("Multiple Disease Prediction System ",
                      options=["Home","Tasks","Contact us","About us","Check-in"],
                      icons = ["house check","list-task","geo-alt-fill","file-person","person-circle"],
                      orientation="horizontal",
                      styles={"container": {"padding": "0!important", "background-color": "#6cd98b"},
                              "icon": {"color": "orange", "font-size": "10px"},
                              "nav-link": {"font-size": "15px", "text-align": "left", "margin":"20px", "--hover-color": "#eee"},
                              "nav-link-selected": {"background-color": "red"}})

#home vidhi predictions
if (selected =="Home"):
    #page title
    # Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/



    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS ----
    lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_sduj9gti.json")
    lottie_coding1= load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_uqwij0uf.json")
    lottie_coding2= load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_4FGi6N.json")
    lottie_coding3= load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_yswivetl.json")

    # ---- intro ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header(":red[Multidisease Predict: An AI-based System for Early Detection and Prediction of Multiple Diseases]")
            st.write("##")
            st.write(
                """
                In recent years, the development of Artificial Intelligence (AI) has revolutionized the healthcare industry by providing advanced tools and techniques for early detection and prediction of diseases.
                One such tool is the Multidisease Predict system, which utilizes machine learning algorithms to analyze patient data and predict the likelihood of multiple diseases. 
                With the ability to detect and predict diseases at an early stage, this system offers numerous benefits for both patients and healthcare providers. 
                By identifying potential health risks before they become severe, patients can receive prompt treatment and avoid more serious health complications. 
                Meanwhile, healthcare providers can use the system's insights to make informed decisions and provide personalized care to patients. 
                In this Neurotomy, You can check your diseases before consulting the physician.
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")
            # ---- steps to login ----
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header(":green[Steps To Use Multiple Disease Prediction System]")
                st.write("##")
                st.write(
                    """
                    - Visit our Neurotomy Website.
                    - Tap on Check-in.
                    - If you are a NEW USER Create your account.
                    - If you are already Have account Please login.
                    - You will find Tasks section.Tap on it.
                    - Then Select the disease You want to check and enter the details accordingly.
                    - Click on check results, The result will appear on your screen

                    """
                )
            with right_column:
                st_lottie(lottie_coding1, height=300, key="coding1")
            st.title(":orange[We Are Here To Help You ...]")
            st.subheader(":blue[Stay at comfort of your homes and Predict your Diseases accurately with our Predictive Systems]")
            with st.container():
                st.write("---")
                left_column, right_column = st.columns(2)
            with left_column:
                st_lottie(lottie_coding2, height=300, key="coding2")
            with right_column:
                st_lottie(lottie_coding3, height=300, key="coding3")
                

    

if (selected == "Tasks"):
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_dia = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_42B8LS.json")
    lottie_heart= load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_pcqghvjn.json")
    lottie_cov = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_ukfskoun.json")
    lottie_bc = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ioxlu1zt.json")
    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header(":red[Diabetes Prediction System]")
            st.write("##")
            st.write(
                """
                Diabetes is a chronic metabolic disorder that affects millions of people worldwide.
                Early detection and prediction of diabetes is crucial for managing the disease and preventing complications. 
                In recent years, machine learning algorithms have shown promising results in predicting diabetes by analyzing patient data such as age, body mass index, blood pressure, and glucose levels. 
                These algorithms can detect patterns and correlations between these variables to identify patients who are at high risk of developing diabetes. 
                By predicting diabetes at an early stage, healthcare providers can take preventive measures and provide patients with personalized care to manage the disease. 
                Diabetes prediction using machine learning algorithms is a rapidly evolving field, and continued research in this area has the potential to improve diabetes management and outcomes for patients.
                """
            )
        with right_column:
            st_lottie(lottie_dia, height=300, key="dia")
        # ---- WHAT I DO ----
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header(":green[Heart Disease Prediction System]")
                st.write("##")
                st.write(
                    """
                    A Heart Disease Prediction System is an AI-based tool that utilizes machine learning algorithms to predict the likelihood of heart disease in individuals. 
                    By analyzing various factors such as age, gender, medical history, lifestyle, and blood pressure, these algorithms can identify individuals who may be at higher risk for developing heart disease. 
                    Early detection and prevention of heart disease is essential for improving outcomes and reducing the risk of heart attacks and other complications. 
                    Heart disease prediction systems can help healthcare providers identify high-risk individuals and implement preventive measures, such as lifestyle modifications and medication, to reduce the risk of heart disease. 
                    With the ability to provide personalized care and identify individuals who may benefit from earlier screening and follow-up care, heart disease prediction systems have the potential to revolutionize cardiovascular disease prevention and management. 
                    As research in this area continues, the development and refinement of heart disease prediction systems will be critical in reducing the burden of heart disease on individuals and society as a whole.
                    """
                )
            with right_column:
                st_lottie(lottie_heart, height=300, key="heart")
            # ---- WHAT I DO ----
            with st.container():
                st.write("---")
                left_column, right_column = st.columns(2)
                with left_column:
                    st.header(":orange[Covid-19 Prediction System]")
                    st.write("##")
                    st.write(
                        """
                        A Covid-19 prediction system is an AI-based tool that utilizes machine learning algorithms to predict the spread and impact of the Covid-19 virus.
                        By analyzing various data points such as the number of cases, fatalities, hospitalizations, and vaccination rates, these algorithms can provide insights into future trends and potential outbreaks.
                        The Covid-19 pandemic has highlighted the need for accurate and timely predictions to help governments and healthcare providers make informed decisions and plan for the future. 
                        With the ability to forecast the impact of the virus in specific regions and populations, Covid-19 prediction systems have the potential to assist in the development of effective public health policies and resource allocation. 
                        As the pandemic continues to evolve, the development and refinement of Covid-19 prediction systems will be critical in managing the spread of the virus and mitigating its impact on society.
                        """
                    )
                with right_column:
                    st_lottie(lottie_cov, height=300, key="cov")
                # ---- WHAT I DO ----
                with st.container():
                    st.write("---")
                    left_column, right_column = st.columns(2)
                    with left_column:
                        st.header(":blue[Breast Cancer Prediction System]")
                        st.write("##")
                        st.write(
                            """
                            A Breast Cancer Prediction System is an AI-based tool that utilizes machine learning algorithms to predict the likelihood of breast cancer in women. 
                            By analyzing various factors such as age, family history, lifestyle, and medical history, these algorithms can identify women who may be at higher risk for developing breast cancer. 
                            Early detection of breast cancer is essential for successful treatment and improved outcomes. Breast cancer prediction systems can help identify women who may benefit from earlier and more frequent screening and follow-up care. 
                            This can lead to more timely diagnosis and treatment, potentially improving survival rates. Breast cancer prediction systems have the potential to revolutionize breast cancer screening and prevention, allowing healthcare providers to provide personalized care and improve outcomes for women. 
                            As research in this area continues, the development and refinement of breast cancer prediction systems will be critical in the fight against breast cancer.
                            """
                        )
                    with right_column:
                        st_lottie(lottie_bc, height=300, key="bc")





if (selected == "Contact us"):
# Define a function to fetch an image from GitHub
    def get_github_image(username, repo, filepath):
        url = f"https://raw.githubusercontent.com/{username}/{repo}/main/{filepath}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
# Define the Streamlit app
    def app():
        st.subheader("Developer ")

        # Define some basic information about the developer
        Name = "S Vivek"
        Title = "Software Developer"
        Email = "vivekabhimanyu553@gmail.com"
        Website = "https://www.example.com"
        Contact = "8688595387"

        # Fetch the developer's GitHub profile picture and display it
        img = get_github_image("vivekabhimanyu", "Diabetes-Prediction-Webapp", "DSC_0160.JPG")
        st.image(img, width=400)

        # Display the developer information
        st.write(f"**Name:** {Name}")
        st.write(f"**Title:** {Title}")
        st.write(f"**Email:** {Email}")
        st.write(f"**Website:** {Website}")
        st.write(f"**contact:** {Contact}")

    # Run the Streamlit app
    if __name__ == '__main__':
        app()

if (selected == "About us"):
# Define a function to fetch an image from GitHub
    def get_github_image(username, repo, filepath):
        url = f"https://raw.githubusercontent.com/{username}/{repo}/main/{filepath}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
# Define the Streamlit app
    def app():
        st.subheader("Developer Card")

        # Define some basic information about the developer
        Name = "S Vivek"
        Title = "Software Developer"
        Email = "vivekabhimanyu553@gmail.com"
        Website = "https://www.example.com"
        Contact = "8688595387"

        # Fetch the developer's GitHub profile picture and display it
        img = get_github_image("vivekabhimanyu", "Diabetes-Prediction-Webapp", "profile_pic.png")
        st.image(img, width=400)

        # Display the developer information
        st.write(f"**Name:** {Name}")
        st.write(f"**Title:** {Title}")
        st.write(f"**Email:** {Email}")
        st.write(f"**Website:** {Website}")
        st.write(f"**contact:** {Contact}")

    # Run the Streamlit app
    if __name__ == '__main__':
        app()

if (selected == "Check-in"):
    def main():
        st.title(" #")
        menu=["Login","Signup"]
        choice=st.sidebar.selectbox(":violet[Control Panel]",menu)

        if choice == "Login":
            new_user=st.sidebar.text_input(":red[User Name]")
            new_password=st.sidebar.text_input(":red[Password]",type='password')
                
            if st.sidebar.checkbox(":violet[Login]"):
                #if password=='12345':
                create_usertable()
                result=login_user(new_user,new_password)
                if result:

                    st.success("Logged in as {}".format(new_user))
                    task=st.selectbox("Tasks",[" ","Diabetes","Heart","Covid-19","Breast Cancer"])
                    if task==" ":
                        st.caption(":red[Please choose the option]")
                    if task == "Diabetes":
                        st.subheader("Diabets Prediction Using ML")
                        st.caption(":violet[Predictions Simplified]....")
                        diabetes_model = pickle.load(open("trained_model.pkl","rb" ))
                        #getting the input data afrom users
                        #columns for input fields
                        col1,col2,col3=st.columns(3)
                        
                        with col1:
                            Pregnancies = st.number_input("Number of Pregnancies : ",min_value=0,max_value=None)
                        with col2:
                            Glucose = st.number_input("Glucose levels",min_value=0,max_value=199)
                        with col3:
                            BloodPressure = st.number_input("Blood Pressure value ",min_value=0,max_value=122)
                        with col1:
                            SkinThickness = st.number_input("SkinThickness value ",min_value=0,max_value=99)
                        with col2:
                            Insulin = st.number_input("insulin level ",min_value=0,max_value=846)
                        with col3:
                            BMI = st.number_input("BMI Value ",min_value=0.0,max_value=67.1)
                        with col1:
                            DPF = st.number_input("Diabetes pedigree Function value ",min_value=0.078,max_value=2.42)
                        with col2:
                            Age = st.number_input("Age of patitent ",min_value=21,max_value=81)
                            
                        
                        #code for prediction
                        diab_dis=""
                        
                        #creating a button for prediction
                        if st.button("Diabetes Test results"):
                            diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age]])
                        
                            if diab_prediction[0]==1:
                                diab_dis="Person is Diabetic"
                            else:
                                diab_dis="Person is Healthy!!!"
                        st.success(diab_dis)
                    elif task == "Heart":
                        st.subheader("Heart Diesase Prediction Using ML")
                        st.caption(":violet[Predictions Simplified]....")
                        #heart disease prediction
                        heart_disease_model = pickle.load(open("heart_disease_model.pkl","rb" ))
                        #radio buttons values 
                        gender_type = ["Female","Male"]
                        chest_pain_type = ["typical angina", "atypical angina", "non-anginal", "asymptomatic"]
                        fbs_type=["fasting blood sugar < 120 mg/dl", " fasting blood sugar > 120 mg/dl"]
                        restecg_type = ["normal", "stt abnormality", "lv hypertrophy"]
                        exang_type=["False","True"]
                        slope_type = ["Downsloping","Flat","upsloping"]
                        thal_type = ["normal","fixed defect"," reversible defect"]
                        #taking input from user
                        Age = st.number_input("Age of patient :",min_value=29,max_value=130)
                        Sex = st.radio("Select Gender :",gender_type)
                        chest_pain = st.radio("Select Chest Pain type :",chest_pain_type)
                        trestbps = st.number_input("Trestbps resting blood pressure :",min_value=94,max_value=200)
                        chol = st.number_input("Serum cholesterol in mg/dl :",min_value=126,max_value=564)
                        fbs =  st.radio("Fasting blood sugar type :",fbs_type)
                        restecg = st.radio("Resting electrocardiographic results :",restecg_type)                            
                        thalach = st.number_input("Maximum heart rate achieved(thalach) :",min_value=70,max_value = 202)
                        exang = st.radio(" Exercise induced angina :",exang_type)
                        oldpeek = st.number_input("Oldpeek value : ",min_value= 0,max_value=7)
                        slope = st.radio("the slope of the peak exercise ST segment :",slope_type)
                        ca = st.number_input("number of major vessels (0-3) colored by fluoroscopy",min_value=0,max_value = 3)
                        thal = st.radio("Thal :" ,thal_type)
                        #assigning values for gender 
                        if Sex =='Female':
                            Sex = 0
                        else:
                            Sex = 1
                        # assigning values for chest pain                            
                        if chest_pain == "typical angina":
                            chest_pain = 0
                        elif chest_pain == "atypical angina":
                            chest_pain = 1
                        elif chest_pain == "non-anginal":
                            chest_pain = 2
                        else:
                            chest_pain = 3
                        # assigning values for fbs
                        if fbs == "fasting blood sugar < 120 mg/dl":
                            fbs = 0
                        else :
                            fbs = 1
                        # asssigning values for restecg
                        if restecg == "normal":
                            restecg = 0
                        elif restecg == "stt abnormality":
                            restecg = 1
                        else:
                            restecg = 2
                            
                        #assigning values to exang
                        if exang == "True":
                            exang = 1
                        else:
                            exang = 0
                        if slope == "Flat":
                            slope =  1
                        elif slope == "upsloping" :
                            slope =  2
                        else:
                            slope = 0
                        if thal == 'normal' :
                            thal = 0
                        elif thal == 'fixed defect':
                            thal =  1
                        else :
                            thal =0

                                
                        # code for prediction
                        heart_dis = ""
                        #creating a button for prediction
                        if(st.button('Heart Disease Test Result')):
                            heart_prediction = heart_disease_model.predict([[Age,Sex,chest_pain,trestbps,chol,fbs,restecg,thalach,exang,oldpeek,slope,ca,thal]])
                            if (heart_prediction[0]== 0):
                                heart_dis='The Person is Healthy!!!'
                            else:
                                heart_dis='The Person has Heart Disease'
                            st.success(heart_dis)
                    elif task =="Covid-19":
                        st.subheader("Covid-19 Prediction Using ML")
                        st.caption(":violet[Predictions Simplified]....")
                        covid19_model = pickle.load(open("covid_model.pkl","rb" ))
                        #radio button values
                        Diabetes=["Yes","No"]
                        Cardio_Vascular_Diseases=["Yes","No"]
                        Sickle_cell_diesases=["Yes","No"]
                        Immuno_deficiency_disease=["Yes","No"]
                        Down_syndrome=["Yes","No"]
                        cancer=["Yes","No"]
                        Chronic_Respiratory_disease=["Yes","No"]
                        Hypertension=["Yes","No"]
                        Vaccinated=["Yes","No"]

                        #getting the input dat afrom users
                        #0--> no and 1---> health issues is there
  
                        Age = st.number_input("Enter Your Age : ",min_value=10,max_value=100)
                        BMI = st.number_input("Enter Your BMI : ",min_value=10,max_value=80)
                        Diabetes = st.radio("Do You Have Diabetes ?? : ",Diabetes)
                        Cardio_Vascular_Diseases = st.radio("Do You Have cardio vascular disease ??",Cardio_Vascular_Diseases)
                        Sickle_cell_diesases = st.radio("Do You Have Sickle_cell_diesases ?",Sickle_cell_diesases)
                        Immuno_deficiency_disease = st.radio("Do You Have Immuno_deficiency_disease ",Immuno_deficiency_disease)
                        Down_syndrome = st.radio("Do You Have Down_syndrome ?",Down_syndrome)
                        cancer = st.radio("Do You Have Cancer ?",cancer)
                        Chronic_Respiratory_disease = st.radio("Do You Have Chronic_Respiratory_disease ?",Chronic_Respiratory_disease)
                        Hypertension = st.radio("Do You Have Hypertension ?",Hypertension)
                        Vaccinated = st.radio(" Are You Vaccinated ?",Vaccinated)

                        #Assigning values for diseases
                        if Diabetes=='Yes':
                            Diabetes=1
                        else:
                            Diabetes=0
                        if Cardio_Vascular_Diseases=='Yes':
                            Cardio_Vascular_Diseases=1
                        else:
                            Cardio_Vascular_Diseases=0
                        if Sickle_cell_diesases=='Yes':
                            Sickle_cell_diesases=1
                        else:
                            Sickle_cell_diesases=0
                        if Immuno_deficiency_disease=='Yes':
                            Immuno_deficiency_disease=1
                        else:
                            Immuno_deficiency_disease=0
                        if Down_syndrome=='Yes':
                            Down_syndrome=1
                        else:
                            Down_syndrome=0
                        if cancer=='Yes':
                            cancer=1
                        else:
                            cancer=0
                        if Chronic_Respiratory_disease=='Yes':
                            Chronic_Respiratory_disease=1
                        else:
                            Chronic_Respiratory_disease=0
                        if Hypertension=='Yes':
                            Hypertension=1
                        else:
                            Hypertension=0
                        if Vaccinated=='Yes':
                            Vaccinated=1
                        else:
                            Vaccinated=0
  
                        #code for prediction
                        covid_dis=''
  
                        #creating a buttion for prediction
                        if st.button('covid-19 test results'):
                            covid_prediction=covid19_model.predict([[Age,BMI,Diabetes,Cardio_Vascular_Diseases,Sickle_cell_diesases,Immuno_deficiency_disease,Down_syndrome,cancer,Chronic_Respiratory_disease,Hypertension,Vaccinated]])
                            if covid_prediction[0]==0:
                                covid_dis="Person is healthy"
                            else:
                                covid_dis="person effected by covid-19"
                            st.success(covid_dis) 
                    elif task =="Breast Cancer":
                        st.subheader("Breast Cancer Prediction Using ML")
                        st.caption(":violet[Predictions Simplified]....")
                        breast_cancer_model = pickle.load(open("breast_cancer_model.pkl","rb"))
                        #getting the inputs from the users
                        #columns for inpt fields
                        col1,col2,col3,col4,col5=st.columns(5)

                        with col1:
                            mean_radius = st.number_input("Mean radius ",min_value = 6.0,max_value = 28.0,format="%.2f")
                        with col2:
                            mean_texture = st.number_input("Mean texture ",min_value = 9.0,max_value = 40.0,format="%.2f")
                        with col3:
                            mean_perimeter = st.number_input("Mean radius ",min_value = 43.0,max_value =190.0 ,format="%.2f")
                        with col4:
                            mean_area = st.number_input("Mean area ",min_value = 143.0,max_value = 2500.0,format= "%.2f")
                        with col5:
                            mean_smoothness = st.number_input("Mean smoothness ",min_value =0.05263 ,max_value=0.16340 , format = "%.5f")
                        with col1:
                            mean_compactness = st.number_input("Mean compactness ",min_value =0.01938,max_value= 0.34540, format = "%.5f")
                        with col2:
                            mean_concavity = st.number_input("Mean concavity ",min_value =0.0000 ,max_value=0.4268 , format = "%.4f")
                        with col3:
                            mean_concave_points = st.number_input("Mean concave points ",min_value =0.00000 ,max_value= 0.20120, format = "%.5f")
                        with col4:
                            mean_symmetry = st.number_input("Mean symmetry ",min_value =0.1060 ,max_value=0.3040, format = "%.4f")
                        with col5:
                            mean_fractal_dimension = st.number_input("Mean fractal dimension ",min_value = 0.04996,max_value=0.09744, format = "%.5f")
                        with col1:
                            error_radius = st.number_input("Radius error " , min_value = 0.1115, max_value = 2.8730 , format = "%.4f")
                        with col2:
                            error_texture = st.number_input("Texture error " , min_value =0.3602 , max_value = 4.8850 , format = "%.4f")
                        with col3:
                            error_perimeter = st.number_input("Perimeter error " , min_value = 0.757 , max_value =21.980  , format = "%.3f")
                        with col4:
                            error_area = st.number_input("Area error " , min_value = 6.802, max_value =542.200  , format = "%.3f")
                        with col5:
                            error_smoothness = st.number_input("Smoothness error " , min_value =0.001713 , max_value = 0.031130 , format = "%.6f")
                        with col1:
                            error_compactness = st.number_input("Compactness error " , min_value = 0.002252, max_value = 0.125400 , format = "%.6f")
                        with col2:
                            error_concavity= st.number_input("Concavvity error " , min_value =0.00000 , max_value = 0.39600 , format = "%.5f")
                        with col3:
                            error_concave_points = st.number_input("Concave points error " , min_value = 0.0000, max_value = 0.05279 , format = "%.5f")
                        with col4:
                            error_symmetry = st.number_input("Symmetry error " , min_value = 0.007882, max_value = 0.078950 , format = "%.6f")
                        with col5:
                            error_fractal_dimension = st.number_input("Fractal dimension error " , min_value = 0.000895, max_value =0.029840  , format = "%.6f")
                        with col1:
                            worst_radius = st.number_input("Worst radius ",min_value =7.930 ,max_value=36.040,format= "%.3f")
                        with col2:
                            worst_texture = st.number_input("Worst  texture ",min_value = 12.02 ,max_value= 49.54,format= "%.2f")
                        with col3:
                            worst_perimeter = st.number_input("Worst perimeter ",min_value = 50.40, max_value= 251.20,format= "%.2f")
                        with col4:
                            worst_area = st.number_input("Worst area ",min_value =185.20 ,max_value= 4254.00,format= "%.2f")
                        with col5:
                            worst_smoothness = st.number_input("Worst smoothness ",min_value = 0.07117, max_value= 0.22260, format= "%.5f")
                        with col1:
                            worst_compactness = st.number_input("Worst  compactness ",min_value = 0.02729,max_value= 1.05800,format= "%.5f")
                        with col2:
                            worst_concavity = st.number_input("Worst concavity ",min_value =0.00000 , max_value= 1.25200, format= "%.5f")
                        with col3:
                            worst_concave_points = st.number_input("Worst concave points ",min_value =0.0000, max_value=1.2910, format= "%.4f")
                        with col4:
                            worst_symmetry = st.number_input("Worst symmetry ",min_value = 0.1565, max_value=0.6638, format= "%.4f")
                        with col5:
                            worst_fractal_dimension = st.number_input("Worst fractal dimension ",min_value =0.05504 ,max_value=0.20750,format= "%.5f")
    
                        #code for prediction
                        bst_cnr = ""
                        #creating a button for prediction
                        if(st.button('Breast Cancer Results')):
                            bst_pre = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,
                                        error_radius,error_texture,error_perimeter,error_area,error_smoothness,error_compactness,error_concavity,error_concave_points,error_symmetry,error_fractal_dimension,
                                        worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
                            if bst_pre[0]==0:
                                bst_cnr=" Malignant Tumor Found" +" "+ "&" +" "+ " Consult Surgeon Immediately!!!! "
                                bst_cnr="high risk"
                            else:
                                bst_cnr=" Benign Tumor Found" +" "+ "&" +" " +"Better To Consult Doctor"
                            st.success(bst_cnr)
                else:
                    st.warning("Incorrect Email/Password")
                
        elif choice == "Signup":
            st.subheader("Create a new account")
            new_user =st.text_input("Username")
            email=st.text_input("Email")
            new_password=st.text_input("Password",type='password')
            age = st.text_input("Age")
            gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
            

            if st.button("Signup"):
                create_usertable()
                add_userdata(new_user,email,new_password,age,gender)
                if not validate_email(email):
                    st.error("Please enter a valid email address")
                elif not validate_password(new_password):
                    st.error("Password must contain at least 8 characters, including 1 uppercase letter, 1 lowercase letter, and 1 number")
                elif not validate_age(age):
                    st.error("Please enter a valid age (0-150)")
                elif not validate_gender(gender):
                    st.error("Please select a valid gender")
                else:
                    st.success("You have succesfully created a valid Account")
                    st.info("Go to Login Menu to Login")





    if __name__ =='__main__':
        main()



