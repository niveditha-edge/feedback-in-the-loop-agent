# 🔄 Feedback-in-the-Loop Agent

An AI-powered writing assistant built with **Python, Streamlit, and Groq** that iteratively improves generated drafts based on human feedback.

The application generates an initial draft, allows users to review and edit it, and uses their feedback to produce improved versions through multiple revision rounds.

## 🚀 Features

- **AI-Powered Draft Generation:** Generate content using a Groq-hosted language model.
- **Human-in-the-Loop Feedback:** Provide natural-language instructions to improve generated content.
- **Iterative Refinement:** Improve drafts through multiple rounds of feedback.
- **Editable Drafts:** Review and modify AI-generated text before requesting revisions.
- **Feedback History:** View previous feedback and the corresponding revised drafts during the current session.
- **Download Support:** Download the latest draft as a text file.
- **Input Validation:** Prevent empty drafts and empty feedback from being processed.
- **Automated Unit Tests:** Test core functionality without making live API calls.

## 🛠️ Tech Stack

- **Python 3.11** — application logic
- **Streamlit** — interactive web interface
- **Groq API** — AI text generation and refinement
- **OpenAI Python SDK** — API client compatible with Groq
- **python-dotenv** — local environment variable management
- **unittest** — automated testing

## 🧠 How It Works

1. The user enters a writing request.
2. The AI generates an initial draft.
3. The user reviews and optionally edits the draft.
4. The user provides feedback describing the desired improvements.
5. The AI generates a revised draft using the current draft and feedback.
6. The user can repeat the feedback process until satisfied.
7. The latest draft can be downloaded.

### Workflow

```text
User Request
     |
     v
AI Draft Generation
     |
     v
Human Review and Editing
     |
     v
Human Feedback
     |
     v
AI Draft Improvement
     |
     v
Review Revised Draft
     |
     +------> Provide More Feedback
     |                   |
     |                   v
     |            AI Improves Draft
     |
     v
Download Final Draft
```

## 📂 Project Structure

```text
feedback-in-the-loop-agent/
├── app.py
├── main.py
├── test_agent.py
├── test_main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env                 # Local only; not committed
```

- `app.py` — Streamlit user interface and feedback workflow.
- `main.py` — functions for initial draft generation and improvement.
- `test_agent.py` — manual test for initial generation and multiple feedback rounds; uses the live Groq API.
- `test_main.py` — automated unit tests using mocked API responses.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes virtual environments, generated files, and secrets.
- `.env` — stores the local Groq API key and must remain private.

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.11
- A Groq API key
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/niveditha-edge/feedback-in-the-loop-agent.git
cd feedback-in-the-loop-agent
```

### 2. Create a virtual environment

On Windows:

```powershell
py -3.11 -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project directory:

```text
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your own Groq API key.

**Security:** Never commit `.env` to GitHub or expose your API key in screenshots, source code, or public documentation.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🧪 Testing

### Run automated unit tests

```bash
python -m unittest test_main.py -v
```

The automated tests mock the Groq API client, allowing the core functions to be tested without live API calls or API credits.

The tests cover:

- Initial draft generation.
- Draft improvement using feedback.
- Validation of empty original drafts.
- Validation of empty feedback.

### Run the manual AI test

```bash
python test_agent.py
```

This test makes live API calls to Groq. It demonstrates initial generation and two successive feedback rounds. API usage limits may apply.

## ☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

1. Push the project to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create an app using this repository and the `main` branch.
4. Set the main file path to `app.py`.
5. Add the API key in the app's Secrets settings:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

6. Deploy the application.

Do not upload your local `.env` file. The deployed application reads the API key from Streamlit Secrets.

**Live Demo:** Add your deployed Streamlit URL here after deployment.

## 🔐 Limitations and Considerations

- The AI may produce inaccurate or unsupported information. Review generated content before using it.
- Human feedback guides the next generation; it does not permanently train or fine-tune the underlying model.
- Long outputs depend on the model's context and output-token limits.
- Feedback history is stored in the current Streamlit session and is not a persistent database or audit log.
- The application generates and downloads text; it does not automatically send emails or submit external requests.
- API usage is subject to Groq's limits and terms.

## 🔮 Future Improvements

- Persistent feedback and revision history.
- User ratings for each revision.
- Better preservation of facts from the original draft.
- Export to PDF and DOCX.
- Support for multiple writing tasks and document types.
- Authentication and multi-user support.

## 👩‍💻 Author

**Niveditha S.**

Built as a learning project to explore AI applications, human feedback loops, LLM integration, and iterative content refinement.

## 📄 License

No license has been added yet. Add a license file if you intend to specify how others may use, modify, or distribute this project.
