# Install chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads

import os  
import argparse

from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'
CHROMEDRIVER_PATH = 'chromedriver.exe'
# WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH

# def save_screenshot(driver: webdriver.Chrome, path: str = '/tmp/screenshot.png') -> None:
#     # Ref: https://stackoverflow.com/a/52572919/
#     original_size = driver.get_window_size()
#     required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#     required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#     driver.set_window_size(required_width, required_height)
#     # driver.save_screenshot(path)  # has scrollbar
#     driver.find_element_by_tag_name('body').screenshot(path)  # avoids scrollbar
#     driver.set_window_size(original_size['width'], original_size['height'])

def make_screenshot(url, output):
    if not url.startswith('http'):
        raise Exception('URLs need to start with "http"')

    driver = webdriver.Chrome(
        options=chrome_options
    )
    driver.get(url)
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    driver.find_element("tag name","body").screenshot(output)
    driver.close()



def main():
    parser = argparse.ArgumentParser(description='Convert problems to md files')
    parser.add_argument('-u', '--url', help='url of the problem', required=True)
    # problem name
    parser.add_argument('-n', '--name', help='problem name', required=True)
    args = parser.parse_args()
    url = args.url
    name = args.name

    screen_loc = os.path.join(name)
    if not os.path.exists(screen_loc):
        os.makedirs(screen_loc)

    sloc = "{}/{}.png".format(name,name)
    make_screenshot(url, sloc)
    create_md_file(url,name)


def create_md_file(url,name):
    # ![image info](./pictures/image.png)

    md_loc = os.path.join(name)
    if not os.path.exists(md_loc):
        os.makedirs(md_loc)
    
    md_file = os.path.join(md_loc, 'readme' + '.md')
    with open(md_file, 'w') as f:
        f.write('### url: {}\n ![{}](./{})'.format(url,name,name+'.png'))
    
    py_file = os.path.join(md_loc, name + '.py')
    with open(py_file, 'w') as f:
        f.write("# {}\n".format(name))
    
if __name__ == '__main__':
    main()
    