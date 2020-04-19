{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Macierz rozpatrywana\n",
      "[[ 9  8 -2  2 -2]\n",
      " [ 7 -3 -2  7  2]\n",
      " [ 2 -2  2 -7  6]\n",
      " [ 4  8 -3  3 -1]\n",
      " [ 2  2 -1  1  4]]\n",
      "Macierz jest kwadratowa\n",
      "Macierz gorna\n",
      "[[ 9.          8.         -2.          2.         -2.        ]\n",
      " [ 0.         -9.22222222 -0.44444444  5.44444444  3.55555556]\n",
      " [ 0.          0.          2.62650602 -9.6746988   4.98795181]\n",
      " [ 0.          0.          0.         -3.83027523  6.01834862]\n",
      " [ 0.          0.          0.          0.          3.40718563]]\n",
      "Macierz dolna\n",
      "[[ 1.          0.          0.          0.          0.        ]\n",
      " [ 0.77777778  1.          0.          0.          0.        ]\n",
      " [ 0.22222222  0.40963855  1.          0.          0.        ]\n",
      " [ 0.44444444 -0.48192771 -0.8853211   1.          0.        ]\n",
      " [ 0.22222222 -0.02409639 -0.21559633  0.36526946  1.        ]]\n",
      "\n",
      "[[[ 1.          0.          0.          0.          0.        ]\n",
      "  [ 0.          1.          0.          0.          0.        ]\n",
      "  [ 0.          0.          1.          0.          0.        ]\n",
      "  [ 0.          0.          0.          1.          0.        ]\n",
      "  [ 0.          0.          0.          0.          1.        ]]\n",
      "\n",
      " [[ 1.          0.          0.          0.          0.        ]\n",
      "  [ 0.77777778  1.          0.          0.          0.        ]\n",
      "  [ 0.22222222  0.40963855  1.          0.          0.        ]\n",
      "  [ 0.44444444 -0.48192771 -0.8853211   1.          0.        ]\n",
      "  [ 0.22222222 -0.02409639 -0.21559633  0.36526946  1.        ]]\n",
      "\n",
      " [[ 9.          8.         -2.          2.         -2.        ]\n",
      "  [ 0.         -9.22222222 -0.44444444  5.44444444  3.55555556]\n",
      "  [ 0.          0.          2.62650602 -9.6746988   4.98795181]\n",
      "  [ 0.          0.          0.         -3.83027523  6.01834862]\n",
      "  [ 0.          0.          0.          0.          3.40718563]]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import scipy.linalg \n",
    "\n",
    "\n",
    "print(\"Macierz rozpatrywana\")\n",
    "\n",
    "Macierz = np.array([[9,8,-2,2,-2],\n",
    "                    [7,-3,-2,7,2],\n",
    "                    [2,-2,2,-7,6],\n",
    "                    [4,8,-3,3,-1],\n",
    "                    [2,2,-1,1,4]])\n",
    "print(Macierz)\n",
    "\n",
    "if all(len(row) == len(Macierz) for row in Macierz):\n",
    "    print(\"Macierz jest kwadratowa\")\n",
    "\n",
    "    n = len(Macierz)\n",
    "    U = ([[0]*n for x in range (n)])\n",
    "    L = ([[0]*n for x in range (n)])\n",
    "    \n",
    "    for ii in range (n):\n",
    "        U[ii][ii] = 1\n",
    "        for kk in range (ii, n):\n",
    "            suma  = sum([U[jj][kk]*L[ii][jj] for jj in range(ii)])\n",
    "            U[ii][kk] = Macierz[ii][kk] - suma\n",
    "            \n",
    "        for kk in range(ii, n):\n",
    "            if ii == kk:\n",
    "                L[ii][ii] = 1\n",
    "                continue\n",
    "            suma = sum([L[kk][jj]*U[jj][ii] for jj in range(ii)])\n",
    "            L[kk][ii] = (Macierz[kk][ii] -suma)/U[ii][ii]\n",
    "    \n",
    "    print(\"Macierz gorna\")\n",
    "    print(np.array(U))\n",
    "    print(\"Macierz dolna\")\n",
    "    print(np.array(L))\n",
    "    \n",
    "    Macierz_lu =scipy.linalg.lu(Macierz)\n",
    "    \n",
    "    print()\n",
    "    print(np.array(Macierz_lu))\n",
    "\n",
    "else:\n",
    "    (print(\"Macierz nie jest kwadratowa\"))\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
