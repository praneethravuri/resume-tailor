# template.py

html_template = (
    """
    <!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Praneeth Ravuri Resume</title>
    <style>
        /* Set up A4 paper dimensions with margins */
        @page {
            size: A4;
        }

        body {
            font-family: Arial, sans-serif;
            line-height: 1;
            color: #000000;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            padding: 20px;
        }

        .header,
        .footer {
            text-align: center;
        }

        .section-title {
            border-bottom: 1px solid #ccc;
            margin-top: 30px;
            margin-bottom: 10px;
            padding-bottom: 5px;
            font-size: 1.3em;
        }

        h1,
        h2,
        h3 {
            margin: 5px 0;
        }

        p {
            margin: 5px 0;
        }

        ul {
            list-style-type: disc;
            margin-left: 20px;
            padding-left: 0;
        }

        li {
            margin-bottom: 5px;
        }

        .sub-section {
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
        }

        .sub-section-right {
            text-align: left;
        }

        .sub-section-left {
            text-align: right;
        }

        a {
            color: #0066cc;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .skills-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .skill-item {
            display: flex;
        }

        .skill-label {
            flex: 0 0 120px;
            /* sets a fixed width for labels */
            font-weight: bold;
        }

        .skill-content {
            flex: 1;
        }
    </style>
</head>

<body>
    <page size="A4">
        <div class="container">

            <!-- Header -->
            <div class="header">
                <h1>Praneeth Ravuri</h1>
                <p>
                    571-622-8648 |
                    <a href="mailto:pravdevrav@gmail.com">pravdevrav@gmail.com</a> |
                    <a href="https://www.praneethravuri.com">praneethravuri.com</a> |
                    <a href="https://www.linkedin.com/in/prav25/">linkedin.com/prav25</a> |
                    <a href="https://www.github.com/praneethravuri">github.com/praneethravuri</a> |
                    Richardson, TX
                </p>
            </div>
                <!-- Resume Content -->
        </div>
    </page>
</body>

</html>
    """
)