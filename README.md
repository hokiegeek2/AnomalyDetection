# Streaming Time Series Anomaly Detection with Pure Python

Twitter's streaming anomaly detection is easy to use and very powerful, but it's a R library. Although there are other python implementations, all of them contain R dependencies. This library is intended to provide a pure python port that provides the same functions as the original Twitter R implementation.

# Description

The python port of the Twitter streaming time series anomaly detection is a technique for detecting anomalies in seasonal univariate time series where the input is a series of <timestamp, count> pairs.


# Arguments

raw_data: Time series as a two column Series where the first column contains timestamps and the second column contains observations.

max_anoms: Maximum number of anomalies that S-H-ESD will detect as a percentage of the data. Defaults to 0.02

direction: Directionality of the anomalies to be detected. Options are: "pos" | "neg" | "both". Defaults to "both"

alpha: The level of statistical significance with which to accept or reject anomalies. Defaults to 0.05

only_last: Find and report anomalies only within the last day or hr in the time series. None | "day" | "hr". Defaults to None

threshold: Only report positive going anoms above the threshold specified. Options are: None | "med_max" | "p95" | "p99". Defaults to None.

e_value: Add an additional column to the anoms output containing the expected value. Defaults to None

longterm: Increase anom detection efficacy for time series that are greater than a month. Defaults to False

piecewise_median_period_weeks: The piecewise median time window as described in Vallis, Hochenbaum, and Kejariwal (2014). Defaults to 2.

verbose: Enable debug messages. Defaults to False
 
resampling: whether ms or sec granularity should be resampled to min granularity. Defaults to False.
             
period_override: Override the auto-generated period. Defaults to None
                  
multithreaded: whether to use multi-threaded Dask implementation of Series operations. Defaults to False

# Details

	"longterm" This option should be set when the input time series is longer than a month. 
	The option enables the 	approach described in Vallis, Hochenbaum, and Kejariwal (2014).
 
	"threshold" Filter all negative anomalies and those anomalies whose magnitude is smaller than one of the   
	specified thresholds which include: the median of the daily max values (med_max), the 95th percentile 
	of the daily max values (p95), and the 99th percentile of the daily max values (p99).

# References

     Vallis, O., Hochenbaum, J. and Kejariwal, A., (2014) "A Novel
     Technique for Long-Term Anomaly Detection in the Cloud", 6th
     USENIX, Philadelphia, PA.

     Rosner, B., (May 1983), "Percentage Points for a Generalized ESD
     Many-Outlier Procedure" , Technometrics, 25(2), pp. 165-172.


# Examples

Detect all anomalies 
 
`anomaly_detect_ts(raw_data, max_anoms=0.02, direction="both", plot=True)`

Detect only the anomalies in the last day  

`anomaly_detect_ts(raw_data, max_anoms=0.02, direction="both", only_last="day", plot=True)`

Detect only the anomalies in the last hr

`anomaly_detect_ts(raw_data, max_anoms=0.02, direction="both", only_last="hr", plot=True)`

Detect the anomalies in the last hr and resample data of ms or sec granularity

`anomaly_detect_ts(raw_data, max_anoms=0.02, direction="both", only_last="hr", plot=True, resampling=True)`

Detect anomalies in the last day specifying a period of 1440

`anomaly_detect_ts(raw_data, max_anoms=0.02, direction="both", only_last="day", period_override=1440)`
