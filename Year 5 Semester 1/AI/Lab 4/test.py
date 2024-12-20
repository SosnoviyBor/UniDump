import pickle
import numpy as np


def test(test_images, test_labels):
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    test_loss, test_acc = model.evaluate(test_images, test_labels)

    print(f"Test accuracy: {round(test_acc, 4)}")
    print(f"Test loss: {round(test_loss, 4)}")


    predictions = model.predict(test_images)

    predicted_labels = np.argmax(predictions, axis=1)
    true_labels = np.argmax(test_labels, axis=1)

    num_classes = 10
    TP = np.zeros(num_classes)
    TN = np.zeros(num_classes)
    FP = np.zeros(num_classes)
    FN = np.zeros(num_classes)

    for i in range(num_classes):
        TP[i] = np.sum((predicted_labels == i) & (true_labels == i))
        TN[i] = np.sum((predicted_labels != i) & (true_labels != i))
        FP[i] = np.sum((predicted_labels == i) & (true_labels != i))
        FN[i] = np.sum((predicted_labels != i) & (true_labels == i))

    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(num_classes):
        tp += TP[i]
        tn += TN[i]
        fp += FP[i]
        fn += FN[i]
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * 1 / (1 / precision + 1 / recall)
    
    print(f"F1: {round(f1, 4)}")
