# Personal Event Management API

This project is an **exploration** of integrating an API using **FastAPI**, **SQLAlchemy**, **Google Calendar**, and a **Large Language Model (LLM)** to create an trainer for GYM exercises. 

## Features

- **Routine generator**: Generate exercises routines based on the specifications of the user, like muscles to be trained and injuries.
- **LLM-Powered Assistance**:
  - Suggest **event locations**.
  - Identify the **best time slots** for new events.
  - **Summarize the day's agenda**.
  - Highlight **important reminders** and action items.

## Technologies Used

- **FastAPI**: For building the RESTful API.
- **SQLAlchemy**: For database management.
- **LangChain**: To communicate with the LLM services.
- **LangSmith**: For tracking and debugging LLM interactions.
- **LLM (Large Language Model)**: For intelligent routines and recommendations.

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