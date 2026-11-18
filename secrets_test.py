import os

def main():
    environment = os.getenv("DEPLOY_ENV", "dev")
    api_key = os.getenv("API_KEY")

    print(f"Environment: {environment}")

    if api_key:
        print("API Key: Successfully loaded from GitHub Secrets")
    else:
        print("API Key: Not found")

if __name__ == "__main__":
    main()
