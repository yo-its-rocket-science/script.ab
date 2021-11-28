import re
import pandas as pd
import spacy
import numpy as np
import spacy
#Run this first to download the language model
#python -m spacy download en_core_web_lg
nlp = spacy.load('en_core_web_lg')
import nmslib
search_index = nmslib.init(method='hnsw', space='cosinesimil')

def course_idnum_split(txt):
    txt = str(txt)
    if len(txt)>1:
        return ' '.join([x for x in re.split('(\d+)', txt) if len(x)>1])
    else:
        return txt

def course_description_clean(txt):
    txt = str(txt)
    pattern='Course Hours:'
    if len(txt)>1 and pattern in txt:
        txtlist = txt.split(pattern)
        return txtlist[0]
    else:
        return txt
    
    
def get_vec_str(txt):
    doc = nlp(txt)
    return doc.vector


def query_skill(txt, orig_index, num_results=2):
    txt_vec = get_vec_str(txt)
    q_index, q_sim = search_index.knnQuery(txt_vec, k=num_results)
    orig_index_vals = [orig_index[i] for i in q_index.tolist()]
    output = pd.DataFrame({'index':q_index.tolist(), 
                           'similarity':q_sim.tolist(),
                           'skill_value':orig_index_vals,
                           'input_value':txt}).sort_values(by='similarity', ascending=False)
    return output


def course_skill_multiplier(course_level):
    course_multiplier = course_level*0.1333+0.5333
    return course_multiplier

def transcript_to_skills(proc_transcript_csv, skills_csv, course_csv):
    df_skill = pd.read_csv(skills_csv)
    df_course = pd.read_csv(course_csv, header=None).iloc[:,1:6]
    df_course.columns = ['Course_Num','Course_IDNum','Course_Description','Course_Department','Course_Level']
    
    df_transcript = pd.read_csv(proc_transcript_csv)
    df_transcript['Course_IDNum'] = df_transcript['Course_ID'].astype(str)+' '+df_transcript['Course_Num'].astype(str)
    
    df_course['Course_IDNum'] = df_course['Course_IDNum'].apply(course_idnum_split)
    df_course['Course_Description'] = df_course['Course_Description'].apply(course_description_clean)
    
    df_student = df_transcript.merge(df_course.drop(columns=['Course_Num']), how='left', on='Course_IDNum')
    
    all_skills = df_skill['Skill Keyword'].tolist()
    
    
    skill_vectors = [get_vec_str(x) for x in all_skills]
    search_index.addDataPointBatch(np.array(skill_vectors))
    search_index.createIndex({'post': 2}, print_progress=True)
        
    df_student_skills = pd.DataFrame()
    for i in range(0, len(df_student)):
        query_desc_df = query_skill(txt=df_student['Course_Description'][i], 
                                    orig_index=all_skills, num_results=3)
        query_dept_df = query_skill(txt=df_student['Course_Department'][i], 
                                    orig_index=all_skills, num_results=3)
        df_student_skills =  pd.concat([df_student_skills, query_desc_df, query_dept_df], axis=0)
    
    df_student_skills =  df_student_skills.sort_values(by='similarity', ascending=False).drop_duplicates(subset='skill_value')
    df_student_skills2 = df_student_skills[df_student_skills['similarity']>=0.01].rename(columns={'similarity':'Estimated_ability', 'skill_value':'Skill', 'input_value':'Relevant_Coursework'})
    df_student_skills2 = df_student_skills2.merge(df_student[['Course_Description', 'Course_Level']], how='left', left_on='Relevant_Coursework', right_on='Course_Description')
    df_student_skills2['Course_Level'] = df_student_skills2['Course_Level'].fillna(0)
    df_student_skills2['Model_Estimated_ability'] = df_student_skills2['Estimated_ability'] * df_student_skills2['Course_Level'].apply(course_skill_multiplier)
    df_student_final = df_student_skills2[['Skill', 'Relevant_Coursework', 'Model_Estimated_ability']].sort_values(by='Model_Estimated_ability', ascending=False).reset_index(drop=True)
    
    return df_student_final


##example usage
#from NLP_model_skills import *
#student_skills = transcript_to_skills(proc_transcript_csv='processed_transcript.csv', 
#                     skills_csv='skills_v2.csv', 
#                     course_csv='numbered_scrapeUC.csv')
#student_skills.to_csv('model_student_skills.csv', index=False)
