# lib
# nltk.download('stopwords')
# gdown https://drive.google.com/drive/u/4/folders/1-C7GWK0ujaSACsaDlqsHPf8J__0-oFsR -O lib/sentimen/indo --folder
# gdown https://drive.google.com/drive/u/4/folders/1X0fE-F2FQ-FOQKUJWWbBlmsUsk_hpgz5 -O lib/sentimen/eng --folder
# gdown https://drive.google.com/drive/folders/1B8oyt7AD268TU6i-yLtE6ZcGdzH-C0b9?usp=share_link -O lib/gender --folder

# dataset
# gdown https://drive.google.com/drive/u/4/folders/1OGWi6L-MZEdNYLAVs-63apWaGKlUJFU_ -O data/instagram/ --folder
# gdown https://drive.google.com/drive/folders/1-h2E9cagdtEfSlabPvFnZyX2FbRBnWrP?usp=sharing -O data/instagram/ --folder --remaining-ok

# sudo lsof -t -i tcp:5000 | xargs kill -9

import os

import nltk

nltk.download("stopwords")
nltk.download("punkt")
os.system(
    "gdown https://drive.google.com/drive/u/4/folders/1-C7GWK0ujaSACsaDlqsHPf8J__0-oFsR -O lib/sentimen/indo --folder"
)
os.system(
    "gdown https://drive.google.com/drive/u/4/folders/1X0fE-F2FQ-FOQKUJWWbBlmsUsk_hpgz5 -O lib/sentimen/eng --folder"
)
os.system(
    "gdown https://drive.google.com/drive/folders/1B8oyt7AD268TU6i-yLtE6ZcGdzH-C0b9?usp=share_link -O lib/gender --folder"
)
os.system(
    "gdown https://drive.google.com/drive/u/4/folders/1OGWi6L-MZEdNYLAVs-63apWaGKlUJFU_ -O data/instagram/ --folder"
)
os.system(
    "gdown https://drive.google.com/drive/folders/1-h2E9cagdtEfSlabPvFnZyX2FbRBnWrP?usp=sharing -O data/instagram/ --folder --remaining-ok"
)
