from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from tkinter import *

def GenerateStats(qbList, ratingList):
    myUrl = 'https://www.nfl.com/stats/player-stats/category/passing/2022/REG/all/passingpasserrating/desc'
    #open connection to the URL, this grabs the webpage HTML
    uClient = uReq(myUrl)
    pageHtml = uClient.read()
    uClient.close()
    #parses the HTML
    pageSoup = soup(pageHtml, "html.parser") 
    #grabs all stats for the  QBs
    qbStats = pageSoup.findAll("tr")
    #drops the header
    qbStats.pop(0)
    #parses through the HTML to find the name and their rating
    for qb in qbStats:
        pName = qb.td.div.div.a
        name = pName.text
        qbList.append(name)
        pRating = qb.findAll("td", {"class" : "selected"})
        rating = pRating[0].text
        ratingList.append(rating)

def exportData(qbList, ratingList):
    file = "quarterbackRatings.csv"
    f = open (file, "w")
    header = "QuarterbackName, Rating"
    f.write(header + "\n")
    for i in range (len(qbList)): 
        f.write(qbList[i] + ", " +  ratingList[i] + "\n")        

def drawGui(qbList, ratingList):
    root = Tk()
    root.title("NFL Quarterbacks")
    
    #creating widgits
    nameLabel = Label(root, text = "Quarterback Name")
    ratingLabel = Label(root, text = "Rating")
    titleLabel = Label(root, text = "Top 5 quarterbacks this week")
    qb1Label = Label(root, text = qbList[0])
    qb2Label = Label(root, text = qbList[1])
    qb3Label = Label(root, text = qbList[2])
    qb4Label = Label(root, text = qbList[3])
    qb5Label = Label(root, text = qbList[4])
    rt1Label = Label(root, text = ratingList[0])
    rt2Label = Label(root, text = ratingList[1])
    rt3Label = Label(root, text = ratingList[2])
    rt4Label = Label(root, text = ratingList[3])
    rt5Label = Label(root, text = ratingList[4])
    exportDataBtn = Button(root, text = "Export Data to CSV file", padx = 10, pady = 10, command = lambda: exportData(qbList, ratingList))
    
    #putting the widgets on the screen
    nameLabel.grid(row = 0, column = 0)
    titleLabel.grid (row = 1, column  = 1)
    ratingLabel.grid(row = 0, column = 2)
    qb1Label.grid(row = 2, column = 0)
    qb2Label.grid(row = 3, column = 0)
    qb3Label.grid(row = 4, column = 0)
    qb4Label.grid(row = 5, column = 0)
    qb5Label.grid(row = 6, column = 0)
    rt1Label.grid(row = 2, column = 2)    
    rt2Label.grid(row = 3, column = 2)
    rt3Label.grid(row = 4, column = 2)
    rt4Label.grid(row = 5, column = 2)
    rt5Label.grid(row = 6, column = 2)
    exportDataBtn.grid(row = 7, column = 1)

    root.mainloop()


def main():
    qbList = []
    ratingList = []
    GenerateStats(qbList, ratingList)
    drawGui(qbList, ratingList)

main()


