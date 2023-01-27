Create environment


'''bash
python - m venv venv 
'''

activate env 
'''bash
venv/Scripts/venv
'''

create req file

install the req
'''bash
pip install -r requirements.txt 
'''

download the data from 

https://www.kaggle.com/datasets/rajyellow46/wine-quality?resource=download

git init 

dvc init 

dvc add remote_data/winequalityN.csv 

git add . 

git commit -m "First Commit" 

"""
After running dvc add remote_data/winequalityN.csv, .gitignore file is created once initialized and it is not uploading the csv file instead keeping the version of it md5  checksome format...!!! naming it's size and where it is located now. 

""" 