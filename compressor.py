import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import os

def SVD(A):
    U, S, V = np.linalg.svd(A, full_matrices= False)
    return U, S, V

def ColorImageCompresion(path, k):
    image = plt.imread(os.path.join(path))
    red = image[:,:,0]
    green = image[:,:,1]
    blue = image[:, :, 2]
    # SVD for every color
    # red
    Ur, Sr, Vr = SVD(red)
    Ur  = Ur[:, :k]
    Sr = np.diag(Sr[:k])
    Vr = Vr[:k, :]
    reduced_r = Ur @ Sr @ Vr
    # green
    Ug, Sg, Vg = SVD(green)
    Ug = Ug[:, :k]
    Sg = np.diag(Sg[:k])
    Vg = Vg[:k, :]
    reduced_g = Ug @ Sg @ Vg
    # blue
    Ub, Sb, Vb = SVD(blue)
    Ub = Ub[:, :k]
    Sb = np.diag(Sb[:k])
    Vb = Vb[:k, :]
    reduced_b = Ub @ Sb @ Vb
    # join all
    reduced = np.zeros((np.array(image).shape[0], np.array(image).shape[1], 3))
    reduced[:, :, 0] = reduced_r
    reduced[:, :, 1] = reduced_g
    reduced[:, :, 2] = reduced_b
    reduced = np.around(reduced).astype(int)
    plt.imshow(reduced)
def NoColorImageCompresion(path, k):
    X = plt.imread(os.path.join(path))
    A = X.dot([0.299, 0.5870, 0.114])
    U, S, V = SVD(A)
    S = np.diag(S)
    reduced = U[:,:k] @ S[0:k,:k] @ V[:k,:]
    plt.imshow(reduced, cmap='gray')
    plt.axis('off')

def main():
    pass
    # przyklad danych do odkodowania
    #ColorImageCopmresion('sciezka', 10)
    #NoColorImageCompresion('sciezka', 10)

if __name__ == '__main__':
    main()
