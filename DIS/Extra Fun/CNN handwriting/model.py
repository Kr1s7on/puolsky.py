import tensorflow as tf
from tensorflow.keras import datasets, layers, models


def load_and_preprocess_data():
    (train_images, train_labels), (test_images, test_labels) = (
        datasets.mnist.load_data()
    )
    train_images, test_images = train_images / 255.0, test_images / 255.0
    train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
    test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))
    return train_images, train_labels, test_images, test_labels


def build_model():
 

    # Suggested model architecture
    model = models.Sequential(
        [
            layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation="relu"),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dense(10, activation="softmax"),
        ]
    )
    return model


def compile_and_train_model(
    model, train_images, train_labels, test_images, test_labels
):
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )
    model.fit(
        train_images, train_labels, epochs=5, validation_data=(test_images, test_labels)
    )


def save_model(model, filename):
    model.save(filename)


def main():
    train_images, train_labels, test_images, test_labels = load_and_preprocess_data()
    model = build_model()
    compile_and_train_model(model, train_images, train_labels, test_images, test_labels)
    save_model(model, "mnist_cnn.h5")


if __name__ == "__main__":
    main()
