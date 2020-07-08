#!/usr/bin/env python3

"""
.. module:: covid
    :platforms: Windows, Unix
    :synopsis: Plots the Covid Cases/Deaths for ther UK and Scotland

.. moduleauthor:: Graham Keenan 2020

"""

# Basic imports
import csv
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List, Optional


def read(filename: str) -> Tuple[List[str], List[int], List[int], List[int]]:
    """Reads a CSV file and returnsthe appropriate data in separate lists

    Args:
        filename (str): CSV file to read

    Returns:
        Tuple[
            List[str],
            List[int],
            List[int],
            List[int]
        ]: Header, Days, Cases, and Deaths numbers
    """

    with open(filename) as f_d:
        # Read the csv file
        reader = csv.reader(f_d, delimiter=',')

        # Get each row of data
        rows = [row for row in reader]

        # Split the header off
        header = rows.pop(0)

        # Get the days, cases, and deaths
        days = [int(r[0]) for r in rows]
        cases = [int(r[1]) for r in rows]
        deaths = [int(r[2]) for r in rows]

    return header, days, cases, deaths


def plot_cases_vs_death(
    days: List[int],
    cases: List[int],
    deaths: List[int],
    filename: str,
    avg_days: Optional[int] = 7
):
    """Plots the total number of cases and deaths together with a rolling
    average for each

    Args:
        days (List[int]): Number of days
        cases (List[int]): Cases each day
        deaths (List[int]): Deaths each day
        filename (str): Name of the parsed csv file
        avg_days (Optional[int], optional): Moving average value. Defaults to 7.
    """

    # Load cases and deaths into Dataframes
    cases_df, deaths_df = pd.DataFrame(cases), pd.DataFrame(deaths)

    # Calculate the rolling average fro each
    rolling_cases = cases_df.rolling(window=avg_days).mean()
    rolling_deaths = deaths_df.rolling(window=avg_days).mean()

    # Create a new plot
    ax = plt.subplot()

    # Plot the cases and deaths
    lc = ax.bar(days, cases, color='orange', edgecolor='black', label='Cases')
    ld = ax.bar(days, deaths, color='black', label='Deaths')

    # PLot the rolling average
    ax.plot(rolling_cases, color="black")
    ax.plot(rolling_deaths, color="red")

    # Add a legend for flair
    ax.legend([lc, ld], ['Cases', 'Deaths'])

    # Labels
    plt.title('Covid-19 Cases and Deaths')
    plt.xlabel('Days since first reported case')
    plt.ylabel('Daily Reported Cases & Deaths')

    # Save the image out to disk
    pic = filename.replace('csv', 'png')
    plt.savefig(pic, dpi=300)


def main():
    """Run the program
    """

    import sys

    # Get the CSV filename
    fn = sys.argv[1]

    # Read in the data
    _, days, cases, deaths = read(fn)

    # Plot the data
    plot_cases_vs_death(days, cases, deaths, fn)

    # Total up and print to stdout
    print(f'Cases: {sum(cases)}\tDeaths: {sum(deaths)}')


if __name__ == '__main__':
    main()
