import csv
from pathlib import Path

out = Path('/Users/tahmina/Documents/Food Save/FoodSave_Synthetic_Survey_Test_Data.csv')
headers = [
    'Record ID (synthetic)',
    'Q1 Purchase interest',
    'Q2 Importance of saving on food',
    'Q4 Rising dining cost impact (1-5)',
    'Q5 Budget strategies (select all; semicolon-separated)',
    'Q6 Satisfaction with current discount options (1-5)',
    'Q7 Monthly dining/takeaway spend',
    'Q8 Bought discounted clearance food before',
    'Q9 Frustration finding affordable, quality meals nearby',
    'Q10 Reasonable surprise-box price per meal',
    'Q11 Early trial/interview willingness (synthetic; no contact details)',
]
rows = [
['TEST-01','yes','Extremely important',5,'Cooking at home more often; Searching for discount vouchers, buy-1-get-1 promo codes, or credit card deals',2,'C. AED 500–1,000','Yes','Good discounts are hard to find nearby, and popular items sell out quickly.','B. AED 15–30','Yes; synthetic interest only'],
['TEST-02','I would consider it','Somewhat important',3,'Ordering only during happy hours or lunchtime specials',3,'B. AED 200–500','Yes','Delivery fees can make an affordable meal expensive.','A. Under AED 15','No; synthetic response'],
['TEST-03','yes','Extremely important',4,'Cooking at home more often; Ordering only during happy hours or lunchtime specials',2,'A. Under AED 200','No','I do not know which places have good-value meals at the end of the day.','A. Under AED 15','Yes; synthetic interest only'],
['TEST-04','I would consider it','Neutral',2,"I don't do anything about it and just pay full price",4,'C. AED 1,000–2,000','Yes','The available offers are not always close to where I am.','B. AED 15–30','No; synthetic response'],
['TEST-05','yes','Somewhat important',4,'Searching for discount vouchers, buy-1-get-1 promo codes, or credit card deals; Ordering only during happy hours or lunchtime specials',3,'C. AED 500–1,000','Yes','It is difficult to compare portion size and quality before ordering.','B. AED 15–30','Yes; synthetic interest only'],
['TEST-06','Definitely not','Not important',1,"I don't do anything about it and just pay full price",4,'E. Over AED 2,000','No','I prefer choosing the exact meal rather than buying surplus food.','C. AED 30–50','No; synthetic response'],
['TEST-07','yes','Extremely important',5,'Cooking at home more often; Searching for discount vouchers, buy-1-get-1 promo codes, or credit card deals; Ordering only during happy hours or lunchtime specials',1,'B. AED 200–500','Yes','Prices change a lot, and there is not enough information about pickup times.','A. Under AED 15','Yes; synthetic interest only'],
['TEST-08','I would consider it','Somewhat important',3,'Searching for discount vouchers, buy-1-get-1 promo codes, or credit card deals',3,'C. AED 1,000–2,000','No','I worry that surprise boxes may include food I cannot eat.','B. AED 15–30','No; synthetic response'],
['TEST-09','yes','Extremely important',4,'Cooking at home more often',2,'C. AED 500–1,000','Yes','There are few affordable options with convenient collection nearby.','B. AED 15–30','Yes; synthetic interest only'],
['TEST-10','I would consider it','Neutral',3,'Ordering only during happy hours or lunchtime specials; Searching for discount vouchers, buy-1-get-1 promo codes, or credit card deals',3,'B. AED 200–500','Yes','The discount is not always clear compared with the regular price.','A. Under AED 15','No; synthetic response'],
['TEST-11','yes','Somewhat important',4,'Cooking at home more often; I don\'t do anything about it and just pay full price',2,'C. AED 1,000–2,000','Yes','I want reliable allergen information and a clear explanation of what is in the box.','B. AED 15–30','Yes; synthetic interest only'],
]
with out.open('w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
readme = Path('/Users/tahmina/Documents/Food Save/FoodSave_Synthetic_Survey_Test_Data_README.txt')
readme.write_text(
    'FoodSave survey synthetic test data\n\n'
    'This file contains 11 invented records for testing or demonstration only. '
    'They are not real respondent answers and must not be represented, submitted, or analyzed as collected survey data. '
    'No responses were entered into the live Google Form.\n\n'
    'The survey numbering skips from question 2 to question 4; no question 3 was visible in the form, so no Q3 column is included. '
    'Q11 answers are synthetic statements and contain no email addresses or contact details. '
    'For multi-select Q5 answers, choices are separated by semicolons.\n', encoding='utf-8')
print(out)
print(readme)
