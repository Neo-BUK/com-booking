from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

def getReviewCount(squirrel):

    dataElement = squirrel.driver.find_elements(By.XPATH, "//a[@id='show_reviews_tab']/span")
    
    if len(dataElement) == 1:
        if len(dataElement[0].text) != 0:
            inText = dataElement[0].text;
            inIntStr = '';
            
            '''
            inIntStr = '';
            for char in inText:
                if char.isdigit() == True:
                    inIntStr = inIntStr + char
            '''
            
            arrayIntStr = re.findall('\d+',inText);
            if len(arrayIntStr) == 0:
                inIntStr = 0;
            else:
                inIntStr = int(arrayIntStr[0]);
                
            #countReview = int(inIntStr);
            return inIntStr;
        else:
            return 0;
        
    else:
        return None; 