import csv
import matplotlib.pyplot as plt

def read(filename):
    with open(filename) as f_d:
        reader = csv.reader(f_d, delimiter=',')
        rows = [row for row in reader]
        header = rows.pop(0)

        days = [int(r[0]) for r in rows]
        cases = [int(r[1]) for r in rows]
        deaths = [int(r[2]) for r in rows]

    return header, days, cases, deaths

def plot_cases_vs_death(days, cases, deaths):
    ax = plt.subplot()
    lc = ax.bar(days, cases, color='orange', edgecolor='black', label='Cases')
    ld = ax.bar(days, deaths, color='black', label='Deaths')
    ax.legend([lc, ld], ['Cases', 'Deaths'])

    plt.title('Covid-19 Cases and Deaths')
    plt.xlabel('Days since first reported case')
    plt.ylabel('Daily Reported Cases & Deaths')

    plt.show()

def main():
    import sys
    fn = sys.argv[1]
    _, days, cases, deaths = read(fn)
    plot_cases_vs_death(days, cases, deaths)
    print(f'Cases: {sum(cases)}\tDeaths: {sum(deaths)}')


if __name__ == '__main__':
    main()
