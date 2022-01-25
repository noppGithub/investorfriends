import os


def list_all_files(mypath):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            files.append(fp)
    return files


if __name__ == "__main__":
    fp = "./img/technical_timing_a_buy"
    for f in list_all_files(fp):
        print(f)
