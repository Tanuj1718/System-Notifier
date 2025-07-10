# System Resource Notifier 🚨

The **System Resource Notifier** script is designed to monitor your system's **CPU**, **RAM**, and **Disk** usage in real-time and send you **email alerts** when any of these resources exceed a defined threshold. Built in **Python**, it uses the `psutil` library for system monitoring and `smtplib` for email notifications.

### Features

- **System Resource Monitoring**: Continuously checks CPU, RAM, and Disk usage.

- **Threshold-based Alerts**: Configurable limits for CPU, RAM, and Disk. The script will alert you if any resource exceeds its threshold.

- **Humorous Notifications**: Includes lighthearted and fun messages in email notifications to make resource monitoring a little less stressful.

- **Email Alerts**: Sends a concise email with detailed system status when a threshold is exceeded.

- **Periodic Execution**: Set up the script to run at regular intervals using cron (Linux/macOS) or Task Scheduler (Windows).

---

## Requirements

Before running the script, you need the following:

- **Python 3.x** (preferably version 3.6+)

- `psutil`: Library for system monitoring.

- `python-dotenv`: Helps to load environment variables securely (like email credentials).

You can install the dependencies using `pip`:

``pip install -r requirements.txt``

The requirements.txt file includes:

psutil

python-dotenv

## Setup Guide

1. Clone or Download the Repository

   First, download or clone the repository to your local machine:

   ``git clone https://github.com/Tanuj1718/System-Notifier.git``


2. Create the .env File
   
   For security purposes, the script uses environment variables to store sensitive information like email credentials. Create a .env file in the project               directory with the following contents:

   EMAIL_FROM=your_email@gmail.com

   EMAIL_TO=recipient_email@gmail.com

   EMAIL_PASS=your_app_password

   **Note:** To generate an App Password for Gmail:

  Enable 2FA (two-factor authentication) for your Gmail account.

  Create an App Password from your Google Account settings.

  Use this app password in place of your regular Gmail password.

3. Run the Script

   Once everything is set up, run the script manually to check your system's usage:

   ``python script.py``

The script will print the system's current usage to the console and send an email alert if any resource exceeds the defined threshold.

## Configuration

By default, the script uses the following thresholds:

CPU_THRESHOLD = 80  # Trigger alert if CPU usage exceeds 80%

RAM_THRESHOLD = 80  # Trigger alert if RAM usage exceeds 80%

DISK_THRESHOLD = 90 # Trigger alert if Disk usage exceeds 90%

You can modify these thresholds in the script to match your specific needs. For example, you can increase the CPU_THRESHOLD to 90 if you want an alert only for high CPU usage above 90%.

## Scheduling the Script

To run the script periodically (for example, every 10 minutes), you can set up a cron job.

Open the cron table for editing:

``crontab -e``

Add the following line to run the script every 10 minutes:

``*/10 * * * * /usr/bin/python3 /file_path``

Save and exit the editor.

The cron job will now automatically run the script at the specified intervals.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

If you'd like to contribute to the project and suggest some features, feel free to fork the repository and submit a pull request. I would be happy to accept improvements and new features!


## Summary

This script makes it easy to keep track of your system resources and get notified if things are running hot! Set it up, adjust the thresholds, and you'll never miss a high CPU or memory spike again. 

