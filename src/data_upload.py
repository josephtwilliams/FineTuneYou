import os
import pdfplumber
import json
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)

def create_text_from_pdf(pdf_folder='./', txt_folder='./src/text_files', txt_file_name='resume.txt'):
    for filename in [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]:
        pdf_path = os.path.join(pdf_folder, filename)
        txt_path = os.path.join(txt_folder, txt_file_name)

        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ''.join(page.extract_text() for page in pdf.pages)

            with open(txt_path, 'w') as txt_file:
                txt_file.write(text)
                
            logging.info(f'Successfully created {txt_path} from {pdf_path}')
        except Exception as e:
            logging.error(f'Error in processing {pdf_path}: {e}')

def create_text_from_questions(json_file='./questions.json', txt_folder='./src/text_files', qa_txt_file_name='additional_questions.txt'):
    try:
        with open(json_file, 'r') as file:
            questions_data = json.load(file)
            
            questions = questions_data.get('questions', [])
            qa_pairs = [f"Question: {q['question']}\nAnswer: {q['answer']}\n" for q in questions]
            
            qa_txt_path = os.path.join(txt_folder, qa_txt_file_name)

            with open(qa_txt_path, 'w') as qa_txt_file:
                qa_txt_file.write('\n'.join(qa_pairs))
            
            logging.info(f'Successfully created {qa_txt_path}')
    except Exception as e:
        logging.error(f'Error in processing {json_file}: {e}')

if __name__ == '__main__':
    create_text_from_pdf()
    create_text_from_questions()
