from scripts.utils import filter_text, sanitize_filename

def test_filter_text():

    sample_text = ['Which of the following elements can be used to customize an application? Select all that apply.\n*\n1 point\nInput widgets\nOutput elements\nReactivity\nLayout']
    question, answers = filter_text(sample_text[0])
    
    assert question == 'Which of the following elements can be used to customize an application? Select all that apply.'
    assert answers == ['Input widgets' , 'Output elements', 'Reactivity', 'Layout']


def test_sanitize_filename_with_no_extension():
    filename = "test"
    assert sanitize_filename(filename) == "test.docx"


def test_sanitize_filename_with_wrong_extension():
    filename = "test.doc"
    assert sanitize_filename(filename) == "test.docx"
