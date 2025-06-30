import os
import sys
import subprocess
import requests

# --- Configuration ---
# IMPORTANT: This must match the address of your running chat_server.py
SERVER_URL = "http://127.0.0.1:5000"

# File names
ENCRYPTION_FILE = "encryption_code.py"

def download_file(url, local_filename):
    """Downloads a file from a URL and saves it locally."""
    print(f"Downloading {local_filename} from {url}...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Successfully downloaded {local_filename}.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to download {local_filename}.")
        print(f"Reason: {e}")
        print("Please ensure the server is running and the URL is correct.")
        return False

def main():
    """
    Main function to guide the user, download necessary files,
    and launch the appropriate chat client.
    """
    print("--- Secure Chat Launcher ---")

    # --- Determine user role ---
    user_role = ""
    while user_role not in ["alice", "bob"]:
        user_role = input("Are you 'alice' or 'bob'? ").lower().strip()
        if user_role not in ["alice", "bob"]:
            print("Invalid input. Please enter 'alice' or 'bob'.")

    client_file = f"{user_role}-client.py"

    # --- Download the necessary files from the server ---
    
    # 1. Download the encryption library (required by both clients)
    encryption_url = f"{SERVER_URL}/download/encryption"
    if not download_file(encryption_url, ENCRYPTION_FILE):
        sys.exit(1) # Exit if we can't get the encryption library

    # 2. Download the specific client file
    client_url = f"{SERVER_URL}/download/{user_role}"
    if not download_file(client_url, client_file):
        sys.exit(1) # Exit if we can't get the client script

    # --- Launch the client ---
    print(f"\nAll files downloaded. Launching the {user_role} client...")
    print("You can start chatting in this terminal window.")
    print("--------------------------------------------------")

    try:
        # Use subprocess to run the downloaded client script in the current terminal
        # sys.executable ensures we use the same Python interpreter that is running this launcher
        subprocess.run([sys.executable, client_file], check=True)
    except FileNotFoundError:
        print(f"Error: Could not find the Python interpreter '{sys.executable}'.")
    except subprocess.CalledProcessError:
        # This can happen if the client exits with an error.
        # The client script itself should print the specific error.
        print(f"\nThe {user_role} client exited unexpectedly.")
    except KeyboardInterrupt:
        print("\nLauncher interrupted by user. Exiting.")
    finally:
        # --- Cleanup: Optional ---
        # You can choose to delete the downloaded files after the chat session ends.
        # print("\nCleaning up downloaded files...")
        # if os.path.exists(ENCRYPTION_FILE):
        #     os.remove(ENCRYPTION_FILE)
        # if os.path.exists(client_file):
        #     os.remove(client_file)
        print("Launcher has finished.")


if __name__ == "__main__":
    main()
