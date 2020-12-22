from filesearch import get_files
from pdf2text import text_converter
import pandas as pd

def _csv_creator(file_pth,
                file_extension,
                save_dir):

    list_of_files = get_files(
        file_pth,
        file_extension)

    text_list = [
        {
            file_path:text_converter(file_path)}  
            for file_path in list_of_files] 

    label_list = []
    text_content_list = []

    for i in range(len(text_list)):
        if 'selected' in list(text_list[i].items())[0][0]:
            label_list.append(1)
        else:
            label_list.append(0)
        text_content_list.append(list(text_list[i].items())[0][1])

    
    df = pd.DataFrame()
    df['content'] = text_content_list
    df['label'] = label_list

    df.to_csv(save_dir,index=False)
    #df.to_csv(,index=False)    

_csv_creator('/home/deeptek4/Projects/code-piece/data/resumes/',
            ".pdf",
            '/home/deeptek4/Projects/code-piece/data/csvs/content.csv')