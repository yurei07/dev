import click
import subprocess
import os
import pathlib

user = "Prizrak"
userLaptop = "laptop_Prizrak"

pathBathEtc = pathlib.Path('/etc/')
pathBathHome = pathlib.Path(f'/home/{user}/')
pathBathHomeD = pathlib.Path(f'/home/{user}/Documents')

nixos = pathlib.Path('/etc/nixos/')
#nixos = pathlib.Path(f'/home/{user}/Documents/nixos/')

newNixos = pathlib.Path(f'/home/{user}/nixos/')

file_check = "check.txt"


@click.group()
def cli_git():
    click.echo("My application git CLI")


@cli_git.command()
@click.option(
    "--choice",
    prompt="Your choice",
    help="Choise of commands: v = version, l = log, s = show",
)
def choice(choice):
    v = subprocess.run(["git", "--version"], text=True, capture_output=True)

    result_v = v.stdout.strip()

    match choice:
        case "v":
            click.echo(f"It is your {result_v}. You are welcome!:)")
        case "l":
            subprocess.run(["git", "log"])
        case "s":
            subprocess.run(["git", "show"])


@cli_git.command()
@click.option(
    "--combo",
    prompt="Your combo",
    type=str,
    help="Combo creates commit and saves files in the Git of the repository",
)
def combo(combo):
    match combo:
        case "pull":
            if os.path.exists(file_check):
                os.system(
                    "rm -rf ./flake.lock ./flake.nix ./hosts ./materials ./modules ./scripts "
                )
                os.system("cp -r /etc/nixos/* ./")
                os.system("git add . --all")

                value = input("Enter commit name (enter to default): ")

                if value != "":
                    os.system(f'git commit -m "{value}"')
                    os.system("git pull")
                    os.system("git push -u")
                elif value == "":
                    os.system('git commit -m "update"')
                    os.system("git pull")
                    os.system("git push -u")
        case "update":
            # OPEN DIRECTORIES AND FIND FILES
            def traverse_directories(current_path: pathlib.Path):
                listFiles = []
                for i in current_path.iterdir():
                    if i.is_dir():
                        function = traverse_directories(i)
                        listFiles.extend(function)
                    elif i.is_file():
                        if i.suffix == '.nix':
                            listFiles.append(i)
                return listFiles
            nameNew = traverse_directories(newNixos)
            nameOld = traverse_directories(nixos)
            for j in range(len(nameNew)):
                for i in range(2, len(nameOld)):
                    new = nameNew[j].relative_to(pathBathHome)
                    old = nameOld[i].relative_to(pathBathEtc)
                    if new == old:
                        if nameNew[j].read_text() == nameOld[i].read_text(): 
                            print(True)
                        elif nameNew[j].read_text() != nameOld[i].read_text():
                            print(f'The files arent correct :( : {nameNew[j].read_text()} and {nameOld[i].read_text()}')
                            question = input("Do you want to upgrade? (input y/n y = yes, n = no): ")
                            if question.lower() == 'y':
                                content = nameNew[j].read_text(encoding='utf-8')
                                nameOld[i].write_text(content, encoding='utf-8')
                                print('IT WORKS!!!!!!!')
                                print(nameNew[j], nameOld[i])
    
if __name__ == "__main__":
    cli_git()
