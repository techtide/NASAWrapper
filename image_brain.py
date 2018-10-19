"""
Created by: Arman B (techtide), adapted from teams at Google.
Purpose: Handles and analyses the data. This one is for image classification. It's just a sample that you need to make appropriate with your dataset.
Date: 12/10/2018
"""

from sklearn import svm, metrics
import numpy as np
import matplotlib.pyplot as plt
import data

images = np.array()
targets = np.array()
targets = data.array1

images_and_labels = list(zip(images, targets))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

n_samples = len(images)
data = images.reshape((n_samples, -1))

classifier = svm.SVC(gamma=0.001)

classifier.fit(data[:n_samples // 2], targets[:n_samples // 2])

expected = targets[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(images.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()