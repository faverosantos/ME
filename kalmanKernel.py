
import defines as defines
import numpy as np

#reference: https://thekalmanfilter.com/kalman-filter-python-example/

class kalmanFilter:
    updateNumber = 1
    currentPosition = 0
    currentVelocity = 0
    refreshTime = defines.REFRESH_TIME_MS
    x = [] # state vector vector [[pos],[vel]]
    P = [] # state covariance matrix
    A = [] # state measurement transition matrix for constant linear motion
    H = [] # state measurement transition matrix
    HT = [] # transposed T
    R = 0 # input measurement variance
    Q = [] # inaccuracy in the system model

    def filter(self, curPos, curVel):
        if self.updateNumber == 1:
            self.x = np.array([[curPos], [curVel]])
            self.P = np.array([[5, 0], [0, 5]])
            self.A = np.array([[1, self.refreshTime], [0, 1]])
            self.H = np.array([[1, 0]])
            self.HT = self.H.transpose()
            self.R = 10
            self.Q = np.array([1, 0], [0, 3])

        # Predict State Forward
        x_p = self.A.dot(self.x)
        # Predict Covariance Forward
        P_p = self.A.dot(self.P).dot(self.A.T) + filter.Q
        # Compute Kalman gain
        S = self.H.dot(P_p).dot(self.HT) + self.R
        K = P_p.dot(self.HT)*(1/S)

        # Estimate state
        residual = z - self.H.dot(x_p)
        self.x = x_p + K*residual

        # Estimate covariance
        self.P = P_p - K.dot(self.H).dot(P_p)

        return [self.x[0], self.x[1], self.P]








