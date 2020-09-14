import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from models.linear_model import LinearModel

# load npy data
train_data = np.load('./datasets/linear_train.npy')
test_x = np.load("./datasets/linear_test_x.npy")

# set x-axis, y-axis data
x_data = np.expand_dims(train_data[:, 0], axis=1)
y_data = train_data[:, 1]

# create model
model = LinearModel(num_units=1)

# model compile with binding optimizers and losses
model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
    loss=tf.keras.losses.MSE,
    metrics=[tf.keras.metrics.MeanSquaredError()]
)

# model fitting
model.fit(
    x=x_data,
    y=y_data,
    epochs=10,
    batch_size=32
)

# model predict
prediction = model.predict(x=test_x, batch_size=None)

# set & show plot
plt.scatter(x_data, y_data, s=5, label="train data")
plt.scatter(test_x, prediction, s=5, label="prediction data")
plt.legend()
plt.show()

# summary
model.summary()
