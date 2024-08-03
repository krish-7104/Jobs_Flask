CREATE TABLE jobs(
	id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(250) NOT NULL,
    location VARCHAR(255) NOT NULL,
    salary INT,
    currency VARCHAR(10),
    responsibilities VARCHAR(2000),
    requirements VARCHAR(2000),
    PRIMARY KEY (id)
);

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
VALUES 
('Software Engineer', 'Bangalore, Karnataka', 1200000, 'Rs', 'Develop and maintain software applications; Collaborate with cross-functional teams; Participate in code reviews.', 'Bachelor\'s degree in Computer Science; 3+ years of experience in software development; Proficiency in Java and Python.');

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
VALUES 
('Data Scientist', 'Hyderabad, Telangana', 1400000, 'Rs', 'Analyze and interpret complex data sets; Develop machine learning models; Communicate findings to stakeholders.', 'Master\'s degree in Data Science or related field; 2+ years of experience in data analysis; Strong knowledge of SQL and Python.');

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
VALUES 
('Project Manager', 'Remote', 900000, 'Rs', 'Manage project timelines and deliverables; Coordinate with team members and clients; Ensure project goals are met.', 'Bachelor\'s degree in Business or related field; 5+ years of project management experience; Strong organizational and communication skills.');

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
VALUES 
('UX Designer', 'Pune, Maharashtra', 1100000, 'Rs', 'Design and prototype user interfaces; Conduct user research and usability testing; Collaborate with developers and product managers.', 'Bachelor\'s degree in Design or related field; 3+ years of UX design experience; Proficiency in design tools like Figma and Sketch.');

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
VALUES 
('Marketing Specialist', 'Mumbai, Maharashtra', 750000, 'Rs', 'Develop and execute marketing campaigns; Analyze market trends and data; Collaborate with sales and product teams.', 'Bachelor\'s degree in Marketing or related field; 2+ years of marketing experience; Strong analytical and communication skills.');

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
VALUES 
('DevOps Engineer', 'Chennai, Tamil Nadu', 1300000, 'Rs', 'Implement and manage CI/CD pipelines; Monitor and maintain infrastructure; Automate deployment processes.', 'Bachelor\'s degree in Computer Science or related field; 3+ years of experience in DevOps; Proficiency in cloud platforms like AWS and Azure.');

INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
VALUES 
('Front-End Develodper', 'Delhi, Delhi', 950000, 'Rs', 'Build and maintain the user interface of web applications; Ensure responsiveness and performance; Collaborate with back-end developers and designers.', 'Bachelor\'s degree in Computer Science or related field; 2+ years of experience in front-end development; Proficiency in HTML, CSS, and JavaScript frameworks like React or Angular.');

CREATE TABLE applications(
	id INT NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(250) NOT NULL,
    email VARCHAR(255) NOT NULL,	
    linkedin VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    experience VARCHAR(2000) NOT NULL,
    resume_link VARCHAR(255) NOT NULL,
	job_id INT,
    PRIMARY KEY (id),
	FOREIGN KEY (job_id) REFERENCES jobs(id)
);
