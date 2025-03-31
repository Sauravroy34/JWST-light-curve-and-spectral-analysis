from sklearn.linear_model import PoissonRegressor
from sklearn.preprocessing import SplineTransformer
from sklearn.pipeline import make_pipeline
import copy

def smoothend_light_curve(lc,n_knots = 10,degree = 3,alpha = 0.1):
        lightcurve = copy.deepcopy(lc)
        X = lightcurve.time.reshape(-1, 1)
        spline = SplineTransformer(n_knots=n_knots, degree=degree, extrapolation="constant")
        model = make_pipeline(spline, PoissonRegressor(alpha=alpha, max_iter=1000))
        model.fit(X, lightcurve.counts)

        smoothed_counts = model.predict(X)
    
        lightcurve.counts = smoothed_counts
        return lightcurve