from timeseries_imports import *


def scaling(df_for_a_symbol):

    min_max_scaler_ = sklearn.preprocessing.MinMaxScaler()

    df_for_a_symbol['open'] = min_max_scaler_.fit_transform(df_for_a_symbol.open.values.reshape(-1,1))
    df_for_a_symbol['close'] = min_max_scaler_.fit_transform(df_for_a_symbol.close.values.reshape(-1,1))
    df_for_a_symbol['high'] = min_max_scaler_.fit_transform(df_for_a_symbol.high.values.reshape(-1,1))
    df_for_a_symbol['low'] = min_max_scaler_.fit_transform(df_for_a_symbol.low.values.reshape(-1,1))

    return df_for_a_symbol


def load_data(df_for_a_symbol, number_timesteps):

    data_nparray_ = df_for_a_symbol.values
    data = []

    for index in range(len(data_nparray_) - number_timesteps):
        data.append(data_nparray_[index: index + number_timesteps])

    data = np.array(data)

    test_set_len = int(np.round(10 / 100 * data.shape[0]))
    train_set_len = data.shape[0] - test_set_len

    x_train = data[:train_set_len, :-1, 1]
    y_train = data[:train_set_len, -1, 1]

    x_test = data[train_set_len:, :-1, 1]
    y_test = data[train_set_len:, -1, 1]

    return x_train, y_train, x_test, y_test