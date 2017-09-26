import mxnet as mx
import tensorflow as tf
from cnn_clf import CNNClassifier


def main():
    (X_train, y_train), (X_test, y_test) = tf.contrib.keras.datasets.cifar10.load_data()
    X_train = (X_train / 255.0).reshape(-1, 3, 32, 32)
    X_test = (X_test / 255.0).reshape(-1, 3, 32, 32)
    y_train = y_train.ravel()
    y_test = y_test.ravel()

    model = CNNClassifier(mx.cpu(), n_out=10)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    final_acc = (pred == y_test).mean()
    print("final testing accuracy: %.4f" % final_acc)


if __name__ == "__main__":
    main()
