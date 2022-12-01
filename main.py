import os


def join_files(path):
    files = []
    for file in os.listdir(path):
        with open(os.path.join(path, file), encoding='utf-8') as f:
            files.append([len(f.readlines()), file])
    with open('result.txt', 'w') as r:
        for file in sorted(files):
            r.write(f'{file[1]}\n{file[0]}\n')
            with open(os.path.join(path, file[1]), encoding='utf-8') as f:
                r.writelines(f.readlines())
            r.write('\n')


if __name__ == '__main__':
    join_files('files')
