# Personal Event Management API

This project is an **exploration** of integrating an API using **FastAPI**, **SQLAlchemy**, **Google Calendar**, and a **Large Language Model (LLM)** to effectively manage a personal event agenda.

## Features

- **Event Scheduling**: Create, update, and manage personal events.
- **Google Calendar Integration**: Sync events, read schedules, and highlight important reminders.
- **LLM-Powered Assistance**:
  - Suggest **event locations**.
  - Identify the **best time slots** for new events.
  - **Summarize the day's agenda**.
  - Highlight **important reminders** and action items.

## Technologies Used

- **FastAPI**: For building the RESTful API.
- **SQLAlchemy**: For database management.
- **Google Calendar API**: For event synchronization.
- **LLM (Large Language Model)**: For intelligent scheduling and recommendations.

## Goal

The goal of this project is to explore how LLMs can enhance personal event management by providing smart recommendations, improving scheduling efficiency, and integrating seamlessly with Google Calendar.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/nicusbonannus/aissistant.git
   cd your-repo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for API keys (Google Calendar, LLM, etc.).

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Future Improvements

- Expand LLM capabilities for more personalized scheduling.
- Implement voice command integration.
- Improve UI/UX for better event visualization.

---

🚀 **This is an experimental project. Contributions and feedback are welcome!**