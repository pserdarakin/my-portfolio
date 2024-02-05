# Serdar's Portfolio Website

This project is a personal portfolio website built with Flask, showcasing my software development projects, professional information, and a contact form to reach out to me directly. The website features a responsive design, ensuring it looks great on all devices.

## Features

- **About Me**: A section that provides an overview of my professional background and skills.
- **Projects**: Highlights of my software projects, including descriptions and links to the project repositories.
- **Contact Form**: A form that visitors can use to send me a message directly through the website. This feature uses Flask-Mail to handle email sending.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or newer
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/yourprojectname.git

   cd yourprojectname
   ```

2. Create a .env file in the root of your project directory and add your environment variables:
    ```bash
    SECRET_KEY=your_secret_key
    MAIL_USERNAME=your_email_username
    MAIL_PASSWORD=your_email_password
    MAIL_DEFAULT_SENDER=your_default_sender_email 

    flask run  
    ```

### Usage

To use the application, open your web browser and navigate to:
    ```bash
http://127.0.0.1:5000/
    ```

### Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project.
2. Create your Feature Branch (git checkout -b feature/AmazingFeature).
3. Commit your Changes (git commit -m 'Add some AmazingFeature').
4. Push to the Branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.



