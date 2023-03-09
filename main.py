from scripts import driver
from scripts.utils import get_inputs

form_link, output_file = get_inputs()

driver.scrape(form_link, output_file)