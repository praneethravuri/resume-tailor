import json
from pdflatex import PDFLaTeX

# Updated LaTeX template with escaped curly braces for literals
latex_template = r"""
% Praneeth Ravuri Resume
% Converted from HTML to LaTeX - Condensed to fit on one page

\documentclass[10pt,a4paper]{{article}}

% Set custom font size (10.5pt)
\usepackage{{anyfontsize}}
\renewcommand{{\normalsize}}{{\fontsize{{10.75pt}}{{12.6pt}}\selectfont}}

% Packages
\usepackage[margin=0.25in]{{geometry}} % Reduced margins
\usepackage{{enumitem}}
\usepackage{{hyperref}}
\usepackage{{fontawesome}}
\usepackage{{titlesec}}
\usepackage{{color}}
\usepackage{{xcolor}}

\definecolor{{linkcolor}}{{rgb}}{{0,0,1}}
\hypersetup{{
    colorlinks=true,
    urlcolor=linkcolor,
    linkcolor=linkcolor
}}

\setlength{{\parindent}}{{0em}}
\setlength{{\parskip}}{{0.3em}} % Reduced paragraph spacing

% Section title format with reduced spacing
\titleformat{{\section}}
{{\normalfont\large\bfseries}}
{{}}
{{0em}}
{{}}[{{\titlerule}}]

% Reduce spacing before and after section titles
\titlespacing*{{\section}}{{0pt}}{{5pt}}{{3pt}}

% Custom commands for header and sections
\newcommand{{\dateplace}}[2]{{\raggedleft #1 \\ #2 \par}}
\newcommand{{\role}}[2]{{\raggedright \textbf{{#1}} \\ #2 \par}}

% Reduce itemize spacing
\setlist[itemize]{{noitemsep, topsep=0pt, parsep=0pt, partopsep=0pt, leftmargin=*}}

\begin{{document}}

% Header
\begin{{center}}
    \textbf{{\Large {name}}}\\
    \vspace{{0.2em}}
    {contact} $|$
    \href{{mailto:{email}}}{{ {email} }} $|$
    \href{{{website_url}}}{{{website}}} $|$
    \href{{https://www.linkedin.com/{linkedin}}}{{linkedin.com/{linkedin}}} $|$
    \href{{https://www.github.com/{github}}}{{github.com/{github}}} $|$
    {location}
\end{{center}}
\vspace{{-0.3em}}

% Education Section
\section*{{Education}}
\vspace{{0.5em}}
{education_section}

% Experience Section
\section*{{Experience}}
\vspace{{0.5em}}
{experience_section}

% Skills Section
\section*{{Skills}}
\vspace{{0.5em}}
{skills_section}

% Projects Section
\section*{{Projects}}
\vspace{{0.5em}}
{projects_section}

\end{{document}}
"""

def generate_education_section(education_list):
    sections = []
    for edu in education_list:
        # Use two minipages for each education entry
        edu_entry = r"""
\begin{{minipage}}[t]{{0.70\textwidth}}
    \role{{{institution}}}{{{degree}\\{coursework}}}
\end{{minipage}}
\begin{{minipage}}[t]{{0.29\textwidth}}
    \dateplace{{{location}}}{{{dates}}}
\end{{minipage}}
\vspace{{0.5em}}
""".format(
            institution=edu.get('institution', ''),
            degree=edu.get('degree', ''),
            coursework=edu.get('coursework', ''),
            location=edu.get('location', ''),
            dates=edu.get('dates', '').replace("&ndash;", "--")
        )
        sections.append(edu_entry)
    return "\n".join(sections)

def generate_experience_section(experience_list):
    sections = []
    for exp in experience_list:
        exp_entry = r"""
\begin{{minipage}}[t]{{0.70\textwidth}}
    \role{{{company}}}{{{position}}}
\end{{minipage}}
\begin{{minipage}}[t]{{0.29\textwidth}}
    \dateplace{{{location}}}{{{dates}}}
\end{{minipage}}
\vspace{{0em}}
\begin{{itemize}}
""".format(
            company=exp.get('company', ''),
            position=exp.get('position', ''),
            location=exp.get('location', ''),
            dates=exp.get('dates', '').replace("&ndash;", "--")
        )
        # Add each bullet point
        for point in exp.get('points', []):
            safe_point = point.replace("%", "\\%")
            exp_entry += "\n    \\item " + safe_point
        exp_entry += r"""
\end{itemize}
\vspace{0.5em}
"""
        sections.append(exp_entry)
    return "\n".join(sections)

def generate_skills_section(skills_list):
    skills_block = r"\begin{{itemize}}"
    for skill in skills_list:
        safe_content = skill.get('content', '').replace("%", "\\%")
        skills_block += "\n    \\item \\textbf{{{label}:}} {content}".format(
            label=skill.get('label', ''), content=safe_content
        )
    skills_block += "\n\\end{itemize}"
    return skills_block

def generate_projects_section(projects_list):
    sections = []
    for proj in projects_list:
        proj_entry = r"\textbf{{{title}}}".format(title=proj.get('title', ''))
        proj_entry += "\n\\vspace{{0.5em}}\n\\begin{{itemize}}"
        for point in proj.get('points', []):
            safe_point = point.replace("%", "\\%")
            proj_entry += "\n    \\item " + safe_point
        proj_entry += "\n\\end{itemize}\n\\vspace{{0.5em}}"
        sections.append(proj_entry)
    return "\n".join(sections)

def create_latex_resume(enhanced_resume):
    personal = enhanced_resume.get('personal', {})
    education_section = generate_education_section(enhanced_resume.get('education', []))
    experience_section = generate_experience_section(enhanced_resume.get('experience', []))
    skills_section = generate_skills_section(enhanced_resume.get('skills', []))
    projects_section = generate_projects_section(enhanced_resume.get('projects', []))
    
    website_url = personal.get('website', '')
    if not website_url.startswith("http"):
        website_url = "https://" + website_url
    
    filled_template = latex_template.format(
        name=personal.get('name', ''),
        contact=personal.get('contact', ''),
        email=personal.get('email', ''),
        website=personal.get('website', ''),
        website_url=website_url,
        linkedin=personal.get('linkedin', ''),
        github=personal.get('github', ''),
        location=personal.get('location', ''),
        education_section=education_section,
        experience_section=experience_section,
        skills_section=skills_section,
        projects_section=projects_section
    )
    return filled_template

def json_to_pdf_converter():
    try:
        with open("enhanced_resume.json", "r") as f:
            enhanced_resume = json.load(f)
    except Exception as e:
        print("Error loading enhanced_resume.json:", e)
        exit(1)
    
    latex_resume = create_latex_resume(enhanced_resume)
    
    with open("resume.tex", "w") as f:
        f.write(latex_resume)
    
    print("LaTeX resume generated as 'resume.tex'")
    
    pdfl = PDFLaTeX.from_texfile("resume.tex")
    pdf, log, completed = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
    if completed:
        print("PDF generated successfully as 'resume.pdf'")
    else:
        print("PDF generation failed.")

if __name__ == "__main__":
    json_to_pdf_converter()
