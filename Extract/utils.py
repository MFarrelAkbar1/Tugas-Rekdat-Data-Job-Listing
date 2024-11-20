import re
import csv

def checkTitleLevel(title: str):
    if "Junior" in title or "Jr." in title or "Jr" in title or "Interns" in title or "Intern" in title or "Trainee" in title:
        return 1
    elif "Mid" in title:
        return 2
    elif "Senior" in title or "Manager" in title or "Sr." in title or "Sr" in title :  # Corrected condition
        return 3
    elif "Executive" in title or "Head" in title or "Principal" in title:  # Corrected condition
        return 4
    else:
        return 2  # Optional: handle cases where no title level is found


def contains_remote(descriptions):
    # Regular expression to check if the word 'remote' exists in any description (case-insensitive)
    pattern = r'\bremote\b'

    # Check each description for the word 'remote'
    for description in descriptions:
        if re.search(pattern, description, re.IGNORECASE):  # re.IGNORECASE makes it case-insensitive
            return True  # Return True if 'remote' is found in any description

    return False  # Return False if no description contains 'remote'


def check_job_type(descriptions):
    # Regular expression to check if 'full time' or 'part time' exists in any description (case-insensitive)
    pattern = r'\b(full\s?time|part\s?time)\b'

    # Check each description for 'part time'
    for description in descriptions:
        if re.search(r'\bpart\s?time\b', description, re.IGNORECASE):  # Looking specifically for 'part time'
            return "part time"  # Return 'part time' if found

    # If no 'part time' is found, return 'full time' by default
    return "full time"

def CheckForSkill(descriptions: list):
    skills = []
    searchable_skills = [
        'Python', 'JavaScript', 'JS', 'TypeScript', 'Java', 'Kotlin', 'Swift', 'C', 'C++', 'C#',
        'Go', 'Golang', 'Rust', 'Ruby', 'PHP', 'Perl', 'HTML', 'CSS', 'SCSS', 'Sass', 'Less',
        'SQL', 'NoSQL', 'GraphQL', 'PL/SQL', 'T-SQL', 'MySQL', 'PostgreSQL', 'MongoDB', 'Redis',
        'SQLite', 'Cassandra', 'Elasticsearch', 'Firebase', 'DynamoDB', 'MariaDB', 'Oracle DB',

        # Web Development Frameworks and Libraries
        'React', 'Angular', 'Vue', 'Svelte', 'Next.js', 'Nuxt.js', 'Gatsby', 'Django', 'Flask',
        'Spring Boot', 'Express.js', 'Laravel', 'Symfony', 'CakePHP', 'ASP.NET', 'Rails', 'Ruby on Rails',

        # Mobile Development
        'Android Development', 'iOS Development', 'Flutter', 'React Native', 'Xamarin',
        'SwiftUI', 'Objective-C', 'Ionic', 'Kivy',

        # DevOps and Cloud
        'AWS', 'Azure', 'Google Cloud', 'GCP', 'Firebase', 'Heroku', 'Terraform', 'Ansible',
        'Puppet', 'Chef', 'Docker', 'Kubernetes', 'OpenShift', 'Helm', 'Jenkins', 'CircleCI',
        'GitLab CI/CD', 'Travis CI', 'CI/CD', 'Vagrant', 'Spinnaker', 'CloudFormation',

        # Machine Learning and Data Science
        'Machine Learning', 'Data Science', 'Deep Learning', 'NLP', 'TensorFlow', 'PyTorch',
        'Keras', 'Scikit-learn', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Statsmodels',
        'OpenCV', 'XGBoost', 'LightGBM', 'CatBoost', 'Hugging Face Transformers',

        # Big Data and Analytics
        'Hadoop', 'Spark', 'Kafka', 'Hive', 'Pig', 'Snowflake', 'BigQuery', 'Presto', 'Redshift',
        'Airflow', 'ETL Pipelines', 'Data Engineering', 'Tableau', 'Power BI',

        # Software Development Tools
        'Git', 'SVN', 'Mercurial', 'Bitbucket', 'GitHub', 'GitLab', 'JIRA', 'Confluence',
        'Trello', 'Asana', 'Slack', 'VS Code', 'IntelliJ IDEA', 'PyCharm', 'Eclipse', 'NetBeans',

        # Networking and Security
        'Networking', 'Cybersecurity', 'Firewalls', 'Wireshark', 'SSL/TLS', 'OAuth', 'OpenID',
        'Zero Trust', 'IAM', 'Authentication', 'Authorization', 'Penetration Testing',
        'Vulnerability Scanning', 'Nmap', 'Burp Suite',

        # Operating Systems and Virtualization
        'Linux', 'Unix', 'Windows', 'MacOS', 'Bash', 'Zsh', 'PowerShell', 'VMware', 'VirtualBox',
        'Hyper-V', 'KVM', 'Docker Swarm', 'LXC/LXD',

        # Programming Paradigms
        'OOP', 'Functional Programming', 'Reactive Programming', 'Concurrent Programming',
        'Multithreading', 'Event-driven Programming', 'Microservices Architecture',
        'Serverless Architecture',

        # Testing and QA
        'JUnit', 'TestNG', 'Mocha', 'Jest', 'Enzyme', 'Cypress', 'Selenium', 'Appium',
        'Postman', 'SoapUI', 'LoadRunner', 'JMeter', 'Pytest', 'Robot Framework', 'Karma',

        # Other Tools and Concepts
        'REST API', 'SOAP API', 'gRPC', 'GraphQL API', 'WebSockets', 'Webpack', 'Parcel',
        'Babel', 'ESLint', 'Prettier', 'JWT', 'Web3', 'Blockchain', 'Smart Contracts',
        'Solidity', 'Rust for Blockchain', 'Ethereum', 'Hyperledger', 'IoT', 'AR/VR', 'Game Development',
        'Unity', 'Unreal Engine', 'Godot', 'CryEngine', '3D Modeling', 'Blender', 'Maya', 'AutoCAD',

        # Emerging Technologies
        'Quantum Computing', 'AI Ethics', 'Edge Computing', '5G', 'Digital Twins', 'Metaverse',
        'Robotics', 'Autonomous Systems', '3D Printing', 'Bioinformatics', 'Wearable Tech'
    ]

    # Iterate over each description in the list
    for desc in descriptions:
        # Loop through each skill in searchable_skills
        for skill in searchable_skills:
            # Use regex to search for the skill as a whole word, case-insensitive
            if re.search(rf'\b{skill}\b', desc, re.IGNORECASE):
                if skill not in skills:  # Optional: avoid duplicates
                    skills.append(skill)

    return skills


def CheckForSkillString(description: str):
    skills = []
    searchable_skills = [
        'Python', 'JavaScript', 'JS', 'TypeScript', 'Java', 'Kotlin', 'Swift', 'C', 'C++', 'C#',
        'Go', 'Golang', 'Rust', 'Ruby', 'PHP', 'Perl', 'HTML', 'CSS', 'SCSS', 'Sass', 'Less',
        'SQL', 'NoSQL', 'GraphQL', 'PL/SQL', 'T-SQL', 'MySQL', 'PostgreSQL', 'MongoDB', 'Redis',
        'SQLite', 'Cassandra', 'Elasticsearch', 'Firebase', 'DynamoDB', 'MariaDB', 'Oracle DB',

        # Web Development Frameworks and Libraries
        'React', 'Angular', 'Vue', 'Svelte', 'Next.js', 'Nuxt.js', 'Gatsby', 'Django', 'Flask',
        'Spring Boot', 'Express.js', 'Laravel', 'Symfony', 'CakePHP', 'ASP.NET', 'Rails', 'Ruby on Rails',

        # Mobile Development
        'Android Development', 'iOS Development', 'Flutter', 'React Native', 'Xamarin',
        'SwiftUI', 'Objective-C', 'Ionic', 'Kivy',

        # DevOps and Cloud
        'AWS', 'Azure', 'Google Cloud', 'GCP', 'Firebase', 'Heroku', 'Terraform', 'Ansible',
        'Puppet', 'Chef', 'Docker', 'Kubernetes', 'OpenShift', 'Helm', 'Jenkins', 'CircleCI',
        'GitLab CI/CD', 'Travis CI', 'CI/CD', 'Vagrant', 'Spinnaker', 'CloudFormation',

        # Machine Learning and Data Science
        'Machine Learning', 'Data Science', 'Deep Learning', 'NLP', 'TensorFlow', 'PyTorch',
        'Keras', 'Scikit-learn', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Statsmodels',
        'OpenCV', 'XGBoost', 'LightGBM', 'CatBoost', 'Hugging Face Transformers',

        # Big Data and Analytics
        'Hadoop', 'Spark', 'Kafka', 'Hive', 'Pig', 'Snowflake', 'BigQuery', 'Presto', 'Redshift',
        'Airflow', 'ETL Pipelines', 'Data Engineering', 'Tableau', 'Power BI',

        # Software Development Tools
        'Git', 'SVN', 'Mercurial', 'Bitbucket', 'GitHub', 'GitLab', 'JIRA', 'Confluence',
        'Trello', 'Asana', 'Slack', 'VS Code', 'IntelliJ IDEA', 'PyCharm', 'Eclipse', 'NetBeans',

        # Networking and Security
        'Networking', 'Cybersecurity', 'Firewalls', 'Wireshark', 'SSL/TLS', 'OAuth', 'OpenID',
        'Zero Trust', 'IAM', 'Authentication', 'Authorization', 'Penetration Testing',
        'Vulnerability Scanning', 'Nmap', 'Burp Suite',

        # Operating Systems and Virtualization
        'Linux', 'Unix', 'Windows', 'MacOS', 'Bash', 'Zsh', 'PowerShell', 'VMware', 'VirtualBox',
        'Hyper-V', 'KVM', 'Docker Swarm', 'LXC/LXD',

        # Programming Paradigms
        'OOP', 'Functional Programming', 'Reactive Programming', 'Concurrent Programming',
        'Multithreading', 'Event-driven Programming', 'Microservices Architecture',
        'Serverless Architecture',

        # Testing and QA
        'JUnit', 'TestNG', 'Mocha', 'Jest', 'Enzyme', 'Cypress', 'Selenium', 'Appium',
        'Postman', 'SoapUI', 'LoadRunner', 'JMeter', 'Pytest', 'Robot Framework', 'Karma',

        # Other Tools and Concepts
        'REST API', 'SOAP API', 'gRPC', 'GraphQL API', 'WebSockets', 'Webpack', 'Parcel',
        'Babel', 'ESLint', 'Prettier', 'JWT', 'Web3', 'Blockchain', 'Smart Contracts',
        'Solidity', 'Rust for Blockchain', 'Ethereum', 'Hyperledger', 'IoT', 'AR/VR', 'Game Development',
        'Unity', 'Unreal Engine', 'Godot', 'CryEngine', '3D Modeling', 'Blender', 'Maya', 'AutoCAD',

        # Emerging Technologies
        'Quantum Computing', 'AI Ethics', 'Edge Computing', '5G', 'Digital Twins', 'Metaverse',
        'Robotics', 'Autonomous Systems', '3D Printing', 'Bioinformatics', 'Wearable Tech'
    ]

    # Iterate over each skill in searchable_skills and check if it appears in the description
    for skill in searchable_skills:
        # Use regex to search for the skill as a whole word, case-insensitive
        if re.search(rf'\b{skill}\b', description, re.IGNORECASE):
            if skill not in skills:  # Optional: avoid duplicates
                skills.append(skill)

    return skills

def save_jobs_to_csv(job_listing, filename='jobs_listing_adzun.csv'):
    """Save the job listings to a CSV file."""
    if not job_listing:
        print("No job listings to save.")
        return

    jobs_dict = [job.__dict__ for job in job_listing]
    fieldnames = jobs_dict[0].keys()

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header (column names)
        writer.writerows(jobs_dict)  # Write each job as a row in the CSV file

    print(f"Data saved to {filename}")