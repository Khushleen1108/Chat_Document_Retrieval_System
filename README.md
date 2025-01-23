# Chat-Document-Retrieval-Assistant

## Overview:
Chat-Document-Retrieval-Assistant is a document processing and interactive chatbot application that allows users to upload documents, store them in a vectorized format, and query the content through an intelligent conversational interface. The application utilizes LangChain for natural language processing, FAISS for vector storage, and Google’s Gemini model for enhanced AI responses. This project ensures data privacy by running a locally hosted LLM.

## Features:
- **User Authentication**: Sign up, login, and authenticate via email and password.
- **File Upload**: Upload various document types (TXT, PDF, DOCX) through the user interface.
- **Document Processing**: Process and vectorize documents, enabling efficient search and retrieval.
- **Interactive Chat Interface**: Engage with the AI chatbot to query documents and get AI-generated answers.
- **Data Privacy**: The system uses a local instance of the LLM, ensuring user data is processed privately.
- **Document Vectorization**: Embeds documents into vector space for efficient content retrieval via FAISS and HuggingFace.

## Architecture
The project is structured for scalability and modularity:
- **Main Application**: `main.py` (entry point for the web app)
- **User Management**: `user_management.py` (handles user sign-up, login, and authentication)
- **Document Upload & Processing**: `document_processing.py` (handles document uploads and processing)
- **Chat Interface**: `chat_history.py` (stores and retrieves chat history)
- **Utilities**: `ai_helpers.py` (handles AI responses and embedding generation)
- **Configuration**: `config.py` (handles environment variables and database connections)

## Project Structure:
```bash
Chat-Document-Retrieval-Assistant/
│
├── main.py                 # Entry point for the app
├── config.py               # Configuration for environment variables, database, and models
├── user_management.py      # Handles user registration, authentication, and email validation
├── document_processing.py  # Manages document uploads, vector store creation, and retrieval
├── ai_helpers.py           # AI response generation and embedding functions
├── chat_history.py         # Chat history management
│
├── uploaded_docs/          # Directory to store uploaded documents
├── .env                    # Environment variables (not included in version control)
├── .gitignore              # Lists files/directories to be ignored by Git
├── requirements.txt        # Python dependencies for the project
└── README.md               # Project documentation
```

## Installation:

**Clone the Repository:**

```bash
git clone <repository-url>
cd <repository-name>
```

**Set Up the Environment:**

Create a `.env` file in the root directory with the following content:

```bash
GOOGLE_API_KEY=your-google-api-key-here
DB_HOST=your-database-host
DB_PORT=your-database-port
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
```

**Install Dependencies:**

Ensure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

**Run the Application:**

To run the application, use the following command:

```bash
python main.py
```

## Usage

**User Authentication:**

Sign up or log in using the provided email and password. The application will store hashed passwords securely in the database.

**Upload Documents:**

Upload documents (TXT, PDF, DOCX) via the user interface. These documents will be processed and stored in the `uploaded_docs/` directory.

**Interact with the Chatbot:**

Use the chat interface to input questions. The system will respond based on the context of the uploaded documents, providing relevant AI-generated answers.

## Technologies Used

*   **LangChain:** For integrating LLMs with document retrieval and processing.
*   **HuggingFace:** For generating document embeddings and handling vectorization.
*   **FAISS:** For efficient vector-based document retrieval.
*   **PyPDF2 and python-docx:** For parsing PDF and DOCX files.
*   **psycopg2:** For PostgreSQL database interactions.
*   **Python-dotenv:** For loading environment variables.


## Documentation and User Guide

**User Guide:**

1. Upload your documents via the user interface.
2. Sign in and interact with the chatbot by typing your queries in the chat interface.
3. The bot will provide relevant information based on the uploaded documents.

**Code Documentation:**

The project's codebase includes well-commented functions for document processing, user authentication, and AI response generation. Refer to `config.py` for setting up the environment variables for database and API keys.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contact

For any questions or feedback, please contact Khushleen Kaur at [k2aur8154@gmail.com].
