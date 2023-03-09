def filter_text(text:str) -> tuple[str, list] :
    text_list = []

    text_list = text.split("\n")
    text_list = [t for t in text_list if "1 point" not in t and "5 points" not in t and t!="*"]

    return text_list[0], text_list[1:]



def get_inputs() -> tuple[str,str] :

    form_link = input("\n\nPlease enter the Google form link that you want to scrape : ")
    form_link = form_link.strip()

    output_file = input("Enter the filename of the output docx file : ")

    return form_link, output_file


def sanitize_filename(filename:str) -> str:
    output_file = ""
    splitted_file_name = filename.split(".")

    if "." in filename and splitted_file_name[-1] != "docx" : 
        output_file = splitted_file_name[0] + ".docx"

    elif "." not in filename:
        output_file = filename + ".docx"

    return output_file
