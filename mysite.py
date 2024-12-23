import streamlit as st

import pandas as pd


# Set up the page configuration
st.set_page_config(
    page_title="Lakshmi Sailaja's Website",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.sidebar.title("Navigation Page")
menu = st.sidebar.radio(
    "Go to page",
    ("Home", "About Me", "Contact", "Projects")
)

   
    
# Home Page
if menu == "Home":
    st.markdown(
"""
    <h1 style='color: blue;'><i>🌟Welcome Lakshmi Sailaja🌟</i></h1>
""",
    unsafe_allow_html=True
)

    st.write("""
    Hi there! This is a simple website built using **Streamlit**.  
    Use the menu on the left to navigate through different sections.  
    """)
    st.image("codingisfun_logo.png", caption="Welcome to my website!", use_container_width =True)
    

# About Me Page
elif menu == "About Me":
    st.markdown(
"""
    <h1 style='color: blue;'><u><i>About Me</i></u></h1>
""",
    unsafe_allow_html=True
)
    # st.title("About Me")
    st.write("""
    Hello! I'm **Lakshmi Sailaja**, a passionate learner, and tech enthusiast.  
    This is my personal website where I share my projects and information about myself.
    """)

    st.subheader("Hobbies and Interests")
    st.write("""
    - 💻 Programming and Development  
    - 📚 Reading Tech Blogs  
    - 🎨 Designing and Art  
    - 🎮 Gaming  
    """)

# Contact Page
elif menu == "Contact":
    st.markdown(
"""
    <h1 style='color: blue;'><u><i>Contact Me</i></u></h1>
""",
    unsafe_allow_html=True
)
    # st.title("Contact Me")
    st.write("""
    Feel free to reach out to me through any of the platforms below:
    - **Email**: lakshmisailaja.kalisetti@gmail.com  
    - **GitHub**: [MyGitHubProfile](https://github.com/Luckylakshmisailaja)  
    - **LinkedIn**: [MyLinkedInProfile](https://www.linkedin.com/feed/)  
    """)

    
    with st.form("contact_form"):
        name = st.text_input("Enter Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            # save the data to csv file
            data = {"name": name, "email": email, "message": message}
            df= pd.DataFrame([data])
            df.to_csv('contact_form.csv', mode='a', header=False, index=False)
            st.success("Your message has been sent successfully! 🎉", icon="🚀")
        else:
            st.error("There was an error sending your message.", icon="😨")            
   

# Projects Page
elif menu == "Projects":
    st.markdown(
"""
    <h1 style='color: blue;'><u><i>Projects</i></u></h1>
""",
    unsafe_allow_html=True
)
    # st.title("Projects")
    st.write("""
    Here are some of my recent projects:
    """)
    st.markdown("""
    - **Project 1**: A cool web app built with Streamlit  
      [View on GitHub](https://github.com/Luckylakshmisailaja/python-multipage-webapp)  
    - **Project 2**: Machine Learning model for prediction  
      [View on GitHub](https://github.com/Luckylakshmisailaja/demo_streamlit_web)  
    - **Project 3**: Automation script for productivity  
      [View on GitHub](https://github.com/Luckylakshmisailaja/FirstGitDemo)
    """)

# Footer

st.sidebar.markdown("""
<hr>
<p style="text-align: center;">
    © 2024 Lakshmi Sailaja. Powered by <a href="https://streamlit.io">Streamlit</a>.  
    <br>
    <a href="https://github.com/Luckylakshmisailaja">GitHub</a> | 
    <a href="https://www.linkedin.com/feed/">LinkedIn</a>
</p>
""", unsafe_allow_html=True)



