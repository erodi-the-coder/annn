import streamlit as st 

st.set_page_config( page_title ="My coding journy" , layout = 'wide' )

from streamlit_option_menu import option_menu



st.subheader("A grade 8 student that want to be a Software engineer")


st.title("Why you should be a software engineer (of cousre its only for those who did make desition yet)")


st.write('Hello I am Erodiya Fikadu a 13 year old who made this web page')


st. write("If you think this is cool and you want to be a software engineer just like me wait till you know more")

st.write(' in whis website you will know about each types of softwares , I will over the to main ones')

with st.container():

    st.write('---')

    left_column, right_column  = st.columns(2)

    with left_column:
         st.header("What is a software engineer")
def jls_extract_def():
    return'###'

      


st.write(jls_extract_def())
      
"""

             They are people who test and make big websites like the elearning from GSS

              - software engineering is basicly like an engineerwho built a house but they build websites

              - if you want to be a software engineer I recomend you see somethings on youtube
              - I am curently learning python porgraming language and let me tell it is mad good
              - I will describe more about it 
              """
with st.sidebar:
    selected = option_menu(
        menu_title = "introduction to coding",
        options=["software engineer", "web developer"],
    )
    if selected == "software engineer":
     st.title(f"Software engineers are people who are manage and kinda superior to web developers also they get paid a 20-25% more  they earn 70,000$ to 167,000$ yearly and 20,000-45,000 ETB and make the them mostly demanded ")
    if selected == "web developer":
     st.title(f"A web developer is a builder that makes websites just like this one it is divided into 2 front end and back end developing , front end is basicly what the yor sees and can intreact ; back end is what the users data is placed and stored eg: your elearning account is saved in the back and when ever you login you tell your computer to give you what ever you saved ; the cobination of those to is called fullstack developer also they earn 60,000$-120,000% yearly , 18,000-35,000 ETB")
    orientation="horizontal",
    
 
        
    

                    
            