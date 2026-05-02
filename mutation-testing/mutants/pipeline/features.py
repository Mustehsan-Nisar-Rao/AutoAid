"""
AutoAid Recommender — Feature Engineering Pipeline
Computes the 7-dimensional feature vector for each driver.
"""

import numpy as np
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def haversine(lat1, lon1, lat2, lon2):
    args = [lat1, lon1, lat2, lon2]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_haversine__mutmut_orig, x_haversine__mutmut_mutants, args, kwargs, None)


def x_haversine__mutmut_orig(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_1(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = None
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_2(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6372
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_3(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = None
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_4(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(None)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_5(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 + lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_6(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = None
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_7(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(None)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_8(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 + lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_9(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = None
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_10(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 - cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_11(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) * 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_12(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(None) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_13(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat * 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_14(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 3) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_15(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 3 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_16(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) / sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_17(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) / cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_18(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(None) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_19(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(None)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_20(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(None) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_21(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(None)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_22(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) * 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_23(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(None) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_24(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon * 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_25(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 3) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_26(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 3
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_27(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 / atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_28(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R / 2 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_29(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 3 * atan2(sqrt(a), sqrt(1 - a))


def x_haversine__mutmut_30(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(None, sqrt(1 - a))


def x_haversine__mutmut_31(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), None)


def x_haversine__mutmut_32(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(1 - a))


def x_haversine__mutmut_33(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), )


def x_haversine__mutmut_34(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(None), sqrt(1 - a))


def x_haversine__mutmut_35(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(None))


def x_haversine__mutmut_36(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 + a))


def x_haversine__mutmut_37(lat1, lon1, lat2, lon2):
    """Distance in km between two GPS coordinates."""
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(2 - a))

x_haversine__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_haversine__mutmut_1': x_haversine__mutmut_1, 
    'x_haversine__mutmut_2': x_haversine__mutmut_2, 
    'x_haversine__mutmut_3': x_haversine__mutmut_3, 
    'x_haversine__mutmut_4': x_haversine__mutmut_4, 
    'x_haversine__mutmut_5': x_haversine__mutmut_5, 
    'x_haversine__mutmut_6': x_haversine__mutmut_6, 
    'x_haversine__mutmut_7': x_haversine__mutmut_7, 
    'x_haversine__mutmut_8': x_haversine__mutmut_8, 
    'x_haversine__mutmut_9': x_haversine__mutmut_9, 
    'x_haversine__mutmut_10': x_haversine__mutmut_10, 
    'x_haversine__mutmut_11': x_haversine__mutmut_11, 
    'x_haversine__mutmut_12': x_haversine__mutmut_12, 
    'x_haversine__mutmut_13': x_haversine__mutmut_13, 
    'x_haversine__mutmut_14': x_haversine__mutmut_14, 
    'x_haversine__mutmut_15': x_haversine__mutmut_15, 
    'x_haversine__mutmut_16': x_haversine__mutmut_16, 
    'x_haversine__mutmut_17': x_haversine__mutmut_17, 
    'x_haversine__mutmut_18': x_haversine__mutmut_18, 
    'x_haversine__mutmut_19': x_haversine__mutmut_19, 
    'x_haversine__mutmut_20': x_haversine__mutmut_20, 
    'x_haversine__mutmut_21': x_haversine__mutmut_21, 
    'x_haversine__mutmut_22': x_haversine__mutmut_22, 
    'x_haversine__mutmut_23': x_haversine__mutmut_23, 
    'x_haversine__mutmut_24': x_haversine__mutmut_24, 
    'x_haversine__mutmut_25': x_haversine__mutmut_25, 
    'x_haversine__mutmut_26': x_haversine__mutmut_26, 
    'x_haversine__mutmut_27': x_haversine__mutmut_27, 
    'x_haversine__mutmut_28': x_haversine__mutmut_28, 
    'x_haversine__mutmut_29': x_haversine__mutmut_29, 
    'x_haversine__mutmut_30': x_haversine__mutmut_30, 
    'x_haversine__mutmut_31': x_haversine__mutmut_31, 
    'x_haversine__mutmut_32': x_haversine__mutmut_32, 
    'x_haversine__mutmut_33': x_haversine__mutmut_33, 
    'x_haversine__mutmut_34': x_haversine__mutmut_34, 
    'x_haversine__mutmut_35': x_haversine__mutmut_35, 
    'x_haversine__mutmut_36': x_haversine__mutmut_36, 
    'x_haversine__mutmut_37': x_haversine__mutmut_37
}
x_haversine__mutmut_orig.__name__ = 'x_haversine'


def bayesian_rating(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    args = [avg_rating, rating_count, global_mean, min_ratings]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_bayesian_rating__mutmut_orig, x_bayesian_rating__mutmut_mutants, args, kwargs, None)


def x_bayesian_rating__mutmut_orig(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_1(avg_rating, rating_count, global_mean=5.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_2(avg_rating, rating_count, global_mean=4.0, min_ratings=11):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_3(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = None
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_4(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = None
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_5(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = None
    m = min_ratings
    return (n / (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_6(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = None
    return (n / (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_7(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r - (m / (n + m)) * C


def x_bayesian_rating__mutmut_8(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) / r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_9(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n * (n + m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_10(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n - m)) * r + (m / (n + m)) * C


def x_bayesian_rating__mutmut_11(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m / (n + m)) / C


def x_bayesian_rating__mutmut_12(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m * (n + m)) * C


def x_bayesian_rating__mutmut_13(avg_rating, rating_count, global_mean=4.0, min_ratings=10):
    """
    Confidence-adjusted rating using Bayesian average.
    Pulls sparse ratings toward the global mean.
    
    - A driver with 3 ratings of 5.0 → pulled toward 4.0
    - A driver with 200 ratings of 4.5 → stays near 4.5
    """
    n = rating_count
    r = avg_rating
    C = global_mean
    m = min_ratings
    return (n / (n + m)) * r + (m / (n - m)) * C

x_bayesian_rating__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_bayesian_rating__mutmut_1': x_bayesian_rating__mutmut_1, 
    'x_bayesian_rating__mutmut_2': x_bayesian_rating__mutmut_2, 
    'x_bayesian_rating__mutmut_3': x_bayesian_rating__mutmut_3, 
    'x_bayesian_rating__mutmut_4': x_bayesian_rating__mutmut_4, 
    'x_bayesian_rating__mutmut_5': x_bayesian_rating__mutmut_5, 
    'x_bayesian_rating__mutmut_6': x_bayesian_rating__mutmut_6, 
    'x_bayesian_rating__mutmut_7': x_bayesian_rating__mutmut_7, 
    'x_bayesian_rating__mutmut_8': x_bayesian_rating__mutmut_8, 
    'x_bayesian_rating__mutmut_9': x_bayesian_rating__mutmut_9, 
    'x_bayesian_rating__mutmut_10': x_bayesian_rating__mutmut_10, 
    'x_bayesian_rating__mutmut_11': x_bayesian_rating__mutmut_11, 
    'x_bayesian_rating__mutmut_12': x_bayesian_rating__mutmut_12, 
    'x_bayesian_rating__mutmut_13': x_bayesian_rating__mutmut_13
}
x_bayesian_rating__mutmut_orig.__name__ = 'x_bayesian_rating'


def distance_score(d_km, decay_rate=0.3):
    args = [d_km, decay_rate]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_distance_score__mutmut_orig, x_distance_score__mutmut_mutants, args, kwargs, None)


def x_distance_score__mutmut_orig(d_km, decay_rate=0.3):
    """
    Exponential decay — nearby drivers score high, distant ones fall off.
    
    d=0km  → score=1.0
    d=3km  → score=0.41
    d=10km → score=0.05
    """
    return np.exp(-decay_rate * d_km)


def x_distance_score__mutmut_1(d_km, decay_rate=1.3):
    """
    Exponential decay — nearby drivers score high, distant ones fall off.
    
    d=0km  → score=1.0
    d=3km  → score=0.41
    d=10km → score=0.05
    """
    return np.exp(-decay_rate * d_km)


def x_distance_score__mutmut_2(d_km, decay_rate=0.3):
    """
    Exponential decay — nearby drivers score high, distant ones fall off.
    
    d=0km  → score=1.0
    d=3km  → score=0.41
    d=10km → score=0.05
    """
    return np.exp(None)


def x_distance_score__mutmut_3(d_km, decay_rate=0.3):
    """
    Exponential decay — nearby drivers score high, distant ones fall off.
    
    d=0km  → score=1.0
    d=3km  → score=0.41
    d=10km → score=0.05
    """
    return np.exp(-decay_rate / d_km)


def x_distance_score__mutmut_4(d_km, decay_rate=0.3):
    """
    Exponential decay — nearby drivers score high, distant ones fall off.
    
    d=0km  → score=1.0
    d=3km  → score=0.41
    d=10km → score=0.05
    """
    return np.exp(+decay_rate * d_km)

x_distance_score__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_distance_score__mutmut_1': x_distance_score__mutmut_1, 
    'x_distance_score__mutmut_2': x_distance_score__mutmut_2, 
    'x_distance_score__mutmut_3': x_distance_score__mutmut_3, 
    'x_distance_score__mutmut_4': x_distance_score__mutmut_4
}
x_distance_score__mutmut_orig.__name__ = 'x_distance_score'


def recency_weighted_jobs(job_timestamps, decay_days=90):
    args = [job_timestamps, decay_days]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_recency_weighted_jobs__mutmut_orig, x_recency_weighted_jobs__mutmut_mutants, args, kwargs, None)


def x_recency_weighted_jobs__mutmut_orig(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_1(job_timestamps, decay_days=91):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_2(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_3(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 1.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_4(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = None
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_5(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = None
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_6(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 1.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_7(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = None
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_8(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(None, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_9(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, None)
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_10(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_11(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, )
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_12(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "XX%Y-%m-%d %H:%M:%SXX")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_13(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%y-%m-%d %h:%m:%s")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_14(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%M-%D %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_15(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = None
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_16(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(None, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_17(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, None)
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_18(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime("%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_19(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, )
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_20(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "XX%Y-%m-%dXX")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_21(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_22(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%M-%D")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_23(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    break
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_24(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = None
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_25(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max(None, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_26(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, None)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_27(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max(0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_28(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, )
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_29(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now + ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_30(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 1)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_31(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score = np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_32(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score -= np.exp(-days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_33(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(None)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_34(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago * decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_35(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(+days_ago / decay_days)
    
    return np.log1p(score)


def x_recency_weighted_jobs__mutmut_36(job_timestamps, decay_days=90):
    """
    Recent jobs weighted higher than old ones using exponential decay.
    Log-scaled to prevent dominant outliers.
    
    A driver with 40 jobs last month > a driver with 200 jobs 2 years ago.
    """
    if not job_timestamps:
        return 0.0
    
    now = datetime.now()
    score = 0.0
    for ts in job_timestamps:
        if isinstance(ts, str):
            try:
                ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    ts = datetime.strptime(ts, "%Y-%m-%d")
                except ValueError:
                    continue
        days_ago = max((now - ts).days, 0)
        score += np.exp(-days_ago / decay_days)
    
    return np.log1p(None)

x_recency_weighted_jobs__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_recency_weighted_jobs__mutmut_1': x_recency_weighted_jobs__mutmut_1, 
    'x_recency_weighted_jobs__mutmut_2': x_recency_weighted_jobs__mutmut_2, 
    'x_recency_weighted_jobs__mutmut_3': x_recency_weighted_jobs__mutmut_3, 
    'x_recency_weighted_jobs__mutmut_4': x_recency_weighted_jobs__mutmut_4, 
    'x_recency_weighted_jobs__mutmut_5': x_recency_weighted_jobs__mutmut_5, 
    'x_recency_weighted_jobs__mutmut_6': x_recency_weighted_jobs__mutmut_6, 
    'x_recency_weighted_jobs__mutmut_7': x_recency_weighted_jobs__mutmut_7, 
    'x_recency_weighted_jobs__mutmut_8': x_recency_weighted_jobs__mutmut_8, 
    'x_recency_weighted_jobs__mutmut_9': x_recency_weighted_jobs__mutmut_9, 
    'x_recency_weighted_jobs__mutmut_10': x_recency_weighted_jobs__mutmut_10, 
    'x_recency_weighted_jobs__mutmut_11': x_recency_weighted_jobs__mutmut_11, 
    'x_recency_weighted_jobs__mutmut_12': x_recency_weighted_jobs__mutmut_12, 
    'x_recency_weighted_jobs__mutmut_13': x_recency_weighted_jobs__mutmut_13, 
    'x_recency_weighted_jobs__mutmut_14': x_recency_weighted_jobs__mutmut_14, 
    'x_recency_weighted_jobs__mutmut_15': x_recency_weighted_jobs__mutmut_15, 
    'x_recency_weighted_jobs__mutmut_16': x_recency_weighted_jobs__mutmut_16, 
    'x_recency_weighted_jobs__mutmut_17': x_recency_weighted_jobs__mutmut_17, 
    'x_recency_weighted_jobs__mutmut_18': x_recency_weighted_jobs__mutmut_18, 
    'x_recency_weighted_jobs__mutmut_19': x_recency_weighted_jobs__mutmut_19, 
    'x_recency_weighted_jobs__mutmut_20': x_recency_weighted_jobs__mutmut_20, 
    'x_recency_weighted_jobs__mutmut_21': x_recency_weighted_jobs__mutmut_21, 
    'x_recency_weighted_jobs__mutmut_22': x_recency_weighted_jobs__mutmut_22, 
    'x_recency_weighted_jobs__mutmut_23': x_recency_weighted_jobs__mutmut_23, 
    'x_recency_weighted_jobs__mutmut_24': x_recency_weighted_jobs__mutmut_24, 
    'x_recency_weighted_jobs__mutmut_25': x_recency_weighted_jobs__mutmut_25, 
    'x_recency_weighted_jobs__mutmut_26': x_recency_weighted_jobs__mutmut_26, 
    'x_recency_weighted_jobs__mutmut_27': x_recency_weighted_jobs__mutmut_27, 
    'x_recency_weighted_jobs__mutmut_28': x_recency_weighted_jobs__mutmut_28, 
    'x_recency_weighted_jobs__mutmut_29': x_recency_weighted_jobs__mutmut_29, 
    'x_recency_weighted_jobs__mutmut_30': x_recency_weighted_jobs__mutmut_30, 
    'x_recency_weighted_jobs__mutmut_31': x_recency_weighted_jobs__mutmut_31, 
    'x_recency_weighted_jobs__mutmut_32': x_recency_weighted_jobs__mutmut_32, 
    'x_recency_weighted_jobs__mutmut_33': x_recency_weighted_jobs__mutmut_33, 
    'x_recency_weighted_jobs__mutmut_34': x_recency_weighted_jobs__mutmut_34, 
    'x_recency_weighted_jobs__mutmut_35': x_recency_weighted_jobs__mutmut_35, 
    'x_recency_weighted_jobs__mutmut_36': x_recency_weighted_jobs__mutmut_36
}
x_recency_weighted_jobs__mutmut_orig.__name__ = 'x_recency_weighted_jobs'


def sentiment_with_confidence(raw_sentiment, review_count, max_reviews=20):
    args = [raw_sentiment, review_count, max_reviews]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_sentiment_with_confidence__mutmut_orig, x_sentiment_with_confidence__mutmut_mutants, args, kwargs, None)


def x_sentiment_with_confidence__mutmut_orig(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_1(raw_sentiment, review_count, max_reviews=21):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_2(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = None
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_3(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(None, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_4(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, None)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_5(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_6(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, )
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_7(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count * max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_8(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 2.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_9(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = None
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_10(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 1.5
    return confidence * raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_11(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment - (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_12(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence / raw_sentiment + (1 - confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_13(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 - confidence) / neutral_prior


def x_sentiment_with_confidence__mutmut_14(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (1 + confidence) * neutral_prior


def x_sentiment_with_confidence__mutmut_15(raw_sentiment, review_count, max_reviews=20):
    """
    Blends actual NLP sentiment with a neutral prior based on data confidence.
    
    - 0 reviews → returns 0.5 (neutral)
    - 5 reviews → 75% actual + 25% neutral
    - 20+ reviews → 100% actual sentiment
    """
    confidence = min(review_count / max_reviews, 1.0)
    neutral_prior = 0.5
    return confidence * raw_sentiment + (2 - confidence) * neutral_prior

x_sentiment_with_confidence__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_sentiment_with_confidence__mutmut_1': x_sentiment_with_confidence__mutmut_1, 
    'x_sentiment_with_confidence__mutmut_2': x_sentiment_with_confidence__mutmut_2, 
    'x_sentiment_with_confidence__mutmut_3': x_sentiment_with_confidence__mutmut_3, 
    'x_sentiment_with_confidence__mutmut_4': x_sentiment_with_confidence__mutmut_4, 
    'x_sentiment_with_confidence__mutmut_5': x_sentiment_with_confidence__mutmut_5, 
    'x_sentiment_with_confidence__mutmut_6': x_sentiment_with_confidence__mutmut_6, 
    'x_sentiment_with_confidence__mutmut_7': x_sentiment_with_confidence__mutmut_7, 
    'x_sentiment_with_confidence__mutmut_8': x_sentiment_with_confidence__mutmut_8, 
    'x_sentiment_with_confidence__mutmut_9': x_sentiment_with_confidence__mutmut_9, 
    'x_sentiment_with_confidence__mutmut_10': x_sentiment_with_confidence__mutmut_10, 
    'x_sentiment_with_confidence__mutmut_11': x_sentiment_with_confidence__mutmut_11, 
    'x_sentiment_with_confidence__mutmut_12': x_sentiment_with_confidence__mutmut_12, 
    'x_sentiment_with_confidence__mutmut_13': x_sentiment_with_confidence__mutmut_13, 
    'x_sentiment_with_confidence__mutmut_14': x_sentiment_with_confidence__mutmut_14, 
    'x_sentiment_with_confidence__mutmut_15': x_sentiment_with_confidence__mutmut_15
}
x_sentiment_with_confidence__mutmut_orig.__name__ = 'x_sentiment_with_confidence'


def cancel_score(cancellations, accepted_jobs):
    args = [cancellations, accepted_jobs]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_cancel_score__mutmut_orig, x_cancel_score__mutmut_mutants, args, kwargs, None)


def x_cancel_score__mutmut_orig(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, 1)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_1(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs != 0:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, 1)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_2(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 1:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, 1)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_3(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 2.0
    cancel_rate = cancellations / max(accepted_jobs, 1)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_4(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = None
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_5(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations * max(accepted_jobs, 1)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_6(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(None, 1)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_7(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, None)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_8(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(1)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_9(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, )
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_10(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, 2)
    return 1.0 - cancel_rate


def x_cancel_score__mutmut_11(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, 1)
    return 1.0 + cancel_rate


def x_cancel_score__mutmut_12(cancellations, accepted_jobs):
    """Reliability score: 1.0 = never cancels, 0.0 = always cancels."""
    if accepted_jobs == 0:
        return 1.0
    cancel_rate = cancellations / max(accepted_jobs, 1)
    return 2.0 - cancel_rate

x_cancel_score__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_cancel_score__mutmut_1': x_cancel_score__mutmut_1, 
    'x_cancel_score__mutmut_2': x_cancel_score__mutmut_2, 
    'x_cancel_score__mutmut_3': x_cancel_score__mutmut_3, 
    'x_cancel_score__mutmut_4': x_cancel_score__mutmut_4, 
    'x_cancel_score__mutmut_5': x_cancel_score__mutmut_5, 
    'x_cancel_score__mutmut_6': x_cancel_score__mutmut_6, 
    'x_cancel_score__mutmut_7': x_cancel_score__mutmut_7, 
    'x_cancel_score__mutmut_8': x_cancel_score__mutmut_8, 
    'x_cancel_score__mutmut_9': x_cancel_score__mutmut_9, 
    'x_cancel_score__mutmut_10': x_cancel_score__mutmut_10, 
    'x_cancel_score__mutmut_11': x_cancel_score__mutmut_11, 
    'x_cancel_score__mutmut_12': x_cancel_score__mutmut_12
}
x_cancel_score__mutmut_orig.__name__ = 'x_cancel_score'


def response_score(avg_response_time_min, decay_rate=0.05):
    args = [avg_response_time_min, decay_rate]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_response_score__mutmut_orig, x_response_score__mutmut_mutants, args, kwargs, None)


def x_response_score__mutmut_orig(avg_response_time_min, decay_rate=0.05):
    """
    Exponential decay on response time.
    Fast responders score high.
    
    5 min → 0.78
    15 min → 0.47
    30 min → 0.22
    """
    return np.exp(-decay_rate * avg_response_time_min)


def x_response_score__mutmut_1(avg_response_time_min, decay_rate=1.05):
    """
    Exponential decay on response time.
    Fast responders score high.
    
    5 min → 0.78
    15 min → 0.47
    30 min → 0.22
    """
    return np.exp(-decay_rate * avg_response_time_min)


def x_response_score__mutmut_2(avg_response_time_min, decay_rate=0.05):
    """
    Exponential decay on response time.
    Fast responders score high.
    
    5 min → 0.78
    15 min → 0.47
    30 min → 0.22
    """
    return np.exp(None)


def x_response_score__mutmut_3(avg_response_time_min, decay_rate=0.05):
    """
    Exponential decay on response time.
    Fast responders score high.
    
    5 min → 0.78
    15 min → 0.47
    30 min → 0.22
    """
    return np.exp(-decay_rate / avg_response_time_min)


def x_response_score__mutmut_4(avg_response_time_min, decay_rate=0.05):
    """
    Exponential decay on response time.
    Fast responders score high.
    
    5 min → 0.78
    15 min → 0.47
    30 min → 0.22
    """
    return np.exp(+decay_rate * avg_response_time_min)

x_response_score__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_response_score__mutmut_1': x_response_score__mutmut_1, 
    'x_response_score__mutmut_2': x_response_score__mutmut_2, 
    'x_response_score__mutmut_3': x_response_score__mutmut_3, 
    'x_response_score__mutmut_4': x_response_score__mutmut_4
}
x_response_score__mutmut_orig.__name__ = 'x_response_score'


def build_feature_vector(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    args = [driver, user_lat, user_lon, sentiment_score, review_count]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_build_feature_vector__mutmut_orig, x_build_feature_vector__mutmut_mutants, args, kwargs, None)


def x_build_feature_vector__mutmut_orig(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_1(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = None
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_2(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        None,
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_3(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        None
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_4(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_5(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_6(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get(None, 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_7(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', None),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_8(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get(4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_9(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', ),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_10(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('XXavg_ratingXX', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_11(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('AVG_RATING', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_12(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 5.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_13(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get(None, 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_14(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', None)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_15(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get(0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_16(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', )
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_17(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('XXrating_countXX', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_18(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('RATING_COUNT', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_19(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 1)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_20(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = None
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_21(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(None, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_22(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, None, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_23(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, None, driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_24(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], None)
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_25(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_26(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_27(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_28(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], )
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_29(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['XXlatXX'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_30(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['LAT'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_31(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['XXlonXX'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_32(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['LON'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_33(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = None
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_34(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(None)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_35(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = None
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_36(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get(None, [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_37(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', None)
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_38(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get([])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_39(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', )
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_40(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('XXjob_timestampsXX', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_41(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('JOB_TIMESTAMPS', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_42(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = None
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_43(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(None)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_44(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_45(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = None
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_46(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_47(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 1
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_48(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = None
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_49(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 1.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_50(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = None
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_51(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 1
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_52(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = None
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_53(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(None, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_54(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, None)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_55(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_56(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, )
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_57(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = None
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_58(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        None,
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_59(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        None
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_60(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_61(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_62(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get(None, 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_63(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', None),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_64(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get(0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_65(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', ),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_66(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('XXcancellationsXX', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_67(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('CANCELLATIONS', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_68(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 1),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_69(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get(None, 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_70(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', None)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_71(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get(1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_72(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', )
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_73(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('XXaccepted_jobsXX', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_74(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('ACCEPTED_JOBS', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_75(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 2)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_76(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = None
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_77(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(None)
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_78(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get(None, 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_79(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', None))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_80(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get(30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_81(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', ))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_82(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('XXavg_response_time_minXX', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_83(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('AVG_RESPONSE_TIME_MIN', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_84(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 31))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_85(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = None
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_86(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(None)
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_87(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get(None, False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_88(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', None))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_89(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get(False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_90(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', ))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_91(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('XXis_onlineXX', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_92(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('IS_ONLINE', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_93(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', True))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_94(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'XXbayesian_ratingXX': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_95(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'BAYESIAN_RATING': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_96(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'XXdistance_scoreXX': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_97(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'DISTANCE_SCORE': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_98(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'XXrecency_jobsXX': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_99(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'RECENCY_JOBS': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_100(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'XXsentimentXX': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_101(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'SENTIMENT': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_102(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'XXcancel_scoreXX': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_103(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'CANCEL_SCORE': c_score,
        'response_score': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_104(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'XXresponse_scoreXX': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_105(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'RESPONSE_SCORE': r_score,
        'is_online': is_online,
    }


def x_build_feature_vector__mutmut_106(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'XXis_onlineXX': is_online,
    }


def x_build_feature_vector__mutmut_107(driver, user_lat, user_lon, sentiment_score=None, review_count=None):
    """
    Assembles the complete 7-dimensional feature vector for a driver.
    
    Parameters:
        driver: dict with driver profile data
        user_lat, user_lon: user's current GPS coordinates
        sentiment_score: pre-computed NLP sentiment (0.0-1.0), or None
        review_count: number of reviews, used for confidence weighting
    
    Returns:
        dict with 7 features, all in [0, ~5] range
    """
    # 1. Bayesian Rating
    bay_rating = bayesian_rating(
        driver.get('avg_rating', 4.0),
        driver.get('rating_count', 0)
    )
    
    # 2. Distance Score (exponential decay)
    d_km = haversine(user_lat, user_lon, driver['lat'], driver['lon'])
    dist = distance_score(d_km)
    
    # 3. Recency-Weighted Jobs
    job_ts = driver.get('job_timestamps', [])
    recency = recency_weighted_jobs(job_ts)
    
    # 4. Sentiment with Confidence
    if sentiment_score is not None:
        r_count = review_count if review_count is not None else 0
    else:
        # Default: neutral if no sentiment pre-computed
        sentiment_score = 0.5
        r_count = 0
    sentiment = sentiment_with_confidence(sentiment_score, r_count)
    
    # 5. Cancel Score (reliability)
    c_score = cancel_score(
        driver.get('cancellations', 0),
        driver.get('accepted_jobs', 1)
    )
    
    # 6. Response Score
    r_score = response_score(driver.get('avg_response_time_min', 30))
    
    # 7. Online Status
    is_online = float(driver.get('is_online', False))
    
    return {
        'bayesian_rating': bay_rating,
        'distance_score': dist,
        'recency_jobs': recency,
        'sentiment': sentiment,
        'cancel_score': c_score,
        'response_score': r_score,
        'IS_ONLINE': is_online,
    }

x_build_feature_vector__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_build_feature_vector__mutmut_1': x_build_feature_vector__mutmut_1, 
    'x_build_feature_vector__mutmut_2': x_build_feature_vector__mutmut_2, 
    'x_build_feature_vector__mutmut_3': x_build_feature_vector__mutmut_3, 
    'x_build_feature_vector__mutmut_4': x_build_feature_vector__mutmut_4, 
    'x_build_feature_vector__mutmut_5': x_build_feature_vector__mutmut_5, 
    'x_build_feature_vector__mutmut_6': x_build_feature_vector__mutmut_6, 
    'x_build_feature_vector__mutmut_7': x_build_feature_vector__mutmut_7, 
    'x_build_feature_vector__mutmut_8': x_build_feature_vector__mutmut_8, 
    'x_build_feature_vector__mutmut_9': x_build_feature_vector__mutmut_9, 
    'x_build_feature_vector__mutmut_10': x_build_feature_vector__mutmut_10, 
    'x_build_feature_vector__mutmut_11': x_build_feature_vector__mutmut_11, 
    'x_build_feature_vector__mutmut_12': x_build_feature_vector__mutmut_12, 
    'x_build_feature_vector__mutmut_13': x_build_feature_vector__mutmut_13, 
    'x_build_feature_vector__mutmut_14': x_build_feature_vector__mutmut_14, 
    'x_build_feature_vector__mutmut_15': x_build_feature_vector__mutmut_15, 
    'x_build_feature_vector__mutmut_16': x_build_feature_vector__mutmut_16, 
    'x_build_feature_vector__mutmut_17': x_build_feature_vector__mutmut_17, 
    'x_build_feature_vector__mutmut_18': x_build_feature_vector__mutmut_18, 
    'x_build_feature_vector__mutmut_19': x_build_feature_vector__mutmut_19, 
    'x_build_feature_vector__mutmut_20': x_build_feature_vector__mutmut_20, 
    'x_build_feature_vector__mutmut_21': x_build_feature_vector__mutmut_21, 
    'x_build_feature_vector__mutmut_22': x_build_feature_vector__mutmut_22, 
    'x_build_feature_vector__mutmut_23': x_build_feature_vector__mutmut_23, 
    'x_build_feature_vector__mutmut_24': x_build_feature_vector__mutmut_24, 
    'x_build_feature_vector__mutmut_25': x_build_feature_vector__mutmut_25, 
    'x_build_feature_vector__mutmut_26': x_build_feature_vector__mutmut_26, 
    'x_build_feature_vector__mutmut_27': x_build_feature_vector__mutmut_27, 
    'x_build_feature_vector__mutmut_28': x_build_feature_vector__mutmut_28, 
    'x_build_feature_vector__mutmut_29': x_build_feature_vector__mutmut_29, 
    'x_build_feature_vector__mutmut_30': x_build_feature_vector__mutmut_30, 
    'x_build_feature_vector__mutmut_31': x_build_feature_vector__mutmut_31, 
    'x_build_feature_vector__mutmut_32': x_build_feature_vector__mutmut_32, 
    'x_build_feature_vector__mutmut_33': x_build_feature_vector__mutmut_33, 
    'x_build_feature_vector__mutmut_34': x_build_feature_vector__mutmut_34, 
    'x_build_feature_vector__mutmut_35': x_build_feature_vector__mutmut_35, 
    'x_build_feature_vector__mutmut_36': x_build_feature_vector__mutmut_36, 
    'x_build_feature_vector__mutmut_37': x_build_feature_vector__mutmut_37, 
    'x_build_feature_vector__mutmut_38': x_build_feature_vector__mutmut_38, 
    'x_build_feature_vector__mutmut_39': x_build_feature_vector__mutmut_39, 
    'x_build_feature_vector__mutmut_40': x_build_feature_vector__mutmut_40, 
    'x_build_feature_vector__mutmut_41': x_build_feature_vector__mutmut_41, 
    'x_build_feature_vector__mutmut_42': x_build_feature_vector__mutmut_42, 
    'x_build_feature_vector__mutmut_43': x_build_feature_vector__mutmut_43, 
    'x_build_feature_vector__mutmut_44': x_build_feature_vector__mutmut_44, 
    'x_build_feature_vector__mutmut_45': x_build_feature_vector__mutmut_45, 
    'x_build_feature_vector__mutmut_46': x_build_feature_vector__mutmut_46, 
    'x_build_feature_vector__mutmut_47': x_build_feature_vector__mutmut_47, 
    'x_build_feature_vector__mutmut_48': x_build_feature_vector__mutmut_48, 
    'x_build_feature_vector__mutmut_49': x_build_feature_vector__mutmut_49, 
    'x_build_feature_vector__mutmut_50': x_build_feature_vector__mutmut_50, 
    'x_build_feature_vector__mutmut_51': x_build_feature_vector__mutmut_51, 
    'x_build_feature_vector__mutmut_52': x_build_feature_vector__mutmut_52, 
    'x_build_feature_vector__mutmut_53': x_build_feature_vector__mutmut_53, 
    'x_build_feature_vector__mutmut_54': x_build_feature_vector__mutmut_54, 
    'x_build_feature_vector__mutmut_55': x_build_feature_vector__mutmut_55, 
    'x_build_feature_vector__mutmut_56': x_build_feature_vector__mutmut_56, 
    'x_build_feature_vector__mutmut_57': x_build_feature_vector__mutmut_57, 
    'x_build_feature_vector__mutmut_58': x_build_feature_vector__mutmut_58, 
    'x_build_feature_vector__mutmut_59': x_build_feature_vector__mutmut_59, 
    'x_build_feature_vector__mutmut_60': x_build_feature_vector__mutmut_60, 
    'x_build_feature_vector__mutmut_61': x_build_feature_vector__mutmut_61, 
    'x_build_feature_vector__mutmut_62': x_build_feature_vector__mutmut_62, 
    'x_build_feature_vector__mutmut_63': x_build_feature_vector__mutmut_63, 
    'x_build_feature_vector__mutmut_64': x_build_feature_vector__mutmut_64, 
    'x_build_feature_vector__mutmut_65': x_build_feature_vector__mutmut_65, 
    'x_build_feature_vector__mutmut_66': x_build_feature_vector__mutmut_66, 
    'x_build_feature_vector__mutmut_67': x_build_feature_vector__mutmut_67, 
    'x_build_feature_vector__mutmut_68': x_build_feature_vector__mutmut_68, 
    'x_build_feature_vector__mutmut_69': x_build_feature_vector__mutmut_69, 
    'x_build_feature_vector__mutmut_70': x_build_feature_vector__mutmut_70, 
    'x_build_feature_vector__mutmut_71': x_build_feature_vector__mutmut_71, 
    'x_build_feature_vector__mutmut_72': x_build_feature_vector__mutmut_72, 
    'x_build_feature_vector__mutmut_73': x_build_feature_vector__mutmut_73, 
    'x_build_feature_vector__mutmut_74': x_build_feature_vector__mutmut_74, 
    'x_build_feature_vector__mutmut_75': x_build_feature_vector__mutmut_75, 
    'x_build_feature_vector__mutmut_76': x_build_feature_vector__mutmut_76, 
    'x_build_feature_vector__mutmut_77': x_build_feature_vector__mutmut_77, 
    'x_build_feature_vector__mutmut_78': x_build_feature_vector__mutmut_78, 
    'x_build_feature_vector__mutmut_79': x_build_feature_vector__mutmut_79, 
    'x_build_feature_vector__mutmut_80': x_build_feature_vector__mutmut_80, 
    'x_build_feature_vector__mutmut_81': x_build_feature_vector__mutmut_81, 
    'x_build_feature_vector__mutmut_82': x_build_feature_vector__mutmut_82, 
    'x_build_feature_vector__mutmut_83': x_build_feature_vector__mutmut_83, 
    'x_build_feature_vector__mutmut_84': x_build_feature_vector__mutmut_84, 
    'x_build_feature_vector__mutmut_85': x_build_feature_vector__mutmut_85, 
    'x_build_feature_vector__mutmut_86': x_build_feature_vector__mutmut_86, 
    'x_build_feature_vector__mutmut_87': x_build_feature_vector__mutmut_87, 
    'x_build_feature_vector__mutmut_88': x_build_feature_vector__mutmut_88, 
    'x_build_feature_vector__mutmut_89': x_build_feature_vector__mutmut_89, 
    'x_build_feature_vector__mutmut_90': x_build_feature_vector__mutmut_90, 
    'x_build_feature_vector__mutmut_91': x_build_feature_vector__mutmut_91, 
    'x_build_feature_vector__mutmut_92': x_build_feature_vector__mutmut_92, 
    'x_build_feature_vector__mutmut_93': x_build_feature_vector__mutmut_93, 
    'x_build_feature_vector__mutmut_94': x_build_feature_vector__mutmut_94, 
    'x_build_feature_vector__mutmut_95': x_build_feature_vector__mutmut_95, 
    'x_build_feature_vector__mutmut_96': x_build_feature_vector__mutmut_96, 
    'x_build_feature_vector__mutmut_97': x_build_feature_vector__mutmut_97, 
    'x_build_feature_vector__mutmut_98': x_build_feature_vector__mutmut_98, 
    'x_build_feature_vector__mutmut_99': x_build_feature_vector__mutmut_99, 
    'x_build_feature_vector__mutmut_100': x_build_feature_vector__mutmut_100, 
    'x_build_feature_vector__mutmut_101': x_build_feature_vector__mutmut_101, 
    'x_build_feature_vector__mutmut_102': x_build_feature_vector__mutmut_102, 
    'x_build_feature_vector__mutmut_103': x_build_feature_vector__mutmut_103, 
    'x_build_feature_vector__mutmut_104': x_build_feature_vector__mutmut_104, 
    'x_build_feature_vector__mutmut_105': x_build_feature_vector__mutmut_105, 
    'x_build_feature_vector__mutmut_106': x_build_feature_vector__mutmut_106, 
    'x_build_feature_vector__mutmut_107': x_build_feature_vector__mutmut_107
}
x_build_feature_vector__mutmut_orig.__name__ = 'x_build_feature_vector'


# Feature names in order (used by scoring module)
FEATURE_NAMES = [
    'bayesian_rating', 'distance_score', 'recency_jobs',
    'sentiment', 'cancel_score', 'response_score', 'is_online'
]


def feature_vector_to_array(features):
    args = [features]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_feature_vector_to_array__mutmut_orig, x_feature_vector_to_array__mutmut_mutants, args, kwargs, None)


def x_feature_vector_to_array__mutmut_orig(features):
    """Convert feature dict to numpy array in consistent order."""
    return np.array([features[k] for k in FEATURE_NAMES])


def x_feature_vector_to_array__mutmut_1(features):
    """Convert feature dict to numpy array in consistent order."""
    return np.array(None)

x_feature_vector_to_array__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_feature_vector_to_array__mutmut_1': x_feature_vector_to_array__mutmut_1
}
x_feature_vector_to_array__mutmut_orig.__name__ = 'x_feature_vector_to_array'
