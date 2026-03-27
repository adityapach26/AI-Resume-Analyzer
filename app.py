from pypdf import PdfReader

#####
import streamlit as st
st.title("AI RESUME SELECTOR",text_alignment="justify")
st.header("Upload your file here ",text_alignment="left")
uploaded_file =st.file_uploader("upload your pdf here",type="pdf")

skills_db = [
    "python",
    "c",
    "c++",
    "java",
    "machine learning",
    "data analysis",
    "sql",
    "html",
    "css",
    "javascript",
    "deep learning",
    "nlp"
]


synonyms = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "db": "database",
    "js": "javascript",
    "py": "python",
    "cpp": "c++",
    "c plus plus": "c++",
    "datasci": "data science",
    "data analytics": "data analysis"
}


def text_extract_skills(text):

    #lower
    text_lowecase=text.lower()

    
    #removing puncuations
    text_split=text_lowecase.split() 
    new_text=text_split
    i=0 
    for a in text_split:  
        
        new_text[i]=a.strip(",.;")
            
        i=i+1

    #synonyms
    b=len(new_text)
    for j in range(0,b):
        if new_text[j] in synonyms:
            new_text[j]=synonyms[new_text[j]]

    synonyms_prone_text=" ".join(new_text)

            

    #identifing skills
    required_text=set()
    m=len(skills_db)

    for a in range(0,m):
        if " " not in skills_db[a]:
            if skills_db[a] in new_text:
                required_text.add(skills_db[a])
        elif " " in skills_db[a]:
            if skills_db[a] in synonyms_prone_text:
                required_text.add(skills_db[a])

    return required_text

def set_printer(set1):
    for element in set1:
        st.write(element,end=",")
        

def main(input_required_skills):
    #resume skills
    resume_skills=text_extract_skills(resume_text)
    #job skills
    job_skills=text_extract_skills(input_required_skills)


    #percentage 

    common=resume_skills&job_skills
    difference=job_skills-resume_skills
    if len(job_skills)!=0:
        percentage=(len(common)/len(job_skills))*100
        st.header("MATCH")
        st.write("Resume is of ",percentage,"% match")
        st.header("USEFULL SKILLS")
        st.write("The useful found skills are:-  ", ", ".join(common))
        st.header("MISSING SKILLS")
        st.write("The missing skills are:-   ", ", ".join(difference))
    else:
        print("error ")

######

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    resume_text=full_text.strip()

    input_required_skills=st.text_area("Enter the job skills us want")
    if input_required_skills is not None:
        main(input_required_skills)


