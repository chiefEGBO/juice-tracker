from rich import print

def display_challenges(challenges, filter_type=None):
    challenges = sorted(challenges, key=lambda c: c['difficulty'])

    for c in challenges:

        if filter_type == "solved" and not c['solved']:
            continue
        if filter_type == "unsolved" and c['solved']:
            continue

        if c['solved']:
            status = "[bold green]✔ SOLVED[/bold green]"
        else:
            status = "[bold red]✖ NOT SOLVED[/bold red]"

        print(f"{status} {c['name']} [yellow](Difficulty: {c['difficulty']})[/yellow]")


def show_summary(challenges):
    total = len(challenges)
    solved = sum(1 for c in challenges if c['solved'])

    print(f"\n[bold cyan]Progress:[/bold cyan] {solved}/{total} solved")
