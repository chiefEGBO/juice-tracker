import sys
from rich import print
from api import login, get_challenges, load_token
from cli import display_challenges, show_summary

def main():
    if len(sys.argv) < 2:
        print("[red]Usage:[/red] python main.py <command>")
        return

    command = sys.argv[1]

    if command == "login":
        email = input("Email: ")
        password = input("Password: ")

        token = login(email, password)

        if token:
            print("[green]Login saved![/green]")
        else:
            print("[red]Login failed[/red]")

    elif command == "status":
        token = load_token()
        challenges = get_challenges(token)

        filter_type = None

        if len(sys.argv) > 2:
            if sys.argv[2] == "--solved":
                filter_type = "solved"
            elif sys.argv[2] == "--unsolved":
                filter_type = "unsolved"

        display_challenges(challenges, filter_type)
        show_summary(challenges)

    else:
        print("[red]Unknown command[/red]")


if __name__ == "__main__":
    main()
