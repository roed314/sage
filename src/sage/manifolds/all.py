from sage.misc.lazy_import import lazy_import
lazy_import('sage.manifolds.manifold', 'Manifold')
lazy_import('sage.manifolds.differentiable.real_line', 'OpenInterval')
lazy_import('sage.manifolds.differentiable.real_line', 'RealLine')
lazy_import('sage.manifolds.differentiable.euclidean', 'EuclideanSpace')
import sage.manifolds.catalog as manifolds
import sage.manifolds.differentiable.degenerate
import sage.manifolds.differentiable.degenerate_submanifold