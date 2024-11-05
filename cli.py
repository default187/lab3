import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI для доступа к приложению")
    parser.add_argument("--action", type=str, help="Действие, которое нужно выполнить", required=True)

    args = parser.parse_args()

    if args.action == "start":
        response = requests.get("http://localhost:8000/start")
        print(response.json())
    elif args.action == "status":
        response = requests.get("http://localhost:8000/status")
        print(response.json())
    else:
        print("Неизвестное действие")

if __name__ == "__main__":
    main()
