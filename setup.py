from setuptools import setup

setup(
    name="streaming_anomaly_detection",
    packages=["anomaly_detection"],
    version="0.0.3",
    description="A pure python implementation of https://github.com/twitter/AnomalyDetection",
    install_requires=['scipy','pandas','dask','toolz','cloudpickle','statsmodels','asn1crypto']
)
