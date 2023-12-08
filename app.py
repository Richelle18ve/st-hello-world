import streamlit as st

# Set page configuration
st.set_page_config(page_title="Richelle's Blog", page_icon=":heart:", layout="wide")

# GREETINGS AND ABOUT ME
with st.container():
    st.title("Welcome to Richelle's Blog! :wave:")
    st.subheader("ABOUT ME")
    st.write(
        "I'm Richelle J. Maravillas, 18 years old and a first-year college student at SNSU. "
        "I chose this computer engineering course because I enjoy the challenge of finding answers to difficult issues. "
        "People are completely engrossed in technology, as it permeates every part of everyday life and influences communication, work, and leisure in different ways. "
    )
    st.write(
        "If you're interested in learning more about me "
        "[message me on Gmail >](mailto:rmaravillas1@ssct.edu.ph)\n "
        "or visit my [LinkedIn Profile >](https://www.linkedin.com/in/richelle-maravillas/). "
    )
    st.write("If you seek an understanding of the significance and advantages of programming, I would be pleased to provide assistance and information on the subject. ")

# WHAT IS PROGRAMMING
with st.container():
    st.write("---")
    st.header("What is Programming?")
    st.write(
        "Programming refers to a technological process for telling a computer which tasks to perform in order to solve problems. "
        "You can think of programming as a collaboration between humans and computers, "
        "in which humans create instructions for a computer to follow (code) in a language computers can understand. "
        "[Learn more](https://www.coursera.org/articles/what-is-programming) "
    )

# BENEFITS OF PROGRAMMING
with st.container():
    st.write("---")
    st.header("Benefits of Programming")
    st.write(
        "Programming offers a wide range of benefits that extend beyond just writing code. Some of the key advantages include:"
    )
    st.write(
        """
        - *Problem Solving:* Develop critical thinking and problem-solving skills.
        - *Automation:* Automate repetitive tasks to save time and effort.
        - *Creativity:* Express creativity by building unique and innovative solutions.
        - *Career Opportunities:* Open up a wide range of career opportunities in tech.
        - *Continuous Learning:* Constantly learn and adapt to new technologies and languages.
        """
    )
    st.write(
        f"For more insights, you can check out this [article on **Why Programming is Important**](https://codedamn.com/news/programming/why-is-programming-important-2)."
    )

# WHAT BROADENS MY KNOWLEDGE OF PROGRAMMING
with st.container():
    st.write("---")
    st.header("What Broadens My Knowledge of Programming:")
    st.write(
        "W3Schools is a valuable resource that enables students to study web development and computer languages at their own pace. "
        "It provides comprehensive documentation, interactive coding exercises, and clear and short lectures. "
    )
    st.write(
        """
        - *Free and Accessible Resources:* Leveraging free tutorials and resources from the platform.
        - *Versatile Learning Paths:* Exploring different routes designed for both beginners and experienced learners.
        - *Structured Practice:* Engaging in exercises and quizzes that reinforce learning through hands-on practice.
        - *Clear Documentation:* Referring to clear and concise documentation for quick comprehension of concepts.
        - *Efficient Learning:* Utilizing resources that facilitate efficient learning with a structured approach. \n
        To know more, visit this link: [**W3Schools**](https://www.w3schools.com/).
        """
    )