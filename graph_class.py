import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt

class graph:

    l = ["China", "France", "Italy", "South Korea", "Spain", "United States"]

    c  = ["China", "France", "Italy", "South Korea", "Spain", "United States"]

    def totalCases(l,c):
        for i in l:

            data = pd.read_csv("./Countries/" + i + "/COVID-19.csv")
            x = data['Date']
            y = data['Total Case']

            #graph for total COVID-19
            fig0 = plt.figure(0)
            plt.xlabel("Dates (MM/DD/YY)")
            plt.ylabel("Total Cases")
            plt.title("Total COVID-19 Case")
            plt.gca().xaxis.set_major_locator(dates.DayLocator(interval=100))
            plt.gca().yaxis.get_major_formatter().set_scientific(False)
            plt.gca().yaxis.get_major_formatter().set_useOffset(False)
            plt.plot(x,y, label=c[l.index(i)])
            plt.legend(loc="best")
            plt.gcf().autofmt_xdate()
            fig0.savefig("Total Covid Cases.png")

        plt.show()

    def newCases(l,c):
        for i in l:

            data = pd.read_csv("./Countries/" + i + "/COVID-19.csv")
            x = data['Date']
            y = data['New Case']

            #graph for new cases of COVID-19
            fig0 = plt.figure(1)
            plt.xlabel("Dates (MM/DD/YY)")
            plt.ylabel("Cases Per Day")
            plt.title("New COVID-19 Cases per Day")
            plt.gca().xaxis.set_major_locator(dates.DayLocator(interval=100))
            plt.gca().yaxis.get_major_formatter().set_scientific(False)
            plt.gca().yaxis.get_major_formatter().set_useOffset(False)
            plt.plot(x,y, label=c[l.index(i)])
            plt.legend(loc="best")
            plt.gcf().autofmt_xdate()
            fig0.savefig("New Covid Cases.png")

        plt.show()