from timeseries_imports import *

def neural_network(x_train, y_train):

    timesteps = int(x_train.shape[1])
    features = 1

    model = Sequential([
        SimpleRNN(128, input_shape = (timesteps, features)),
        # LSTM(128, input_shape=(timesteps,features), return_sequences=True),
        Dropout(0.2),
        # RepeatVector(timesteps),
        # LSTM(128, return_sequences= True),
        # Dropout(0.2),
        Dense(1)
    ])

    model.compile(loss='mse', optimizer='adam')

    print(model.summary())

    es = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
    history=model.fit(
        x_train.reshape(x_train.shape[0], x_train.shape[1], 1), y_train,
        epochs=100,
        batch_size=32,
        validation_split=0.1,
        callbacks=[es],
        shuffle=False
    )

    return model, history



