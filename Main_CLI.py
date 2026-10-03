from organizer import FileOrganizer
import argparse
from rich.console import Console
import time

def main():

    # Creating an instance
    console = Console()

    # Creating a parser
    parser = argparse.ArgumentParser(description="AutoFile Organizer\nAutomatically Organize files based on their file type")

    console.rule("[bold cyan]AutoFile Organizer[/bold cyan]")

    # Adding Arguments (Positional(Required) & Optional)
    parser.add_argument("location", type=str, help="Input the file location for organizing.")
    parser.add_argument("--dry-run", action="store_true", help="Used to run a preview without making changes to the files")

    # Parse Arguments (Access values via dot.notations)
    args = parser.parse_args()
    organizer = FileOrganizer(args.location, args.dry_run)

    # Existing path validation logic in organizer.py
    if not organizer.validate_location():
        return

    # Rich Status Spinner during directory scanning
    with console.status(
            f"[bold green]Scanning directory '{args.location}'...[/bold green]",
            spinner="dots",
    ):
        time.sleep(2)  # Simulating folder scanning work
        console.print("[bold green]✓[/bold green] Directory scan complete!")

    if args.dry_run:
        console.print("[bold orange1]MODE:[/bold orange1] [italic]Dry Run (No files will be modified)[/italic]")
    else:
        console.print("[bold green]MODE:[/bold green] Live Execution")

    # Running organize_folder() method in organizer.py
    organizer.organize_folder()

    # Check if running dry run or not to show below print
    if args.dry_run:
        console.print(f"[bold green]Dry run complete.[/bold green] [bold]{organizer.count_files}[/bold] files would be moved.\n[red]No files were changed[/red]")

if __name__ == "__main__":
    main()