import requests
import os
from tqdm import tqdm
import click




@click.command()
@click.option('--path', default='./')
@click.option('--factor', default=1)
def main(path,factor):
    print(factor)
    files = [os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(path)
        for f in files if f.endswith('.dds')]


    for file in tqdm(files):
        time = 0
        file0 = {'image': open(file, 'rb')}
        while time*1.0 < factor * 1.0:
            url = 'http://127.0.0.1:5000/model/predict'
            print(file0)
            A = requests.post(url, files=file0)
            with open(f"{file[:-3]}png","wb") as f:
                f.write(A.content)
            file0["image"].close()
            file0 = {'image': open(f"{file[:-3]}png", 'rb')}
            time += 1
            # print(file)

if __name__ == '__main__':
    main()