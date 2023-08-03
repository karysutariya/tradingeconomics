# My Flask Web App

This is a simple Flask web application that displays a table and two charts. The app utilizes the Flask framework, Chart.js for generating charts, and Pandas for handling data.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Introduction

This Flask web app is designed to showcase basic data visualization using charts. The data used in the charts is fatched tradingeconomics api of sweden and mexico. 

## Installation

To run the Flask app, follow these steps:

1. Clone the repository:

    '''bash
    git clone https://github.com/karysutariya/tradingeconomics.git
    '''

2. Create a virtual environment (optional but recommended):

    '''bash
    conda create <environment_name> py38 python=3.8
    conda activate <environment_name>
    '''

3. Install the required dependencies:

    '''bash
    pip install -r requirements.txt
    '''

## Usage

After installing the dependencies, run the Flask app:

1. To run the flask app:

    '''bash
    python app.py 
    '''

The app will be accessible at `http://localhost:5000`.

## Endpoints

- `/`: This is the home page that displays the charts.
