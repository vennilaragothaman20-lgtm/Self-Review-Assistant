Self-Review Assistant
About
A simple Python project that takes a task or topic, creates a response, and checks it using a basic rule.
How It Works
1. Enter a task or topic, such as Python or SQL.
2. The assistant generates an initial response.
3. The critic checks whether the response has at least 10 words.
4. If it fails, the assistant revises the response.
5. The program returns the response if it passes, or stops when the retry limit is reached.
Requirements
- Python
- VS Code (recommended)
No extra Python packages are needed.
How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:
   python main.py
4. Enter a task or topic when asked.
Example
Input:
Python

The assistant first creates a short response. The critic asks for a revision because it is too short. The assistant then creates a longer response and checks it again.
Note
This is a beginner project that demonstrates the Generate → Critic → Revise → Pass workflow. The critic checks word count only; it does not check whether the answer is factually correct.