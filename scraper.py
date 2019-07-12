# Import all the required modules 
import bs4 as bs
import lxml
import urllib.request
import csv
import os

# Scraping the website data
raw = urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html').read()
scode = bs.BeautifulSoup(raw,'lxml')

# Listing of all the links in the website 
x = list()
for link in scode.find_all('a'):
	x.append(link.get('href'))

# Parsing and storing the link data from each link
for i in x:	
	#print(i)
	rowlist = list()
	temp = urllib.request.urlopen('https://karki23.github.io/Weather-Data/' + i).read()
	tempcode = bs.BeautifulSoup(temp,'lxml')
	tabledata = tempcode.find_all('table')
	for row in tabledata:
		tblrow = row.find_all('tr') 
		#print(tblrow)
		for data in tblrow:
			tbldata = data.find_all('td')
			#print(tbldata)
			rowdata = [i.text for i in tbldata]
			#print('\n')
			rowlist.append(rowdata)
			#print(rowlist)

	# Reading the table header
	tblhdr = row.find_all('th')
	headerdata = [i.text for i in tblhdr]
	#print(headerdata)
	
	# Changing output directory (below path is used from my local system)
	os.chdir("C:/Users/raveendra/Documents/GitHub/pesuio_final_assignment/dataset/")
	
	# Writing output to csv files
	with open('temp.csv', 'w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerow(headerdata)
		
	with open('temp.csv', 'a') as writeFile:	
		for j in rowlist:
			writer = csv.writer(writeFile)
			writer.writerow(j)
			
	# Removing the extra blank rows
	with open('temp.csv') as input, open(i.rstrip('.html') + 'final.csv', 'w') as output:
		non_blank = (line for line in input if line.strip())
		output.writelines(non_blank)
	
os.remove("temp.csv") 
print("'temp.csv' File Removed!")

	