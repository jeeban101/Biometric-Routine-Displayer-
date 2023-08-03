# Biometric Routine Displayer

## Table of Contents
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Motivation](#motivation)
- [Objectives](#objectives)
- [Problem Statement](#problem-statement)
- [Existing System](#existing-system)
- [Modules](#modules)
- [Architecture](#architecture)
- [Proposed Technique](#proposed-technique)
- [Results and Discussion](#results-and-discussion)
- [Conclusion and Future Enhancement](#conclusion-and-future-enhancement)
- [References](#references)

## Abstract
Biometric Routine Displayer is an innovative solution designed to address the challenges individuals face in managing their daily schedules. This project utilizes biometric recognition, specifically facial recognition, to provide users with real-time access to their timetables. Users can simply scan their face or manually input their unique identity number to instantly retrieve their schedules. The system enhances time management, efficiency, and productivity across various domains such as education, workplaces, hospitals, and more.

## Introduction
Biometric Routine Displayer aims to simplify schedule management for individuals in various settings. Whether it's students in educational institutions, employees in workplaces, or medical professionals in hospitals, the system ensures that users have easy access to their daily routines. By utilizing biometric recognition and database integration, the project offers an efficient and user-friendly approach to timetable management.

## Motivation
The motivation behind Biometric Routine Displayer is rooted in addressing the common challenge of schedule management. With the increasing demand for efficient time utilization, the project seeks to provide a solution that eliminates the need for manual schedule checks. By integrating biometric recognition technology, the system enables users to access their timetables quickly and accurately, thereby enhancing productivity and reducing time wastage.

## Objectives
The primary objectives of Biometric Routine Displayer include:

1. Providing easy and real-time access to users' schedules.
2. Minimizing conflicts and optimizing timetable scheduling.
3. Storing user details and attendance records for future reference.
4. Improving efficiency and time management for users.
5. Enabling both biometric and manual (registration number) login modes.

## Problem Statement
The modern world often faces challenges in efficiently managing schedules. Individuals, whether students, employees, or professionals, struggle to remember and access their daily routines. This problem becomes even more pronounced in large-scale organizations. Biometric Routine Displayer aims to solve this problem by leveraging biometric recognition technology to offer seamless access to schedules and reduce time-consuming manual checks.

## Existing System
The existing system relies on conventional methods of schedule management, which often involve manual checks or accessing timetables through various platforms. Biometric Routine Displayer introduces a more streamlined and convenient approach by integrating biometric recognition, which eliminates the need for manual searches and ensures accurate and efficient schedule retrieval.

## Modules
The Biometric Routine Displayer project comprises the following modules:

1. Attendance.csv: Contains details of users who have accessed the system.
2. FacematchProject.py: Includes functions and code for the project.
3. ImageAttendance: Stores images of users for facial recognition.
4. UserDetails: Contains user information, including registration numbers, names, and course session details.

## Architecture
The project follows a modular architecture that incorporates various components:

1. Database Connectivity: Establishes connection with MySQL database for data storage.
2. Biometric Recognition: Utilizes OpenCV and face_recognition modules for facial recognition.
3. Attendance Logging: Records user attendance and time of access in the Attendance.csv file.
4. Data Retrieval: Fetches schedule data from the database based on user inputs.

## Proposed Technique
Biometric Routine Displayer operates based on a user-friendly approach:

1. Users can log in using biometric (facial recognition) or manual (registration number) modes.
2. Facial recognition technology scans the user's face and matches it with stored data.
3. Upon successful recognition, the system displays the user's timetable for the chosen period.
4. The system also logs the user's attendance and access time in the Attendance.csv file and the database.

## Results and Discussion
The implementation of Biometric Routine Displayer has yielded promising results. Users can seamlessly access their schedules in real time using either biometric or manual methods. The system's accuracy and efficiency contribute to enhanced time management and productivity. The project demonstrates the feasibility of leveraging biometric recognition for schedule management across various domains.

## Conclusion and Future Enhancement
Biometric Routine Displayer offers an efficient solution to schedule management challenges by utilizing biometric recognition technology. The project's success in providing real-time schedule access demonstrates its potential for adoption in educational institutions, workplaces, hospitals, and other settings. As a future enhancement, additional features such as fingerprint scanning and master timetable generation could be explored to further improve the system's capabilities.

## References
1. W3Schools - Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp
2. Stack Overflow - OpenCV Camera: https://stackoverflow.com/questions/46821936/open-cv-close-camera
3. Stack Overflow - Face Recognition Installation: https://stackoverflow.com/questions/52332268/pip-install-face-recognition-giving-error
4. OpenCV Python Documentation: https://pypi.org/project/opencv-python/
5. W3Schools - Python MySQL SELECT: https://www.w3schools.com/python/python_mysql_select.asp
6. YouTube - OpenCV Face Recognition: https://www.youtube.com/watch?v=sz25xxF_AVE
