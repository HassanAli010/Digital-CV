from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hassan Ali"
PAGE_ICON = ":wave:"
NAME = "Hassan Ali"
DESCRIPTION = """
ReactJS Frontend Website Developer | MongoDB | MySQL | NodeJS.
"""
EMAIL = "hassan7538216@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/hassan-ali-2ab7aa269/",
    "GitHub": "https://github.com/HassanAli010",
    "Twitter": "https://twitter.com/Hassan_Web_Dev",
}
PROJECTS = {
    "🏆 Personal Portfolio Website": "",
    "🏆 Advanced Todo List App": "",
    "🏆 Course Recommendation System": "",
    "🏆 Live Crypto Coin Tracker": "",
    "🏆 Movie Recommendation System": "",
    "🏆 Professional E-commerce Website": "",
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    """
- ✔️ Hazara University Mansehra | 2024 | Bachelor In Computer Science
- ✔️ Jinnah Colleges Mansehra | 2020 | Pre-Engineering
- ✔️ Orient Public School | 2018 | Science-Core

"""
)

# --- EXPERIENCE---
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ 2 years of frontend development with HTML, CSS, and JavaScript, focusing on ReactJS
- ✔️ Strong hands-on experience with ReactJS
- ✔️ Expertise in using WordPress for dynamic, responsive web solutions
- ✔️ Excellent team player with strong initiative
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, NumPy).
- 📊 Data Visualization: MS Excel.
- 📚 Modeling: KNN MODEL (Brute Algorithm).
- 🗄️ Databases: MongoDB, MySQL
- 🌐 Front-End Development: HTML, CSS, JavaScript, React.JS
- 🖥️ Back-End Development: Node.js
- 🎨 Web Designing: Figma
- 🗃️ Version Control: Git, GitHub
- 🌍 Web APIs: RESTful APIs
- 🚀 Web Performance: Optimization, Caching, CDNs
- 📦 Package Managers/ Bundler: NPM, Vite
- 🏢 Hosting and Deployment: Netlify, Vercel
- 💅 Styling: SASS/SCSS, Tailwind CSS, GSAP
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
# st.write("🚧", "****")
# st.write("02/2020 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# --- JOB 2
st.write('\n')
st.write("🚧", "**FYP Project Management**")
st.write("02/2024 - 07/2024")
st.write(
    """
- ► Built CRS where user preference based recommend the courses 
- ► Modeled targets likely user past history and real time history updation
- ► Basic and Enhanced content based filtering technique used in project 
"""
)

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
