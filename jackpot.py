import requests
from bs4 import BeautifulSoup
import datetime
import time

number = [0] * 50
star = [0] * 12
key_numbers = [0] * 5
key_stars = [0] * 2
first_year=2004
year=first_year
current_year=int(datetime.datetime.now().year)
print('Going online...')
while year<(current_year + 1):
	#get values form each year
	URL = 'https://www.euro-millions.com/pt/arquivo-de-resultados-{}'.format(year)
	page = requests.get(URL)
	html = page.text
	soup = BeautifulSoup(html, 'html.parser')
	nums = soup.findAll("li", {"class": "new ball"})
	stars= soup.findAll("li", {"class": "new lucky-star"})
	if year==2004:
		time.sleep(0.3)
		print('Connected!')
		time.sleep(0.3)

	#add 1 to index of the number or star
	for b in nums:
		a=int(b.text)
		number[a-1]=number[a-1]+1

	for b in stars:
		a=int(b.text)
		star[a-1]=star[a-1]+1	
	print('Data from ',year,' collected')
	print('')	
	year=year+1
print('')
print('Calculating odds')
time.sleep(1.5)
print('')
#put higher values on final arrays
i=0
while i<5:
	b=number.index(max(number))
	key_numbers[i]= b+1
	number[b]=0
	i=i+1
i=0	
	
while i<2:
	b=star.index(max(star))
	key_stars[i]= b+1
	star[b]=0
	i=i+1
	
print('Done!')
print('')

#sort arrays
key_numbers.sort()
key_stars.sort()


# final prints
print('Most likely numbers to win:')
print (key_numbers)
print('')
print('Most likely stars to win')
print (key_stars)
print('')
print('Complet key')
print('Numbers -',key_numbers[0],':',key_numbers[1],':',key_numbers[2],':',key_numbers[3],':',key_numbers[4],', Stars -',key_stars[0],':',key_stars[1])