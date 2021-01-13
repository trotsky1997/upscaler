# Skyrim texture upscaler

Usage:
Install Docker and python3 first.
```bash
git clone https://github.com/trotsky1997/upscaler.git
pip install tqdm requests click
docker pull codait/max-image-resolution-enhancer
docker run -it -p 5000:5000 codait/max-image-resolution-enhancer

cd upscaler
python main.py --help

# python main.py --factor=2 --path='./'

```