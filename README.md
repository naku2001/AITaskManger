AI Google Calendar Agent
A simple AI-powered assistant that lets you manage your Google Calendar using natural language commands.

Features
Create, update, move, delete calendar events

List upcoming events

Authenticate securely with Google using OAuth2

Understands plain English instructions via AI

Setup
Create Google API credentials

Go to Google Cloud Console

Create a project and enable Google Calendar API

Create OAuth 2.0 credentials (Desktop app)

Download credentials.json and place it in the project folder

Install dependencies

bash
Copy
Edit
pip install langchain-google-community langchain google-auth-oauthlib
Run the app

bash
Copy
Edit
python CALENDAR.py
On first run, a browser window will open for Google authentication.

Usage
Type natural language commands like:

sql
Copy
Edit
Create a green event for a 30-minute run this afternoon.
Delete my meeting tomorrow at 2 PM.
Show me my events for next week.
The agent will interact with your Google Calendar accordingly.

Notes
This is a learning project to demonstrate AI + Google API integration.

Make sure to keep your credentials.json secure.

Tokens will be saved locally for reuse.
