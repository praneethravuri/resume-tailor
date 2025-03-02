import json
import os

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def generate_html(resume_data):
    """Generate HTML content from resume JSON data."""
    
    # Create the HTML structure
    html = """<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>{name} Resume</title>
    <style>
        /* Set up A4 paper dimensions with margins */
        @page {{
            size: A4;
        }}

        body {{
            font-family: Arial, sans-serif;
            line-height: 1;
            color: #000000;
            margin: 0;
            padding: 0;
        }}

        .container {{
            max-width: 1000px;
            margin: auto;
            padding: 20px;
        }}

        .header,
        .footer {{
            text-align: center;
        }}

        .section-title {{
            border-bottom: 1px solid #ccc;
            margin-top: 30px;
            margin-bottom: 10px;
            padding-bottom: 5px;
            font-size: 1.3em;
        }}

        h1,
        h2,
        h3 {{
            margin: 5px 0;
        }}

        p {{
            margin: 5px 0;
        }}

        ul {{
            list-style-type: disc;
            margin-left: 20px;
            padding-left: 0;
        }}

        li {{
            margin-bottom: 5px;
        }}

        .sub-section {{
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
        }}

        .sub-section-right {{
            text-align: left;
        }}

        .sub-section-left {{
            text-align: right;
        }}

        a {{
            color: #0066cc;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .skills-container {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .skill-item {{
            display: flex;
        }}
    </style>
</head>

<body>
    <page size="A4">
        <div class="container">
""".format(name=resume_data['personal']['name'])

    # Add header section
    html += """
            <!-- Header -->
            <div class="header">
                <h1>{name}</h1>
                <p>
                    {contact} |
                    <a href="mailto:{email}">{email}</a> |
                    <a href="https://www.{website}">{website}</a> |
                    <a href="https://www.{linkedin}">{linkedin}</a> |
                    <a href="https://www.{github}">{github}</a> |
                    {location}
                </p>
            </div>
""".format(
        name=resume_data['personal']['name'],
        contact=resume_data['personal']['contact'],
        email=resume_data['personal']['email'],
        website=resume_data['personal']['website'],
        linkedin=resume_data['personal']['linkedin'],
        github=resume_data['personal']['github'],
        location=resume_data['personal']['location']
    )

    # Add education section
    html += """
            <div class="section">
                <div class="section-title"><strong>Education</strong></div>
"""

    for edu in resume_data['education']:
        html += """
                <div class="sub-section">
                    <div class="sub-section-right">
                        <h3>{institution}</h3>
                        <p>{degree}</p>
                        <p>{coursework}</p>
                    </div>
                    <div class="sub-section-left">
                        <p>{location}</p>
                        <p>{dates}</p>
                    </div>
                </div>
""".format(
            institution=edu['institution'],
            degree=edu['degree'],
            coursework=edu['coursework'],
            location=edu['location'],
            dates=edu['dates']
        )

    html += """
            </div>
"""

    # Add experience section
    html += """
            <div class="section">
                <div class="section-title"><strong>Experience</strong></div>
"""

    for exp in resume_data['experience']:
        html += """
                <div class="exp-sub-section">
                    <div class="sub-section">
                        <div class="sub-section-right">
                            <h3>{company}</h3>
                            <p>{position}</p>
                        </div>
                        <div class="sub-section-left">
                            <p>{location}</p>
                            <p>{dates}</p>
                        </div>
                    </div>
                    <div class="resume-points">
                        <ul>
""".format(
            company=exp['company'],
            position=exp['position'],
            location=exp['location'],
            dates=exp['dates']
        )

        for point in exp['points']:
            html += """
                            <li>{point}</li>
""".format(point=point)

        html += """
                        </ul>
                    </div>
                </div>
"""

    html += """
            </div>
"""

    # Add skills section
    html += """
            <div class="section">
                <div class="section-title"><strong>Skills</strong></div>
                <div class="skills-container">
"""

    for i, skill in enumerate(resume_data['skills']):
        class_name = "skill-item-1" if i == 0 else "skill-item"
        html += """
                    <div class="{class_name}">
                        <span class="skill-content"><strong>{label}:</strong> {content}</span>
                    </div>
""".format(
            class_name=class_name,
            label=skill['label'],
            content=skill['content']
        )

    html += """
                </div>
            </div>
"""

    # Add projects section
    html += """
            <div class="section">
                <div class="section-title"><strong>Projects</strong></div>
"""

    for project in resume_data['projects']:
        html += """
                <div class="projects-section">
                    <h3>{title}</h3>
                    <ul>
""".format(title=project['title'])

        for point in project['points']:
            html += """
                        <li>{point}</li>
""".format(point=point)

        html += """
                    </ul>
                </div>
"""

    html += """
            </div>
        </div>
    </page>
</body>

</html>
"""

    return html

def write_html(html_content, output_file):
    """Write HTML content to a file."""
    with open(output_file, 'w') as f:
        f.write(html_content)

def json_to_html_converter():
    """Main function to convert JSON resume to HTML."""
    # File paths
    json_file = "enhanced_resume.json"
    output_html = "final_resume.html"
    
    # Check if JSON file exists
    if not os.path.isfile(json_file):
        print(f"Error: {json_file} not found!")
        return
    
    # Load JSON data
    resume_data = load_json(json_file)
    
    # Generate HTML
    html_content = generate_html(resume_data)
    
    # Write HTML to file
    write_html(html_content, output_html)
    
    print(f"Resume successfully converted to HTML: {output_html}")

if __name__ == "__main__":
    json_to_html_converter