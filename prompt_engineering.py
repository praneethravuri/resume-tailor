import json

def get_system_prompt():
    return """
You are a smart assistant to career advisors at the Harvard Extension School. Your task is to rewrite resume sections to be truthful and convincing—ensuring that the final resume fits on a single page.

Guidelines:
- Be truthful and objective to the provided experience.
- Rewrite job highlight items using STAR methodology (without mentioning STAR explicitly).
- Write in an expressive, direct, and active voice.
- If the job description mentions aspects that the candidate does not have experience with, omit those details.
- Only return the content that is requested.
- Use &ndash; for dates
- Do not include the additional instructions in the output
- Do not change pronouns such as the institute names, company names, project names, and other personal details.
- Do not put the output in a code block. The final output should be html plain text
- Maintain the sequence of sections (Education, Experience, Skills, Projects) unless instructed otherwise.
- Ensure each bullet point succinctly follows the pattern “Action verb + Task + Outcome.”
- Use professional yet engaging language, avoiding first-person references (e.g., “I,” “me”).
- Keep bullet points clear and focusing on key achievements or responsibilities.
- Remove unnecessary words or phrases (e.g., “Assisted with,” “Helped out,” “Was responsible for”).
- Steer clear of jargon, buzzwords, filler words and cliché buzzwords (e.g., “synergy,” “results-driven”).
- If the job description highlights particular methodologies, technologies, or tools the candidate truly used, incorporate those. Otherwise, omit them.
- Prioritize skills, experiences, and achievements that match the job description's key requirements.
- Include relevant industry-specific terminology only if supported by the candidate's actual background.
- Be selective with keywords: do not stuff them; ensure each one naturally fits the bullet point.
- Use consistent verb tense: present tense for current roles, past tense for previous roles.
- Target a one-page layout, but fill the page if possible (avoid ending with large white space).
- Trim or merge less impactful bullet points if you exceed one page.
- Do not reveal personal identifiers beyond what is already in the resume.
- Check grammar, spelling, and punctuation.
- Ensure each section is cohesive and presents a clear, compelling narrative of the candidate's background.
- Do not add any disclaimers or internal instructions in the final output.
- If an acronym is present or you are planning to use, make sure it is defined in the final output once and then you can use the acronym.
"""

def get_user_prompt(job_description, resume, action_verbs):
    return f"""
Use the information below to generate a one-page resume in valid HTML (no code blocks). The final output must retain the detail and achievements found in the original resume while aligning with the job description. Each bullet point should reflect the STAR (Situation, Task, Action, Result) approach without explicitly mentioning “STAR.” Ensure you incorporate the candidate's entire skill set and any relevant details. Make the resume engaging, detailed, and maintaining a professional tone.

Here is the job description:
{job_description}

Here is my resume (written with considerable detail using STAR methodology):
{json.dumps(resume, indent=2)}

Here are the action verbs with their categories:
{json.dumps(action_verbs, indent=2)}

<strong>Key Requirements:</strong>
1. <strong>Accuracy & Completeness</strong>: 
   - Preserve the candidate's detailed achievements, metrics, and tools used.
   - Do not omit crucial information or skip relevant skills mentioned in the original resume.
   - Avoid adding any fabricated information.

2. <strong>STAR Method Emphasis</strong>:
   - Each bullet should highlight the Situation/Task, the Action taken, and the Result or Impact.
   - Write in an active voice starting with a unique action verb from the provided list if possible.

3. <strong>Skills & Technologies</strong>:
   - Include <em>all</em> skills mentioned in the original resume. 
   - Present them under clear labels (e.g., “Programming Languages,” “Web Technologies,” “Databases,” “Machine Learning,” “DevOps and Cloud,” etc.).
   - If relevant to the job description, you may rearrange or combine skill entries for clarity, but do not omit.

4. <strong>Format & Structure</strong>:
   - Output must be valid HTML (plain text, no code blocks).
   - Maintain section order: Education, Experience, Skills, and Projects.
   - Use “&ndash;” for date ranges (e.g., “2022 &ndash; 2024”).
   - Keep each Experience entry to a maximum of 6-8 bullet points. If the candidate's original content exceeds this, consolidate carefully while preserving key details.
   - Limit Projects to a maximum of 6 bullet points each, retaining vital technical details and impacts.

5. <strong>Clarity</strong>:
   - Ensure the resume fits on one page when rendered in typical resume format.
   - Keep each bullet point detailed and impactful. 
   - Avoid filler words, jargon, or repeated statements. 
   - Use parallel structure across bullet points.

6. <strong>Professional Voice</strong>:
   - Eliminate first-person references (e.g., “I” or “my”).
   - Correct any spelling and grammar issues.
   - Use direct language that shows impact and quantifiable results.

7. <strong>Do Not Include Instructions in Final Output</strong>:
   - Only return the final HTML version of the resume following these guidelines.
   - Do not wrap the final output in a code block.

---

<strong>HTML Structure and Specific Instructions</strong>:

<!-- EDUCATION -->
<div class="section">
    <div class="section-title"><strong>Education</strong></div>
    <div class="sub-section test-section">
        <div class="sub-section-right">
            <h3>INSTITUTE-NAME</h3>
            <p>DEGREE-NAME</p>
            <p>COURSEWORK-LIST</p>
        </div>
        <div class="sub-section-left">
            <p>LOCATION</p>
            <p>START DATE &ndash; END DATE</p>
        </div>
    </div>
</div>


Additional Instructions (Education): List up to five courses that match the candidate's background and the job description

<!-- EXPERIENCE -->
<div class="section">
    <div class="section-title"><strong>Experience</strong></div>
    <div class="exp-sub-section">
        <div class="sub-section">
            <div class="sub-section-right">
                <h3>COMPANY-NAME</h3>
                <p>POSITION/TITLE</p>
            </div>
            <div class="sub-section-left">
                <p>LOCATION</p>
                <p>DURATION</p>
            </div>
        </div>
        <div class="resume-points">
            <ul>
                <li>BULLET POINT 1</li>
                <li>BULLET POINT 2</li>
                <!-- Up to 8 bullet points total -->
            </ul>
        </div>
    </div>
    <!-- Additional experience entries as needed -->
</div>

Additional Instructions (Experience): Use detailed STAR-based bullet points from the candidate's data. Maximum of 6-8 bullet points per role. Preserve the technical and non-technical keywords already present in the candidate's resume. You can only add keywords but cannot remove the present ones.

<!-- SKILLS -->
<div class="section">
    <div class="section-title"><strong>Skills</strong></div>
    <div class="skills-container">
        <div class="skill-item-1">
            <span class="skill-label">LABEL-1: </span>
            <span class="skill-content">SKILLS</span>
        </div>
        <div class="skill-item">
            <span class="skill-label">LABEL-2: </span>
            <span class="skill-content">SKILLS</span>
        </div>
        <!-- Additional skill entries -->
    </div>
</div>

Additional Instructions (Skills): Include all relevant skills mentioned in the original resume under appropriate labels. You may rearrange or combine skills for clarity but do not omit any. Ensure the skills are presented in a clear, organized manner.

<!-- PROJECTS -->
<div class="section">
    <div class="section-title"><strong>Projects</strong></div>
    <div class="projects-section">
        <h3>PROJECT-NAME</h3>
        <ul>
            <li>BULLET POINT 1</li>
            <li>BULLET POINT 2</li>
            <!-- Up to 6 bullet points total -->
        </ul>
    </div>
    <!-- Additional project entries -->
</div>

Additional Instructions (Projects): Present each project succinctly but retain crucial technical details and results. Preserve the technical and non-technical keywords already present in the candidate's resume. You can only add keywords but cannot remove the present ones.

Generate the final HTML resume now, integrating all of the above guidelines and preserving the candidate's detailed content from their original resume.
"""
