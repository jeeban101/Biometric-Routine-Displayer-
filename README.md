# Biometric Routine Displayer

## Table of Contents

- [Abstract](#abstract)
- [Problem Statement](#problem-statement)
- [Introduction](#introduction)
- [Motivation](#motivation)
- [Objectives](#objectives)
- [Architecture](#architecture)
- [Implementation and Results](#implementation-and-results)
- [Conclusion and Future Enhancement](#conclusion-and-future-enhancement)
- [References](#references)
- [Contributors](#contributors)

## Abstract

People working in large-scale organizations often face problems regarding their schedules and time-tables. For instance, in any university students and sometimes even teachers/professors tend to forget their class schedule. It results in failure in attending class. Similar problems are faced by employees in their workplace too. In order to solve this issue, we have come up with a technological solution that provides people information about their respective schedule at the particular time hour of their day through Biometric recognition.

## Problem Statement

The modern work and education environments often involve complex schedules that can be challenging to manage. People struggle with remembering their class or work timings, leading to inefficiencies and missed opportunities. The Biometric Routine Displayer project aims to address this problem by utilizing biometric recognition technology to provide users with easy access to their daily schedules.

## Introduction

In this project, we present an innovative solution to the problem of managing and accessing daily schedules. The Biometric Routine Displayer leverages biometric recognition, specifically facial recognition, to allow users to retrieve their schedules conveniently and efficiently. Users can simply scan their face or manually enter their unique identity (e.g., registration number) to access their daily timetable.

## Motivation

This project was conceived to address the challenges faced by individuals in organizations, schools, and universities when managing their schedules. As one of the contributors to this project, I, Jeeban, handled the user detection and data retrieval aspects of the system. My focus was on developing the facial recognition component and integrating it with the database to fetch users' schedules.

## Objectives

The main objectives of the Biometric Routine Displayer project are as follows:

1. Provide easy access for users to view their daily schedules.
2. Minimize scheduling conflicts and improve efficiency.
3. Store user access details in the system.
4. Enhance efficiency and productivity by minimizing time consumption.

## Architecture

The architecture of the Biometric Routine Displayer consists of several key components:

- User Input: Users can access their schedules by either scanning their face using the OpenCV-Python library or manually entering their unique identity, such as a registration number.
- Data Retrieval: The system fetches the schedule data from a MySQL database, which contains tables for each day of the week.
- User Interface: The application presents the retrieved schedule to the user, displaying either the entire day's timetable or the schedule for the current time period.

## Implementation and Results

The project is implemented using Python and MySQL. The facial recognition functionality is achieved through the OpenCV-Python library. The system successfully recognizes users' faces and retrieves their schedules based on the current day and time.

## Conclusion and Future Enhancement

The Biometric Routine Displayer project offers a practical and efficient solution for managing schedules. It simplifies the process of accessing daily timetables, especially in large-scale organizations and educational institutions. Future enhancements could include the integration of additional biometric modalities, such as fingerprint recognition, and the development of a master timetable generation feature.

## Contributors

- Jeeban: User detection and data retrieval from the database.

This project was initially developed as a team project, with each contributor focusing on specific aspects. The use of biometric recognition technology adds a layer of convenience and security to schedule management, benefiting a wide range of users.
