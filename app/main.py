def copy_file(copy: str) -> None:
    lst = copy.split()
    try:
        if not lst[0] == "cp":
            return
        if not lst[1] == lst[2]:
            with open(lst[1], "r") as f, open(lst[2], "w") as g:
                g.write(f.read())
    except Exception as e:
        print(e)
