from local_lib import path

def foo():
    path.Path("new_dir").mkdir()
    path.Path("new_dir/new_file.txt").touch()
    path.Path("new_dir/new_file.txt").write_text("My program works fine!")
    txt = path.Path("new_dir/new_file.txt").read_text()
    print(txt)


if __name__ == '__main__':
    foo()