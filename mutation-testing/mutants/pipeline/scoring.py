"""
AutoAid Recommender — Scoring & Ranking Module
Dual scoring system: formula-based baseline + Ridge Regression.
Includes cold-start tier interleaving.
"""

import numpy as np
import joblib
import os
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline as SkPipeline

from .features import FEATURE_NAMES, feature_vector_to_array


# ══════════════════════════════════════════════════
# FORMULA-BASED SCORING (always available)
# ══════════════════════════════════════════════════

WEIGHTS = {
    'bayesian_rating': 0.30,
    'distance_score':  0.25,
    'recency_jobs':    0.15,
    'sentiment':       0.15,
    'cancel_score':    0.08,
    'response_score':  0.05,
    'is_online':       0.02,
}
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


def score_formula(features):
    args = [features]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_score_formula__mutmut_orig, x_score_formula__mutmut_mutants, args, kwargs, None)


def x_score_formula__mutmut_orig(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(WEIGHTS[k] * features.get(k, 0) for k in WEIGHTS)


def x_score_formula__mutmut_1(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(None)


def x_score_formula__mutmut_2(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(WEIGHTS[k] / features.get(k, 0) for k in WEIGHTS)


def x_score_formula__mutmut_3(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(WEIGHTS[k] * features.get(None, 0) for k in WEIGHTS)


def x_score_formula__mutmut_4(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(WEIGHTS[k] * features.get(k, None) for k in WEIGHTS)


def x_score_formula__mutmut_5(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(WEIGHTS[k] * features.get(0) for k in WEIGHTS)


def x_score_formula__mutmut_6(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(WEIGHTS[k] * features.get(k, ) for k in WEIGHTS)


def x_score_formula__mutmut_7(features):
    """
    Score a driver using the weighted formula.
    
    Parameters:
        features: dict with 7 feature values
    
    Returns:
        float score (higher = better)
    """
    return sum(WEIGHTS[k] * features.get(k, 1) for k in WEIGHTS)

x_score_formula__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_score_formula__mutmut_1': x_score_formula__mutmut_1, 
    'x_score_formula__mutmut_2': x_score_formula__mutmut_2, 
    'x_score_formula__mutmut_3': x_score_formula__mutmut_3, 
    'x_score_formula__mutmut_4': x_score_formula__mutmut_4, 
    'x_score_formula__mutmut_5': x_score_formula__mutmut_5, 
    'x_score_formula__mutmut_6': x_score_formula__mutmut_6, 
    'x_score_formula__mutmut_7': x_score_formula__mutmut_7
}
x_score_formula__mutmut_orig.__name__ = 'x_score_formula'


# ══════════════════════════════════════════════════
# RIDGE REGRESSION SCORING (when trained)
# ══════════════════════════════════════════════════

class RidgeRanker:
    """Ridge Regression model for driver ranking."""
    
    def __init__(self, model_path=None):
        args = [model_path]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRidgeRankerǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁRidgeRankerǁ__init____mutmut_mutants'), args, kwargs, self)
    
    def xǁRidgeRankerǁ__init____mutmut_orig(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_1(self, model_path=None):
        self.model = ""
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_2(self, model_path=None):
        self.model = None
        self.model_path = None
    
    def xǁRidgeRankerǁ__init____mutmut_3(self, model_path=None):
        self.model = None
        self.model_path = model_path and os.path.join(
            os.path.dirname(__file__), '..', 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_4(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            None, '..', 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_5(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), None, 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_6(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', None, 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_7(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', None, 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_8(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'models', None
        )
    
    def xǁRidgeRankerǁ__init____mutmut_9(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            '..', 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_10(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_11(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_12(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_13(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'models', )
    
    def xǁRidgeRankerǁ__init____mutmut_14(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(None), '..', 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_15(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), 'XX..XX', 'training', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_16(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'XXtrainingXX', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_17(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'TRAINING', 'models', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_18(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'XXmodelsXX', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_19(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'MODELS', 'ridge_ranker.joblib'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_20(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'models', 'XXridge_ranker.joblibXX'
        )
    
    def xǁRidgeRankerǁ__init____mutmut_21(self, model_path=None):
        self.model = None
        self.model_path = model_path or os.path.join(
            os.path.dirname(__file__), '..', 'training', 'models', 'RIDGE_RANKER.JOBLIB'
        )
    
    xǁRidgeRankerǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRidgeRankerǁ__init____mutmut_1': xǁRidgeRankerǁ__init____mutmut_1, 
        'xǁRidgeRankerǁ__init____mutmut_2': xǁRidgeRankerǁ__init____mutmut_2, 
        'xǁRidgeRankerǁ__init____mutmut_3': xǁRidgeRankerǁ__init____mutmut_3, 
        'xǁRidgeRankerǁ__init____mutmut_4': xǁRidgeRankerǁ__init____mutmut_4, 
        'xǁRidgeRankerǁ__init____mutmut_5': xǁRidgeRankerǁ__init____mutmut_5, 
        'xǁRidgeRankerǁ__init____mutmut_6': xǁRidgeRankerǁ__init____mutmut_6, 
        'xǁRidgeRankerǁ__init____mutmut_7': xǁRidgeRankerǁ__init____mutmut_7, 
        'xǁRidgeRankerǁ__init____mutmut_8': xǁRidgeRankerǁ__init____mutmut_8, 
        'xǁRidgeRankerǁ__init____mutmut_9': xǁRidgeRankerǁ__init____mutmut_9, 
        'xǁRidgeRankerǁ__init____mutmut_10': xǁRidgeRankerǁ__init____mutmut_10, 
        'xǁRidgeRankerǁ__init____mutmut_11': xǁRidgeRankerǁ__init____mutmut_11, 
        'xǁRidgeRankerǁ__init____mutmut_12': xǁRidgeRankerǁ__init____mutmut_12, 
        'xǁRidgeRankerǁ__init____mutmut_13': xǁRidgeRankerǁ__init____mutmut_13, 
        'xǁRidgeRankerǁ__init____mutmut_14': xǁRidgeRankerǁ__init____mutmut_14, 
        'xǁRidgeRankerǁ__init____mutmut_15': xǁRidgeRankerǁ__init____mutmut_15, 
        'xǁRidgeRankerǁ__init____mutmut_16': xǁRidgeRankerǁ__init____mutmut_16, 
        'xǁRidgeRankerǁ__init____mutmut_17': xǁRidgeRankerǁ__init____mutmut_17, 
        'xǁRidgeRankerǁ__init____mutmut_18': xǁRidgeRankerǁ__init____mutmut_18, 
        'xǁRidgeRankerǁ__init____mutmut_19': xǁRidgeRankerǁ__init____mutmut_19, 
        'xǁRidgeRankerǁ__init____mutmut_20': xǁRidgeRankerǁ__init____mutmut_20, 
        'xǁRidgeRankerǁ__init____mutmut_21': xǁRidgeRankerǁ__init____mutmut_21
    }
    xǁRidgeRankerǁ__init____mutmut_orig.__name__ = 'xǁRidgeRankerǁ__init__'
    
    def is_trained(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRidgeRankerǁis_trained__mutmut_orig'), object.__getattribute__(self, 'xǁRidgeRankerǁis_trained__mutmut_mutants'), args, kwargs, self)
    
    def xǁRidgeRankerǁis_trained__mutmut_orig(self):
        """Check if a trained model is available."""
        return self.model is not None
    
    def xǁRidgeRankerǁis_trained__mutmut_1(self):
        """Check if a trained model is available."""
        return self.model is None
    
    xǁRidgeRankerǁis_trained__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRidgeRankerǁis_trained__mutmut_1': xǁRidgeRankerǁis_trained__mutmut_1
    }
    xǁRidgeRankerǁis_trained__mutmut_orig.__name__ = 'xǁRidgeRankerǁis_trained'
    
    def train(self, X, y):
        args = [X, y]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRidgeRankerǁtrain__mutmut_orig'), object.__getattribute__(self, 'xǁRidgeRankerǁtrain__mutmut_mutants'), args, kwargs, self)
    
    def xǁRidgeRankerǁtrain__mutmut_orig(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_1(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = None
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_2(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline(None)
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_3(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('XXscalerXX', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_4(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('SCALER', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_5(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('XXridgeXX', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_6(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('RIDGE', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_7(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=None))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_8(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=2.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_9(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(None, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_10(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, None)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_11(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_12(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, )
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_13(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = None
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_14(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['XXridgeXX']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_15(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['RIDGE']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_16(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = None
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_17(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['XXscalerXX']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_18(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['SCALER']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_19(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print(None)
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_20(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("XX\n--- Ridge Regression Learned Weights ---XX")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_21(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- ridge regression learned weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_22(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- RIDGE REGRESSION LEARNED WEIGHTS ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_23(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            None, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_24(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, None, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_25(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, None, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_26(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, None
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_27(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_28(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_29(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_30(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_31(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(None)
        print(f"   {'intercept':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_32(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(None)
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_33(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'XXinterceptXX':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    def xǁRidgeRankerǁtrain__mutmut_34(self, X, y):
        """
        Train Ridge model on feature matrix and labels.
        
        Parameters:
            X: np.ndarray shape (n_samples, 7) — feature vectors
            y: np.ndarray shape (n_samples,) — labels (1.0=hired, 0.0=skipped)
        """
        self.model = SkPipeline([
            ('scaler', StandardScaler()),
            ('ridge', Ridge(alpha=1.0))
        ])
        self.model.fit(X, y)
        
        # Print learned weights
        ridge = self.model.named_steps['ridge']
        scaler = self.model.named_steps['scaler']
        print("\n--- Ridge Regression Learned Weights ---")
        for name, coef, mean, scale in zip(
            FEATURE_NAMES, ridge.coef_, scaler.mean_, scaler.scale_
        ):
            print(f"   {name:20s}: coef={coef:.4f} (mean={mean:.3f}, std={scale:.3f})")
        print(f"   {'INTERCEPT':20s}: {ridge.intercept_:.4f}")
        
        return self
    
    xǁRidgeRankerǁtrain__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRidgeRankerǁtrain__mutmut_1': xǁRidgeRankerǁtrain__mutmut_1, 
        'xǁRidgeRankerǁtrain__mutmut_2': xǁRidgeRankerǁtrain__mutmut_2, 
        'xǁRidgeRankerǁtrain__mutmut_3': xǁRidgeRankerǁtrain__mutmut_3, 
        'xǁRidgeRankerǁtrain__mutmut_4': xǁRidgeRankerǁtrain__mutmut_4, 
        'xǁRidgeRankerǁtrain__mutmut_5': xǁRidgeRankerǁtrain__mutmut_5, 
        'xǁRidgeRankerǁtrain__mutmut_6': xǁRidgeRankerǁtrain__mutmut_6, 
        'xǁRidgeRankerǁtrain__mutmut_7': xǁRidgeRankerǁtrain__mutmut_7, 
        'xǁRidgeRankerǁtrain__mutmut_8': xǁRidgeRankerǁtrain__mutmut_8, 
        'xǁRidgeRankerǁtrain__mutmut_9': xǁRidgeRankerǁtrain__mutmut_9, 
        'xǁRidgeRankerǁtrain__mutmut_10': xǁRidgeRankerǁtrain__mutmut_10, 
        'xǁRidgeRankerǁtrain__mutmut_11': xǁRidgeRankerǁtrain__mutmut_11, 
        'xǁRidgeRankerǁtrain__mutmut_12': xǁRidgeRankerǁtrain__mutmut_12, 
        'xǁRidgeRankerǁtrain__mutmut_13': xǁRidgeRankerǁtrain__mutmut_13, 
        'xǁRidgeRankerǁtrain__mutmut_14': xǁRidgeRankerǁtrain__mutmut_14, 
        'xǁRidgeRankerǁtrain__mutmut_15': xǁRidgeRankerǁtrain__mutmut_15, 
        'xǁRidgeRankerǁtrain__mutmut_16': xǁRidgeRankerǁtrain__mutmut_16, 
        'xǁRidgeRankerǁtrain__mutmut_17': xǁRidgeRankerǁtrain__mutmut_17, 
        'xǁRidgeRankerǁtrain__mutmut_18': xǁRidgeRankerǁtrain__mutmut_18, 
        'xǁRidgeRankerǁtrain__mutmut_19': xǁRidgeRankerǁtrain__mutmut_19, 
        'xǁRidgeRankerǁtrain__mutmut_20': xǁRidgeRankerǁtrain__mutmut_20, 
        'xǁRidgeRankerǁtrain__mutmut_21': xǁRidgeRankerǁtrain__mutmut_21, 
        'xǁRidgeRankerǁtrain__mutmut_22': xǁRidgeRankerǁtrain__mutmut_22, 
        'xǁRidgeRankerǁtrain__mutmut_23': xǁRidgeRankerǁtrain__mutmut_23, 
        'xǁRidgeRankerǁtrain__mutmut_24': xǁRidgeRankerǁtrain__mutmut_24, 
        'xǁRidgeRankerǁtrain__mutmut_25': xǁRidgeRankerǁtrain__mutmut_25, 
        'xǁRidgeRankerǁtrain__mutmut_26': xǁRidgeRankerǁtrain__mutmut_26, 
        'xǁRidgeRankerǁtrain__mutmut_27': xǁRidgeRankerǁtrain__mutmut_27, 
        'xǁRidgeRankerǁtrain__mutmut_28': xǁRidgeRankerǁtrain__mutmut_28, 
        'xǁRidgeRankerǁtrain__mutmut_29': xǁRidgeRankerǁtrain__mutmut_29, 
        'xǁRidgeRankerǁtrain__mutmut_30': xǁRidgeRankerǁtrain__mutmut_30, 
        'xǁRidgeRankerǁtrain__mutmut_31': xǁRidgeRankerǁtrain__mutmut_31, 
        'xǁRidgeRankerǁtrain__mutmut_32': xǁRidgeRankerǁtrain__mutmut_32, 
        'xǁRidgeRankerǁtrain__mutmut_33': xǁRidgeRankerǁtrain__mutmut_33, 
        'xǁRidgeRankerǁtrain__mutmut_34': xǁRidgeRankerǁtrain__mutmut_34
    }
    xǁRidgeRankerǁtrain__mutmut_orig.__name__ = 'xǁRidgeRankerǁtrain'
    
    def predict(self, features_array):
        args = [features_array]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRidgeRankerǁpredict__mutmut_orig'), object.__getattribute__(self, 'xǁRidgeRankerǁpredict__mutmut_mutants'), args, kwargs, self)
    
    def xǁRidgeRankerǁpredict__mutmut_orig(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_1(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_2(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError(None)
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_3(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("XXModel not trained. Call train() or load() first.XX")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_4(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("model not trained. call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_5(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("MODEL NOT TRAINED. CALL TRAIN() OR LOAD() FIRST.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_6(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim != 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_7(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 2:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_8(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = None
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_9(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(None, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_10(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, None)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_11(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(-1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_12(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, )
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_13(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(2, -1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_14(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, +1)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_15(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -2)
        
        return self.model.predict(features_array)
    
    def xǁRidgeRankerǁpredict__mutmut_16(self, features_array):
        """
        Score a single driver.
        
        Parameters:
            features_array: np.ndarray shape (7,) or (n, 7)
        
        Returns:
            float score or np.ndarray of scores
        """
        if not self.is_trained():
            raise RuntimeError("Model not trained. Call train() or load() first.")
        
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
        
        return self.model.predict(None)
    
    xǁRidgeRankerǁpredict__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRidgeRankerǁpredict__mutmut_1': xǁRidgeRankerǁpredict__mutmut_1, 
        'xǁRidgeRankerǁpredict__mutmut_2': xǁRidgeRankerǁpredict__mutmut_2, 
        'xǁRidgeRankerǁpredict__mutmut_3': xǁRidgeRankerǁpredict__mutmut_3, 
        'xǁRidgeRankerǁpredict__mutmut_4': xǁRidgeRankerǁpredict__mutmut_4, 
        'xǁRidgeRankerǁpredict__mutmut_5': xǁRidgeRankerǁpredict__mutmut_5, 
        'xǁRidgeRankerǁpredict__mutmut_6': xǁRidgeRankerǁpredict__mutmut_6, 
        'xǁRidgeRankerǁpredict__mutmut_7': xǁRidgeRankerǁpredict__mutmut_7, 
        'xǁRidgeRankerǁpredict__mutmut_8': xǁRidgeRankerǁpredict__mutmut_8, 
        'xǁRidgeRankerǁpredict__mutmut_9': xǁRidgeRankerǁpredict__mutmut_9, 
        'xǁRidgeRankerǁpredict__mutmut_10': xǁRidgeRankerǁpredict__mutmut_10, 
        'xǁRidgeRankerǁpredict__mutmut_11': xǁRidgeRankerǁpredict__mutmut_11, 
        'xǁRidgeRankerǁpredict__mutmut_12': xǁRidgeRankerǁpredict__mutmut_12, 
        'xǁRidgeRankerǁpredict__mutmut_13': xǁRidgeRankerǁpredict__mutmut_13, 
        'xǁRidgeRankerǁpredict__mutmut_14': xǁRidgeRankerǁpredict__mutmut_14, 
        'xǁRidgeRankerǁpredict__mutmut_15': xǁRidgeRankerǁpredict__mutmut_15, 
        'xǁRidgeRankerǁpredict__mutmut_16': xǁRidgeRankerǁpredict__mutmut_16
    }
    xǁRidgeRankerǁpredict__mutmut_orig.__name__ = 'xǁRidgeRankerǁpredict'
    
    def save(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRidgeRankerǁsave__mutmut_orig'), object.__getattribute__(self, 'xǁRidgeRankerǁsave__mutmut_mutants'), args, kwargs, self)
    
    def xǁRidgeRankerǁsave__mutmut_orig(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_1(self):
        """Save trained model to disk."""
        os.makedirs(None, exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_2(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=None)
        joblib.dump(self.model, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_3(self):
        """Save trained model to disk."""
        os.makedirs(exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_4(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), )
        joblib.dump(self.model, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_5(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(None), exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_6(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=False)
        joblib.dump(self.model, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_7(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(None, self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_8(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, None)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_9(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model_path)
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_10(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, )
        print(f"[SAVED] Ridge model -> {self.model_path}")
    
    def xǁRidgeRankerǁsave__mutmut_11(self):
        """Save trained model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print(None)
    
    xǁRidgeRankerǁsave__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRidgeRankerǁsave__mutmut_1': xǁRidgeRankerǁsave__mutmut_1, 
        'xǁRidgeRankerǁsave__mutmut_2': xǁRidgeRankerǁsave__mutmut_2, 
        'xǁRidgeRankerǁsave__mutmut_3': xǁRidgeRankerǁsave__mutmut_3, 
        'xǁRidgeRankerǁsave__mutmut_4': xǁRidgeRankerǁsave__mutmut_4, 
        'xǁRidgeRankerǁsave__mutmut_5': xǁRidgeRankerǁsave__mutmut_5, 
        'xǁRidgeRankerǁsave__mutmut_6': xǁRidgeRankerǁsave__mutmut_6, 
        'xǁRidgeRankerǁsave__mutmut_7': xǁRidgeRankerǁsave__mutmut_7, 
        'xǁRidgeRankerǁsave__mutmut_8': xǁRidgeRankerǁsave__mutmut_8, 
        'xǁRidgeRankerǁsave__mutmut_9': xǁRidgeRankerǁsave__mutmut_9, 
        'xǁRidgeRankerǁsave__mutmut_10': xǁRidgeRankerǁsave__mutmut_10, 
        'xǁRidgeRankerǁsave__mutmut_11': xǁRidgeRankerǁsave__mutmut_11
    }
    xǁRidgeRankerǁsave__mutmut_orig.__name__ = 'xǁRidgeRankerǁsave'
    
    def load(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRidgeRankerǁload__mutmut_orig'), object.__getattribute__(self, 'xǁRidgeRankerǁload__mutmut_mutants'), args, kwargs, self)
    
    def xǁRidgeRankerǁload__mutmut_orig(self):
        """Load trained model from disk."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"[OK] Ridge model loaded from {self.model_path}")
            return True
        return False
    
    def xǁRidgeRankerǁload__mutmut_1(self):
        """Load trained model from disk."""
        if os.path.exists(None):
            self.model = joblib.load(self.model_path)
            print(f"[OK] Ridge model loaded from {self.model_path}")
            return True
        return False
    
    def xǁRidgeRankerǁload__mutmut_2(self):
        """Load trained model from disk."""
        if os.path.exists(self.model_path):
            self.model = None
            print(f"[OK] Ridge model loaded from {self.model_path}")
            return True
        return False
    
    def xǁRidgeRankerǁload__mutmut_3(self):
        """Load trained model from disk."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(None)
            print(f"[OK] Ridge model loaded from {self.model_path}")
            return True
        return False
    
    def xǁRidgeRankerǁload__mutmut_4(self):
        """Load trained model from disk."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(None)
            return True
        return False
    
    def xǁRidgeRankerǁload__mutmut_5(self):
        """Load trained model from disk."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"[OK] Ridge model loaded from {self.model_path}")
            return False
        return False
    
    def xǁRidgeRankerǁload__mutmut_6(self):
        """Load trained model from disk."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"[OK] Ridge model loaded from {self.model_path}")
            return True
        return True
    
    xǁRidgeRankerǁload__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRidgeRankerǁload__mutmut_1': xǁRidgeRankerǁload__mutmut_1, 
        'xǁRidgeRankerǁload__mutmut_2': xǁRidgeRankerǁload__mutmut_2, 
        'xǁRidgeRankerǁload__mutmut_3': xǁRidgeRankerǁload__mutmut_3, 
        'xǁRidgeRankerǁload__mutmut_4': xǁRidgeRankerǁload__mutmut_4, 
        'xǁRidgeRankerǁload__mutmut_5': xǁRidgeRankerǁload__mutmut_5, 
        'xǁRidgeRankerǁload__mutmut_6': xǁRidgeRankerǁload__mutmut_6
    }
    xǁRidgeRankerǁload__mutmut_orig.__name__ = 'xǁRidgeRankerǁload'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def get_driver_tier(driver):
    args = [driver]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_driver_tier__mutmut_orig, x_get_driver_tier__mutmut_mutants, args, kwargs, None)


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_orig(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_1(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = None
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_2(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get(None, 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_3(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', None)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_4(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get(0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_5(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', )
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_6(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('XXcompleted_jobsXX', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_7(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('COMPLETED_JOBS', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_8(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 1)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_9(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = None
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_10(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get(None, 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_11(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', None)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_12(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get(0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_13(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', )
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_14(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('XXrating_countXX', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_15(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('RATING_COUNT', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_16(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 1)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_17(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 or ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_18(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs != 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_19(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 1 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_20(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings != 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_21(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 1:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_22(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'XXnewXX'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_23(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'NEW'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_24(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 and ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_25(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs <= 5 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_26(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 6 or ratings < 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_27(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings <= 3:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_28(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 4:
        return 'emerging'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_29(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'XXemergingXX'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_30(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'EMERGING'
    else:
        return 'established'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_31(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'XXestablishedXX'


# ══════════════════════════════════════════════════
# COLD-START TIER INTERLEAVING
# ══════════════════════════════════════════════════

def x_get_driver_tier__mutmut_32(driver):
    """
    Categorize driver by data availability.
    
    Returns:
        'new'         — no history at all (cold start)
        'emerging'    — sparse history
        'established' — reliable data
    """
    jobs = driver.get('completed_jobs', 0)
    ratings = driver.get('rating_count', 0)
    
    if jobs == 0 and ratings == 0:
        return 'new'
    elif jobs < 5 or ratings < 3:
        return 'emerging'
    else:
        return 'ESTABLISHED'

x_get_driver_tier__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_driver_tier__mutmut_1': x_get_driver_tier__mutmut_1, 
    'x_get_driver_tier__mutmut_2': x_get_driver_tier__mutmut_2, 
    'x_get_driver_tier__mutmut_3': x_get_driver_tier__mutmut_3, 
    'x_get_driver_tier__mutmut_4': x_get_driver_tier__mutmut_4, 
    'x_get_driver_tier__mutmut_5': x_get_driver_tier__mutmut_5, 
    'x_get_driver_tier__mutmut_6': x_get_driver_tier__mutmut_6, 
    'x_get_driver_tier__mutmut_7': x_get_driver_tier__mutmut_7, 
    'x_get_driver_tier__mutmut_8': x_get_driver_tier__mutmut_8, 
    'x_get_driver_tier__mutmut_9': x_get_driver_tier__mutmut_9, 
    'x_get_driver_tier__mutmut_10': x_get_driver_tier__mutmut_10, 
    'x_get_driver_tier__mutmut_11': x_get_driver_tier__mutmut_11, 
    'x_get_driver_tier__mutmut_12': x_get_driver_tier__mutmut_12, 
    'x_get_driver_tier__mutmut_13': x_get_driver_tier__mutmut_13, 
    'x_get_driver_tier__mutmut_14': x_get_driver_tier__mutmut_14, 
    'x_get_driver_tier__mutmut_15': x_get_driver_tier__mutmut_15, 
    'x_get_driver_tier__mutmut_16': x_get_driver_tier__mutmut_16, 
    'x_get_driver_tier__mutmut_17': x_get_driver_tier__mutmut_17, 
    'x_get_driver_tier__mutmut_18': x_get_driver_tier__mutmut_18, 
    'x_get_driver_tier__mutmut_19': x_get_driver_tier__mutmut_19, 
    'x_get_driver_tier__mutmut_20': x_get_driver_tier__mutmut_20, 
    'x_get_driver_tier__mutmut_21': x_get_driver_tier__mutmut_21, 
    'x_get_driver_tier__mutmut_22': x_get_driver_tier__mutmut_22, 
    'x_get_driver_tier__mutmut_23': x_get_driver_tier__mutmut_23, 
    'x_get_driver_tier__mutmut_24': x_get_driver_tier__mutmut_24, 
    'x_get_driver_tier__mutmut_25': x_get_driver_tier__mutmut_25, 
    'x_get_driver_tier__mutmut_26': x_get_driver_tier__mutmut_26, 
    'x_get_driver_tier__mutmut_27': x_get_driver_tier__mutmut_27, 
    'x_get_driver_tier__mutmut_28': x_get_driver_tier__mutmut_28, 
    'x_get_driver_tier__mutmut_29': x_get_driver_tier__mutmut_29, 
    'x_get_driver_tier__mutmut_30': x_get_driver_tier__mutmut_30, 
    'x_get_driver_tier__mutmut_31': x_get_driver_tier__mutmut_31, 
    'x_get_driver_tier__mutmut_32': x_get_driver_tier__mutmut_32
}
x_get_driver_tier__mutmut_orig.__name__ = 'x_get_driver_tier'


def rank_drivers(drivers, features_list, ridge_model=None, top_n=10):
    args = [drivers, features_list, ridge_model, top_n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_rank_drivers__mutmut_orig, x_rank_drivers__mutmut_mutants, args, kwargs, None)


def x_rank_drivers__mutmut_orig(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_1(drivers, features_list, ridge_model=None, top_n=11):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_2(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = None
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_3(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(None, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_4(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, None):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_5(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_6(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, ):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_7(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model or ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_8(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = None
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_9(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(None)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_10(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = None
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_11(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(None)
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_12(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(None)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_13(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[1])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_14(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = None
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_15(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(None)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_16(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = None
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_17(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(None)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_18(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append(None)
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_19(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = None
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_20(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        None,
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_21(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=None
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_22(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_23(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_24(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t != 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_25(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'XXestablishedXX'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_26(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'ESTABLISHED'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_27(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: None
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_28(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: +x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_29(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[2]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_30(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = None
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_31(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        None,
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_32(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=None
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_33(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_34(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_35(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t != 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_36(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'XXemergingXX'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_37(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'EMERGING'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_38(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: None
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_39(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: +x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_40(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[2]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_41(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = None
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_42(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 - np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_43(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 1.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_44(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(None, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_45(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, None))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_46(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_47(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, ))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_48(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(1, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_49(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 1.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_50(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t != 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_51(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'XXnewXX'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_52(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'NEW'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_53(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = None
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_54(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(None, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_55(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, None)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_56(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_57(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, )
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_58(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n + 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_59(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 3, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_60(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 2)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_61(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = None
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_62(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(None)  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_63(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[1])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_64(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = None
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_65(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(None, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_66(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, None)
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_67(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_68(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, )
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_69(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(1, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_70(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(None)
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_71(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = None
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_72(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n + len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_73(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining >= 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_74(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 1:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_75(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = None
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_76(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get(None) for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_77(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('XXdriver_idXX') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_78(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('DRIVER_ID') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_79(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = None
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_80(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get(None) not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_81(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('XXdriver_idXX') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_82(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('DRIVER_ID') not in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_83(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') in already_ids]
        result.extend(extras[:remaining])
    
    return result[:top_n]


def x_rank_drivers__mutmut_84(drivers, features_list, ridge_model=None, top_n=10):
    """
    Rank drivers with cold-start interleaving.
    
    Strategy:
    - Top 8 slots: best established drivers
    - 1 slot: best emerging driver (gives exposure)
    - 1 slot: random new driver (cold-start injection)
    
    Parameters:
        drivers: list of driver dicts
        features_list: list of feature dicts (parallel to drivers)
        ridge_model: optional RidgeRanker instance
        top_n: number of results to return
    
    Returns:
        list of (driver, score) tuples, ranked
    """
    scored = []
    
    for driver, features in zip(drivers, features_list):
        # Score using Ridge if available, else formula
        if ridge_model and ridge_model.is_trained():
            arr = feature_vector_to_array(features)
            score = float(ridge_model.predict(arr)[0])
        else:
            score = score_formula(features)
        
        tier = get_driver_tier(driver)
        scored.append((driver, score, tier))
    
    # Split by tier
    established = sorted(
        [(d, s) for d, s, t in scored if t == 'established'],
        key=lambda x: -x[1]
    )
    emerging = sorted(
        [(d, s) for d, s, t in scored if t == 'emerging'],
        key=lambda x: -x[1]
    )
    new_drivers = [
        (d, 0.5 + np.random.uniform(0, 0.1))
        for d, s, t in scored if t == 'new'
    ]
    
    # Interleave: mostly established, with exposure slots
    established_slots = max(top_n - 2, 1)
    result = established[:established_slots]
    
    if emerging:
        result.append(emerging[0])  # 1 emerging driver
    if new_drivers:
        # Random new driver for cold-start exploration
        idx = np.random.randint(0, len(new_drivers))
        result.append(new_drivers[idx])
    
    # Fill remaining slots with established if needed
    remaining = top_n - len(result)
    if remaining > 0:
        already_ids = {d.get('driver_id') for d, _ in result}
        extras = [(d, s) for d, s in established if d.get('driver_id') not in already_ids]
        result.extend(None)
    
    return result[:top_n]

x_rank_drivers__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_rank_drivers__mutmut_1': x_rank_drivers__mutmut_1, 
    'x_rank_drivers__mutmut_2': x_rank_drivers__mutmut_2, 
    'x_rank_drivers__mutmut_3': x_rank_drivers__mutmut_3, 
    'x_rank_drivers__mutmut_4': x_rank_drivers__mutmut_4, 
    'x_rank_drivers__mutmut_5': x_rank_drivers__mutmut_5, 
    'x_rank_drivers__mutmut_6': x_rank_drivers__mutmut_6, 
    'x_rank_drivers__mutmut_7': x_rank_drivers__mutmut_7, 
    'x_rank_drivers__mutmut_8': x_rank_drivers__mutmut_8, 
    'x_rank_drivers__mutmut_9': x_rank_drivers__mutmut_9, 
    'x_rank_drivers__mutmut_10': x_rank_drivers__mutmut_10, 
    'x_rank_drivers__mutmut_11': x_rank_drivers__mutmut_11, 
    'x_rank_drivers__mutmut_12': x_rank_drivers__mutmut_12, 
    'x_rank_drivers__mutmut_13': x_rank_drivers__mutmut_13, 
    'x_rank_drivers__mutmut_14': x_rank_drivers__mutmut_14, 
    'x_rank_drivers__mutmut_15': x_rank_drivers__mutmut_15, 
    'x_rank_drivers__mutmut_16': x_rank_drivers__mutmut_16, 
    'x_rank_drivers__mutmut_17': x_rank_drivers__mutmut_17, 
    'x_rank_drivers__mutmut_18': x_rank_drivers__mutmut_18, 
    'x_rank_drivers__mutmut_19': x_rank_drivers__mutmut_19, 
    'x_rank_drivers__mutmut_20': x_rank_drivers__mutmut_20, 
    'x_rank_drivers__mutmut_21': x_rank_drivers__mutmut_21, 
    'x_rank_drivers__mutmut_22': x_rank_drivers__mutmut_22, 
    'x_rank_drivers__mutmut_23': x_rank_drivers__mutmut_23, 
    'x_rank_drivers__mutmut_24': x_rank_drivers__mutmut_24, 
    'x_rank_drivers__mutmut_25': x_rank_drivers__mutmut_25, 
    'x_rank_drivers__mutmut_26': x_rank_drivers__mutmut_26, 
    'x_rank_drivers__mutmut_27': x_rank_drivers__mutmut_27, 
    'x_rank_drivers__mutmut_28': x_rank_drivers__mutmut_28, 
    'x_rank_drivers__mutmut_29': x_rank_drivers__mutmut_29, 
    'x_rank_drivers__mutmut_30': x_rank_drivers__mutmut_30, 
    'x_rank_drivers__mutmut_31': x_rank_drivers__mutmut_31, 
    'x_rank_drivers__mutmut_32': x_rank_drivers__mutmut_32, 
    'x_rank_drivers__mutmut_33': x_rank_drivers__mutmut_33, 
    'x_rank_drivers__mutmut_34': x_rank_drivers__mutmut_34, 
    'x_rank_drivers__mutmut_35': x_rank_drivers__mutmut_35, 
    'x_rank_drivers__mutmut_36': x_rank_drivers__mutmut_36, 
    'x_rank_drivers__mutmut_37': x_rank_drivers__mutmut_37, 
    'x_rank_drivers__mutmut_38': x_rank_drivers__mutmut_38, 
    'x_rank_drivers__mutmut_39': x_rank_drivers__mutmut_39, 
    'x_rank_drivers__mutmut_40': x_rank_drivers__mutmut_40, 
    'x_rank_drivers__mutmut_41': x_rank_drivers__mutmut_41, 
    'x_rank_drivers__mutmut_42': x_rank_drivers__mutmut_42, 
    'x_rank_drivers__mutmut_43': x_rank_drivers__mutmut_43, 
    'x_rank_drivers__mutmut_44': x_rank_drivers__mutmut_44, 
    'x_rank_drivers__mutmut_45': x_rank_drivers__mutmut_45, 
    'x_rank_drivers__mutmut_46': x_rank_drivers__mutmut_46, 
    'x_rank_drivers__mutmut_47': x_rank_drivers__mutmut_47, 
    'x_rank_drivers__mutmut_48': x_rank_drivers__mutmut_48, 
    'x_rank_drivers__mutmut_49': x_rank_drivers__mutmut_49, 
    'x_rank_drivers__mutmut_50': x_rank_drivers__mutmut_50, 
    'x_rank_drivers__mutmut_51': x_rank_drivers__mutmut_51, 
    'x_rank_drivers__mutmut_52': x_rank_drivers__mutmut_52, 
    'x_rank_drivers__mutmut_53': x_rank_drivers__mutmut_53, 
    'x_rank_drivers__mutmut_54': x_rank_drivers__mutmut_54, 
    'x_rank_drivers__mutmut_55': x_rank_drivers__mutmut_55, 
    'x_rank_drivers__mutmut_56': x_rank_drivers__mutmut_56, 
    'x_rank_drivers__mutmut_57': x_rank_drivers__mutmut_57, 
    'x_rank_drivers__mutmut_58': x_rank_drivers__mutmut_58, 
    'x_rank_drivers__mutmut_59': x_rank_drivers__mutmut_59, 
    'x_rank_drivers__mutmut_60': x_rank_drivers__mutmut_60, 
    'x_rank_drivers__mutmut_61': x_rank_drivers__mutmut_61, 
    'x_rank_drivers__mutmut_62': x_rank_drivers__mutmut_62, 
    'x_rank_drivers__mutmut_63': x_rank_drivers__mutmut_63, 
    'x_rank_drivers__mutmut_64': x_rank_drivers__mutmut_64, 
    'x_rank_drivers__mutmut_65': x_rank_drivers__mutmut_65, 
    'x_rank_drivers__mutmut_66': x_rank_drivers__mutmut_66, 
    'x_rank_drivers__mutmut_67': x_rank_drivers__mutmut_67, 
    'x_rank_drivers__mutmut_68': x_rank_drivers__mutmut_68, 
    'x_rank_drivers__mutmut_69': x_rank_drivers__mutmut_69, 
    'x_rank_drivers__mutmut_70': x_rank_drivers__mutmut_70, 
    'x_rank_drivers__mutmut_71': x_rank_drivers__mutmut_71, 
    'x_rank_drivers__mutmut_72': x_rank_drivers__mutmut_72, 
    'x_rank_drivers__mutmut_73': x_rank_drivers__mutmut_73, 
    'x_rank_drivers__mutmut_74': x_rank_drivers__mutmut_74, 
    'x_rank_drivers__mutmut_75': x_rank_drivers__mutmut_75, 
    'x_rank_drivers__mutmut_76': x_rank_drivers__mutmut_76, 
    'x_rank_drivers__mutmut_77': x_rank_drivers__mutmut_77, 
    'x_rank_drivers__mutmut_78': x_rank_drivers__mutmut_78, 
    'x_rank_drivers__mutmut_79': x_rank_drivers__mutmut_79, 
    'x_rank_drivers__mutmut_80': x_rank_drivers__mutmut_80, 
    'x_rank_drivers__mutmut_81': x_rank_drivers__mutmut_81, 
    'x_rank_drivers__mutmut_82': x_rank_drivers__mutmut_82, 
    'x_rank_drivers__mutmut_83': x_rank_drivers__mutmut_83, 
    'x_rank_drivers__mutmut_84': x_rank_drivers__mutmut_84
}
x_rank_drivers__mutmut_orig.__name__ = 'x_rank_drivers'
