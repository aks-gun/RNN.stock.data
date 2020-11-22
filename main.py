from timeseries_imports import *
from timeseries_functions import *
from timeseries_analyze import *
from nn import *


# download_data()
df = pd.read_csv("prices-split-adjusted.csv", index_col = 0)
# analyze_data(df)
# plot_timeseries(df, 'AAPL')

df_for_one_symbol = df[df.symbol == 'AAPL'].copy()
df_for_one_symbol.drop(['symbol'], 1, inplace=True)
df_for_one_symbol.drop(['volume'], 1, inplace=True)

df_for_one_symbol_scaled = df_for_one_symbol.copy()
df_for_one_symbol_scaled = scaling(df_for_one_symbol_scaled)

# analyze_data(df_for_one_symbol_scaled)
# plot_timeseries(df_for_one_symbol_scaled)

number_timesteps = 30
x_train, y_train, x_test, y_test = load_data(df_for_one_symbol_scaled, number_timesteps)
print(x_train.shape)
print(y_train.shape)

model, history = neural_network(x_train, y_train)

model.save('model')

x_train_predictions = model.predict(x_train.reshape(x_train.shape[0], x_train.shape[1], 1))

x_test_predictions = model.predict(x_test.reshape(x_test.shape[0], x_test.shape[1], 1))

print('Testing loss = ', model.evaluate(x_test.reshape(x_test.shape[0], x_test.shape[1], 1), y_test))

test_error = np.abs(x_test_predictions.reshape(x_test_predictions.shape[0],) - y_test)*100

fig, axes = plt.subplots(2,2)
axes[0,0].plot(history.history['loss'], label='loss')
axes[0,0].plot(history.history['val_loss'], label='loss')
axes[1,0].plot(x_train_predictions, label='prediction')
axes[1,0].plot(y_train, label='original')
axes[1,1].plot(x_test_predictions, label='prediction')
axes[1,1].plot(y_test, label='original')
axes[1,1].legend()
axes[0,1].hist(test_error, bins=20)
plt.show()