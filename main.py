import os
import hashlib
from config import BASE_DOCS_DIR
from user_management import is_valid_email, check_if_email_exists, add_user_to_db, verify_user_credentials, get_user_id_by_email
from chat_history import get_chat_history, update_chat_history
from ai_helpers import generate_prompt, get_ai_response
from document_processing import handle_file_upload, load_documents_from_directory, initialize_vector_store

def handle_user_input(email, vectorstore):
    user_id = get_user_id_by_email(email)
    chat_history = get_chat_history(user_id)

    if chat_history:
        print("\nPrevious Chat History:")
        for message_pair in chat_history:
            print(f"User: {message_pair['user']}")
            print(f"AI: {message_pair['ai']}")
            print("-" * 50)
    else:
        print("\nNo previous chat history available.")

    while True:
        user_input = input("Ask your question (type 'exit' to return to the menu):\n> ").strip()

        if user_input.lower() == "exit":
            print("Returning to main menu...")
            break

        retriever = vectorstore.as_retriever()
        context = "\n\n".join(doc.page_content for doc in retriever.invoke(user_input, k=5))

        prompt = generate_prompt(chat_history, user_input, context)
        ai_response = get_ai_response(prompt)
        print("AI Assistant Response:", ai_response)

        update_chat_history(user_id, user_input, ai_response)

def handle_user_action(email):
    while True:
        user_docs_dir = os.path.join(BASE_DOCS_DIR, email)
        documents_exist = os.path.exists(user_docs_dir) and os.listdir(user_docs_dir)

        if documents_exist:
            upload_choice = input("Do you want to upload more documents? [yes/no]: ").strip().lower()
            if upload_choice == "yes":
                uploaded_files = input("Enter file paths (comma-separated): ").split(",")
                handle_file_upload(email, uploaded_files)
        else:
            upload_choice = input("Do you want to upload documents? [yes/no]: ").strip().lower()
            if upload_choice == "yes":
                uploaded_files = input("Enter file paths (comma-separated): ").split(",")
                handle_file_upload(email, uploaded_files)

        vectorstore = initialize_vector_store(load_documents_from_directory(email), email, reset=False)
        if vectorstore:
            handle_user_input(email, vectorstore)
        else:
            print("No documents available to process.")

        action = input("Do you want to logout or exit? [logout/exit]: ").strip().lower()
        if action == "logout":
            print("Logging out...")
            break
        elif action == "exit":
            print("Exiting system...")
            exit(0)

def setup_user_management():
    while True:
        action = input("Choose action: [Login/Sign Up/Exit]: ").strip().lower()

        if action == "login":
            email = input("Enter Email ID: ").strip()
            password = input("Enter Password: ").strip()

            if check_if_email_exists(email) and verify_user_credentials(email, password):
                print(f"Logged in as: {email}")
                handle_user_action(email)
            else:
                print("Invalid Email ID or Password.")

        elif action == "sign up":
            email = input("Enter Email ID for Sign Up: ").strip()
            password = input("Enter Password: ").strip()
            confirm_password = input("Confirm Password: ").strip()

            if not is_valid_email(email):
                print("Invalid email format!")
            elif password != confirm_password:
                print("Passwords do not match!")
            elif check_if_email_exists(email):
                print("Email ID already exists!")
            else:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                add_user_to_db(email, hashed_password)
                print(f"Email ID {email} signed up successfully! Please log in.")

        elif action == "exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    setup_user_management()
