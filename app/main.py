def copy_file(command: str) -> None:
    parts = command.split()
    try:
        if not parts[0] == "cp":
            return
        if not parts[1] == parts[2]:
            with (open(parts[1], "r") as source_file,
                  open(parts[2], "w") as destination_file):
                destination_file.write(source_file.read())
    except Exception as e:
        print(e)
