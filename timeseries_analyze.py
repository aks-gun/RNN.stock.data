from timeseries_imports import *


def download_data():
    api = KaggleApi()
    api.authenticate()
    all_competitions = api.competitions_list(category='all')
    for i in range(len(all_competitions)):
        print(all_competitions[i])
    api.dataset_download_files('dgawlik/nyse')
    zf = ZipFile('nyse.zip')
    zf.extractall()
    zf.close()
    print(os.path.dirname(os.getcwd()) + ':', os.listdir(os.path.dirname(os.getcwd())))
    print(os.getcwd() + ':', os.listdir(os.getcwd()))


def analyze_data(df):
    print("Dataframe info:")
    print(df.info())
    print("Dataframe head")
    print(df.head())
    print("Dataframe tail")
    print(df.tail())
    print("Dataframe describe")
    print(df.describe())
    if 'symbol' in df.columns.values:
        print("No. of different stocks = ", len(list(set(df.symbol))))
        print(list(set(df.symbol))[:10])



def plot_timeseries(df, *args):

    if 'volume' in df.columns.values:

        if len(args) == 0:

            plt.subplot(1, 2, 1)
            plt.plot(df.open.values, color='yellow', label='Open')
            plt.plot(df.close.values, color='black', label='Close')
            plt.plot(df.high.values, color='green', label='High')
            plt.plot(df.low.values, color='red', label='Low')

            plt.subplot(1, 2, 2)
            plt.plot(df.volume.values, color='black', label='volume')

            plt.show()

        else:

            for symbol_ in args:

                plt.subplot(1, 2, 1)
                plt.plot(df[df.symbol == symbol_].open.values, color='yellow', label='Open')
                plt.plot(df[df.symbol == symbol_].close.values, color='black', label='Close')
                plt.plot(df[df.symbol == symbol_].high.values, color='green', label='High')
                plt.plot(df[df.symbol == symbol_].low.values, color='red', label='Low')

                plt.subplot(1, 2, 2)
                plt.plot(df[df.symbol == symbol_].volume.values, color='black', label='volume')

                plt.show()

    else:

        if len(args) == 0:

            plt.plot(df.open.values, color='yellow', label='Open')
            plt.plot(df.close.values, color='black', label='Close')
            plt.plot(df.high.values, color='green', label='High')
            plt.plot(df.low.values, color='red', label='Low')
            plt.show()

        else:

            for symbol_ in args:

                plt.plot(df[df.symbol == symbol_].open.values, color='yellow', label='Open')
                plt.plot(df[df.symbol == symbol_].close.values, color='black', label='Close')
                plt.plot(df[df.symbol == symbol_].high.values, color='green', label='High')
                plt.plot(df[df.symbol == symbol_].low.values, color='red', label='Low')
                plt.show()
