r"""
General extensions of p-adic rings and fields; the base ring may also be an
extension.

These are implemented as proxy parents, backed by an absolute extension.

EXAMPLES:

A trivial extension::

    sage: L.<a> = Qp(2).extension(x)
    sage: L
    2-adic Trivial Extension Field in a defined by x
    sage: a == 0
    True

A trivial extension of a trivial extension::

    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b - a)
    sage: M
    2-adic Trivial Extension Field in b defined by b
    sage: b == a
    True

An unramified extension::

    sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
    sage: L
    2-adic Unramified Extension Field in a defined by x^2 + 2*x + 4
    sage: a^2 + 2*a + 4 == 0
    True
    sage: L.absolute_f()
    2

An unramified extension given by a non-monic defining polynomial (currently, not supported, see #33362)::

    sage: L.<a> = Qp(2).extension(4*x^2 + 2*x + 1)
    Traceback (most recent call last):
    ...
    ValueError: G must be integral
    sage: a^2 + 2*a + 4 == 0  # not tested
    True
    sage: L.absolute_f()
    2

An unramified extension given by a non-integral defining polynomial (currently, not supported, see #33362)::

    sage: L.<a> = Qp(2).extension(x^2 + x/4 + 1/16)
    Traceback (most recent call last):
    ...
    ValueError: G must be integral
    sage: a^2 + 2*a + 4 == 0  # not tested
    True
    sage: L.absolute_f()
    2

A trivial extension of an unramified extension::

    sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b - 2)
    sage: M
    2-adic Trivial Extension Field in b defined by b - 2 over its base field
    sage: M.relative_f()
    1
    sage: M.absolute_f()
    2

An unramified extension of a trivial extension::

    sage: L.<a> = Qp(2).extension(x + 1)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 - b - a)
    sage: M
    2-adic Unramified Extension Field in b defined by b^2 - b + 1
    sage: M.absolute_f()
    2

An unramified extension of an unramified extension::

    sage: L.<a> = Qp(2).extension(x^2 + x + 1)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 + b + a)
    sage: M
    2-adic Unramified Extension Field in b defined by b^2 + b + a over its base field
    sage: M.relative_f()
    2
    sage: M.absolute_f()
    4

::

    sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 + a*b + 4)
    sage: M
    2-adic Unramified Extension Field in b defined by b^2 + a*b + 4 over its base field
    sage: M.relative_f()
    2
    sage: M.absolute_f()
    4

A totally ramified extension not given by an Eisenstein polynomial::

    sage: L.<a> = Qp(2).extension(x^2 + 8)
    sage: L.absolute_e()
    2

A trivial extension of a totally ramified extension::

    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b - a)

A totally ramified extension of a trivial extension::

    sage: L.<a> = Qp(2).extension(x - 2)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 - a)
    sage: M.absolute_e(), M.absolute_f()
    (2, 1)

A totally ramified extension of an unramified extension::

    sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 - 8)  # long time, 1s in early 2022
    sage: M.absolute_e(), M.absolute_f()  # long time
    (2, 2)

An unramified extension of a totally ramified extension::

    sage: L.<a> = Qp(2).extension(x^2 + 8)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 + a*b + a^2)
    sage: M.absolute_e(), M.absolute_f()
    (2, 2)

A totally ramified extension of a totally ramified extension::

    sage: L.<a> = Qp(2).extension(x^2 + 8)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 + 2*a)
    sage: M.absolute_e(), M.absolute_f()
    (4, 1)

A mixed case::

    sage: L.<a> = Qp(2).extension(x^4 + 8*x^2 + 64)
    sage: L.absolute_e(), L.absolute_f()
    (2, 2)

A trivial extension of a mixed extension::

    sage: L.<a> = Qp(2).extension(x^4 + 8*x^2 + 64)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b - a)
    sage: M.absolute_e(), M.absolute_f()
    (2, 2)

An unramified extension of a mixed extension::

    sage: L.<a> = Qp(2).extension(x^4 + 8*x^2 + 64)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 - a^2/8*b - a^2/8)  # long time, 5s in early 2022
    sage: M.absolute_e(), M.absolute_f()  # long time
    (2, 4)

An Eisenstein extension of a mixed extension::

    sage: L.<a> = Qp(2).extension(x^4 + 8*x^2 + 64)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^2 - L.uniformizer())
    sage: M.absolute_e(), M.absolute_f()
    (4, 2)

A mixed extension of a trivial extension::

    sage: L.<a> = Qp(2).extension(x - 2)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(x^4 + 8*x^2 + 64)
    sage: M.absolute_e(), M.absolute_f()
    (2, 2)

A mixed extension of an unramified extension::

    sage: L.<a> = Qp(2).extension(x^2 + x + 1)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^4 + 2*b^2 + 4*a)
    sage: M.absolute_e(), M.absolute_f()

::

    sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(b^4 - a*b^2 - 2*a)
    sage: M.absolute_e(), M.absolute_f()

A mixed extension of an Eisenstein extension::

    sage: L.<a> = Qp(2).extension(x^3 - 2)
    sage: R.<b> = L[]
    sage: M.<b> = L.extension(x^4 + 8*x^2 + 64)
    sage: M.absolute_e(), M.absolute_f()
    (6, 2)

A mixed extension of a mixed extension::

    TODO

A tower of mixed extensions::

    TODO

"""
# ****************************************************************************
#       Copyright (C)      2019 David Roe <roed.math@gmail.com>
#                     2019-2022 Julian Rüth <julian.rueth@fsfe.org>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.functions.other import floor, binomial

from .padic_general_extension_element import pAdicGeneralRingExtensionElement, pAdicGeneralFieldExtensionElement
from .padic_extension_generic import pAdicExtensionGeneric
from sage.rings.ring_extension import RingExtensionWithGen, RingExtension_generic
from sage.rings.ring_extension_conversion import backend_parent
from sage.rings.padics.pow_computer import PowComputer_class
from sage.rings.morphism import RingMap
from sage.categories.homset import Hom


class pAdicGeneralExtension(pAdicExtensionGeneric):
    r"""
    Shared base class for a general extension of a p-adic ring such as a
    relative extension or an extension not given by an unramified polynomial or
    an Eisenstein polynomial.

    EXAMPLES:

        sage: L.<a> = Qp(2).extension(x)

    """
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, element_class, category=None):
        r"""

        TESTS::

            sage: L.<a> = Qp(2).extension(x)
            sage: from sage.rings.padics.padic_general_extension import pAdicGeneralExtension
            sage: isinstance(L, pAdicGeneralExtension)
            True

        """
        base = approx_modulus.base_ring()
        self._exact_modulus = exact_modulus
        self._shift_seed = shift_seed
        self._implementation = 'proxy'
        self._prec_type = base._prec_type
        self.prime_pow = PowComputer_general(base.prime(), cache_limit=0, prec_cap=prec, ram_prec_cap=prec, in_field=base.is_field(), poly=approx_modulus)
        category = category or base.category()

        pAdicExtensionGeneric.__init__(self, exact_modulus, approx_modulus, prec, print_mode, names, element_class, category=category)

        if prec != self.base_ring().precision_cap():
            raise NotImplementedError("cannot change precision in general extension yet")

        if not self._exact_modulus.is_monic():
            raise NotImplementedError(f"defining modulus must be monic but {exact_modulus} is not")

    def relative_e(self):
        r"""
        Return the ramification degree of this ring over its base ring.

        EXAMPLES::

        A trivial extension::

            sage: L.<a> = Qp(2).extension(x + 2)
            sage: L.relative_e()
            1

        An unramified extension::

            sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
            sage: L.relative_e()
            1

        An Eisenstein extension of an Eisenstein extension::

            sage: L.<a> = Zp(2).extension(x^2 - 2)
            sage: R.<b> = L[]
            sage: M.<b> = L.extension(b^3 - a)
            sage: M.relative_e()
            3

        """
        return self.exact_valuation().E()

    def absolute_ring(self, map=False):
        r"""
        Return an absolute extension of the absolute base isomorphic to this
        field.

        Note that this might not be a simple extension. It might be a p-adic
        base ring for a trivial extension or a two step extension, i.e., a
        totally ramified extension given by an Eisenstein polynomial over an
        unramified extension.

        EXAMPLES:

        A trivial extension::

            sage: L.<a> = Qp(2).extension(x + 2)
            sage: L.absolute_ring()
            2-adic Field with capped relative precision 20

        An unramified extension::

            sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
            sage: L.absolute_ring()
            2-adic Unramified Extension Field in a_u defined by x^2 + x + 1

        Optionally, maps from and to the absolute extension are provided::

            sage: M, M_to_L, L_to_M = L.absolute_ring(map=True)
            sage: M_to_L(L_to_M(L.gen())) == L.gen()
            True

        """
        return backend_parent(self, map=map)

    def teichmuller(self, x, prec=None):
        R = self._backend
        x = R(x) if prec is None else R(x, prec)
        return self(R.teichmuller(x))

    def _prec_type(self):
        return self._backend._prec_type()

    def random_element(self, **kwds):
        return self(self._backend.random_element(**kwds))

    def residue_ring(self, n):
        raise NotImplementedError

    @cached_method
    def residue_class_field(self):
        r"""
        Return the residue class field of this ring.

        EXAMPLES::

        A trivial extension::

            sage: L.<a> = Qp(2).extension(x + 2)
            sage: L.residue_class_field()
            Trivial extension of Finite Field of size 2

        A trivial extension of a trivial extension::

            sage: R.<b> = L[]
            sage: M.<b> = L.extension(b - a)
            sage: M.residue_field()
            Trivial extension of Trivial extension of Finite Field of size 2

        An unramified extension::

            sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
            sage: L.residue_class_field()
            Finite Field in z2 of size 2^2 over its base

        A trivial extension of an unramified extension::

            sage: R.<b> = L[]
            sage: M.<b> = L.extension(b - 2)
            sage: M.residue_field()
            Trivial extension of Finite Field in z2 of size 2^2 over its base

        An unramified extension of an unramified extension::

            sage: L.<a> = Qp(2).extension(x^2 + 2*x + 4)
            sage: R.<b> = L[]
            sage: M.<b> = L.extension(b^2 + a*b + 4)
            sage: m = M.residue_field()
            sage: m
            Finite Field in z4 of size 2^4 over its base
            sage: m.base_ring() is L.residue_field()
            True
            sage: m.modulus()
            x^2 + x + z2

        """
        return self.base_ring().residue_class_field().extension(self.relative_f(), absolute=False, implementation="GF", backend=self._backend.residue_class_field())

    def uniformizer(self):
        backend, from_backend, _ = backend_parent(self, map=True)
        return from_backend(backend.uniformizer())

    def uniformizer_pow(self, n):
        backend, from_backend, _ = backend_parent(self, map=True)
        return from_backend(backend.uniformizer_pow(n))

    def _uniformizer_print(self):
        return self._backend._uniformizer_print()

    def gen_unram(self):
        backend, from_backend, _ = backend_parent(self, map=True)
        return from_backend(backend.gen_unram())

    def _unram_print(self):
        return self._backend._unram_print()

    def has_pth_root(self):
        return self._backend.has_pth_root()

    def has_root_of_unity(self, n):
        return self._backend.has_root_of_unity(self, n)

    def construction(self, forbid_frac_field=None):
        # Prefer AlgebraicExtensionFunctor for pushout since FractionField
        # functor often does not work because there is no integer_ring.
        if forbid_frac_field is None:
            forbid_frac_field = True

        # TODO: Change prec of AlgebraicExtensionFunctor
        construction = pAdicExtensionGeneric.construction(self, forbid_frac_field=forbid_frac_field)
        return construction

    def inertia_subring(self):
        r"""
        Return the inertia subring of this extension over its base.

        EXAMPLES:

        The inertia subring of an unramified extension is the ring itself::

            sage: L.<a> = Zp(2).extension(x^2 + 2*x + 4)
            sage: L.inertia_subring() is L
            True

        A trivial extension is added to the inertia subring::

            sage: R.<b> = L[]
            sage: M.<b> = L.extension(b - a)
            sage: M.inertia_subring() is M
            True

        A ramified extension of an unramified extension::

            sage: R.<b> = L[]
            sage: M.<b> = L.extension(b^2 - 2)
            sage: M.inertia_subring() is L
            True

        A general extension. The inertia subring is an extension of the ground
        field::

            sage: L.<a> = Zp(2).extension(x^4 + 8*x^2 + 64)
            sage: M = L.inertia_subring(); M
            2-adic Unramified Extension Ring in a_u defined by x^2 + x + 1
            sage: M.base_ring() is Zp(2)
            True

        """
        if self.relative_e() == 1:
            return self
        if self.relative_f() == 1:
            return self.base_ring()

        backend, from_backend, to_backend = backend_parent(self, map=True)

        backend_inertia_subring = self._backend.inertia_subring()
        inertia_subring_generator = from_backend(backend_inertia_subring.gen())
        inertia_subring = self.base_ring().extension(inertia_subring_generator.minpoly(), names=backend_inertia_subring._unram_print())
        return inertia_subring


class pAdicGeneralRingExtension(pAdicGeneralExtension, RingExtension_generic):
    r"""
    A general extension of a p-adic ring such as a relative extension or an
    extension not given by an unramified polynomial or an Eisenstein
    polynomial.

    This class models rings that are not fields.

    .. SEEALSO:: :class:`pAdicGeneralFieldExtension`

    """
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation='FLINT', category=None):
        base = approx_modulus.base_ring()
        category = category or base.category()

        pAdicGeneralExtension.__init__(self, exact_modulus=exact_modulus, approx_modulus=approx_modulus, prec=prec, print_mode=print_mode, shift_seed=shift_seed, names=names, element_class=pAdicGeneralRingExtensionElement, category=category)

        _, _, to_fraction_field_backend = backend_parent(self.fraction_field(), map=True)

        defining_morphism = pAdicGeneralRingMap_FractionField(self.base_ring(), self.fraction_field()._backend.integer_ring(), to_fraction_field_backend)
        self._backend = defining_morphism.codomain()
        self._prec = self.fraction_field()._prec

        RingExtension_generic.__init__(self, defining_morphism=defining_morphism, import_methods=False, category=category, check=False)

        pAdicGeneralMap_Backend(self.fraction_field(), self).register_as_conversion()

    def is_field(self, *args, **kwds):
        r"""
        Return whether this ring is a field.

        EXAMPLES::

            sage: L.<a> = Zp(2).extension(x + 3)
            sage: L.is_field()
            False

        """
        return False

    def gen(self, i=0):
        r"""
        Return the generator of this ring's fraction field over its base.

        EXAMPLES::
        
            sage: L.<a> = Zp(2).extension(x^2 + 2*x + 4)
            sage: L.gen()
            (a_u + 1)*2 + (a_u + 1)*2^2 + (a_u + 1)*2^3 + (a_u + 1)*2^4 + (a_u + 1)*2^5 + (a_u + 1)*2^6 + (a_u + 1)*2^7 + (a_u + 1)*2^8 + (a_u + 1)*2^9 + (a_u + 1)*2^10 + (a_u + 1)*2^11 + (a_u + 1)*2^12 + (a_u + 1)*2^13 + (a_u + 1)*2^14 + (a_u + 1)*2^15 + (a_u + 1)*2^16 + (a_u + 1)*2^17 + (a_u + 1)*2^18 + (a_u + 1)*2^19 + (a_u + 1)*2^20 + O(2^21)
            sage: L.gen().parent() is L
            True

        """
        return self(self.fraction_field().gen(i))

    def integer_ring(self):
        # TODO: Is this the default implementation anyway?
        return self

    def exact_ring(self):
        # TODO: The naive approach of the base class is typically not correct
        # here anymore.
        raise NotImplementedError

    @cached_method
    def fraction_field(self):
        # TODO: Is this the default implementation anyway?
        return self.construction()[0](self.base_ring().fraction_field())


class pAdicGeneralFieldExtension(pAdicGeneralExtension, RingExtensionWithGen):
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation='FLINT', category=None):
        base = approx_modulus.base_ring()
        category = category or base.category()

        pAdicGeneralExtension.__init__(self, exact_modulus=exact_modulus, approx_modulus=approx_modulus, prec=prec, print_mode=print_mode, shift_seed=shift_seed, names=names, element_class=pAdicGeneralFieldExtensionElement, category=category)

        # TODO: We are currently ignoring implementation.
        defining_morphism, gen = self._create_backend()

        self._backend = gen.parent()

        # Patch prec which was set not knowing the ramification index.
        self._prec = prec * self.relative_e()

        RingExtensionWithGen.__init__(self, defining_morphism=defining_morphism, gen=gen, names=[self.variable_name()], category=category, import_methods=False, check=False)

    degree = RingExtensionWithGen.degree
    # Use the implementation of __reduce__ from the factory and ignore RingExtensionWithGen's override.
    __reduce__ = pAdicGeneralExtension.__reduce__

    def is_field(self, *args, **kwds):
        r"""
        Return whether this ring is a field.

        EXAMPLES::

            sage: L.<a> = Qp(2).extension(x)
            sage: L.is_field()
            True

        """
        return True

    @cached_method
    def integer_ring(self):
        # TODO: Is this the default implementation anyway?
        return self.construction()[0](self.base_ring().integer_ring())

    def fraction_field(self):
        # TODO: Is this the default implementation anyway?
        return self

    def _coerce_map_from_(self, R):
        if isinstance(R, pAdicGeneralRingExtension) and R is self.integer_ring():
            return pAdicGeneralMap_Backend(R, self)
        return RingExtensionWithGen._coerce_map_from_(self, R)

    def _create_backend(self):
        r"""
        Return a backend for this extension, i.e., a p-adic ring that is not a
        general extension itself.
        """
        from sage.misc.misc import walltime
        t0 = walltime()

        if not self._exact_modulus.is_squarefree():
            # We only check squarefreeness here. Irreducibility is checked
            # automatically, when the extensions of the valuations on base to
            # the ring are constructed. (If there is more than one extension,
            # i.e., the polynomial is not irreducible, exact_valuation() is
            # going to complain.)
            raise ValueError("polynomial must be irreducible but %r is not" % self._given_poly)

        p = self.prime()
        K, from_K, to_K = backend_parent(self._base, map=True)
        F = K.ground_ring_of_tower()
        Kex = K.exact_field()
        Ku = K.maximal_unramified_subextension()
        if isinstance(self._base, RingExtension_generic):
            P = self._given_poly.map_coefficients(to_K)
        else:
            P = self._given_poly.change_ring(K)
        Pex = P.change_ring(Kex)
        Lex = Kex.extension(Pex, names='z')
        is_base_unramified = (K.absolute_e() == 1)

        # uniformizer
        t = walltime()
        try:
            val = Lex.valuation(p)
        except ValueError:
            raise ValueError("polynomial must be irreducible but %r is not" % self._given_poly)
        pi = val.uniformizer()
        print("# uniformizer computed in %.3fs" % walltime(t))

        # e and f
        t = walltime()
        e = val.E()
        f = val.F()
        if e*f != self._exact_modulus.degree():
            raise RuntimeError
        print("# ramification index computed in %.3fs [e = %s, f = %s]" % (walltime(t), e, f))

        # Lu and embedding fu : Ku -> Lu
        t = walltime()
        k = Ku.residue_field()
        if f == 1:
            Lu = Ku; l = k
            fu = End(Ku).identity()
        else:
            # Lu
            l = k.extension(ZZ(f), absolute=True)
            Lu = F.extension(l.modulus().change_ring(ZZ).change_ring(F), names='b', absolute=True)
            l = Lu.residue_field()
            # Fu : Ku -> Lu
            if Ku.absolute_f() == 1:
                fu = Lu.coerce_map_from(Ku)
            else:
                U = Ku.modulus().change_ring(Lu)
                U0 = U.change_ring(l)
                a0 = U0.any_root()
                a = U.hensel_lift(Lu(a0).lift_to_precision())
                fu = Ku.hom([a])
        print("# embedding Ku -> Lu computed in %.3fs" % walltime(t))

        # KLu and embedding g : K -> KLu
        t = walltime()
        if is_base_unramified:
            KLu = Lu
            wK = KLu(p)
            g = fu
        else:
            EK = K.defining_polynomial().map_coefficients(fu)
            KLu = Lu.extension(EK, names='wK', absolute=True)
            wK = KLu.uniformizer()
            g = K.hom([wK], base_map=fu)
        print("# embedding K -> KLu computed in %.3fs" % walltime(t))

        if e == 1:
            f = g

        else:

            # minimal polynomial of pi over KLu
            t = walltime()
            S = PolynomialRing(KLu, names='x'); x = S.gen()
            cp = S([ sum(g(Ku(c[i]))*wK**i for i in range(K.absolute_e())) for c in pi.charpoly().list() ])
            if cp.newton_slopes(repetition=False) != [ 1/e ]:
                raise RuntimeError
            S0 = PolynomialRing(l, names='xe'); xe = S0.gen()
            cp0 = S0([ (cp[i*e] >> (f-i)).residue() for i in range(f+1) ])
            roots = cp0.roots()
            if len(roots) < f:
                raise RuntimeError
            mp = x**e - KLu(roots[0][0]).lift_to_precision() * wK
            while True:
                q, r = cp.quo_rem(mp)
                if r == 0: break
                _, _, c = mp.xgcd(q)  # can probably be improved
                mp += (c*cp) % mp
            print("# minimal polynomial of pi over KLu computed in %.3fs" % walltime(t))

            # minimal polynomial of pi over Lu
            t = walltime()
            if is_base_unramified:
                S = PolynomialRing(Lu, names='y')
                E = mp(S.gen())
            else:
                S = PolynomialRing(Lu, names=['x', 'y'])
                (x, y) = S.gens()
                EK = S(EK)
                Q = sum(mp[i].polynomial()*y**i for i in range(e+1))
                E = EK.resultant(Q)
                S = PolynomialRing(Lu, names='y')
                E = S(E)

            d = E.degree()
            for i in range(1,d):
                v = min(ZZ(binomial(j,i)).valuation(p) + E[j].valuation() + (j-i)/d
                        for j in range(i, d+1))
                if i == 1:
                    valder = v
                    slope = 0
                else:
                    s = (valder - v) / (i - 1)
                    if s > slope:
                        slope = s
            val = valder + slope
            coeffs = [ ]
            for i in range(d):
                prec = floor(val - i/d) + 1
                coeffs.append(E[i].add_bigoh(prec).lift_to_precision())
            coeffs.append(Lu.one())
            Ered = S(coeffs)
            print("# minimal polynomial of pi over Lu computed and reduced in %.3fs" % walltime(t))

            # L and embedding f : K -> L
            t = walltime()
            L = Lu.extension(Ered, names='wL')
            if is_base_unramified:
                f = L.coerce_map_from(Lu) * fu
            else:
                E = E.change_ring(L)
                dE = E.derivative()
                wL = L.uniformizer()
                while True:
                    u = E(wL)
                    if u == 0: break
                    v = dE(wL)
                    wL -= u/v
                S = PolynomialRing(L, names='x')
                wK = Q.change_ring(S)(S.gen(), wL).hensel_lift(0)
                f = K.hom([wK], base_map=fu)
            print("# embedding K -> L computed in %.3fs" % walltime(t))

        t = walltime()
        gen = self._given_poly.map_coefficients(f).any_root()
        print("# generator computed in %.3fs" % walltime(t))

        print("# total time: %.3fs" % walltime(t0))
        return f, gen


class PowComputer_general(PowComputer_class):
    pass


class pAdicGeneralMap_Backend(RingMap):
    def _init__(self, domain, codomain):
        # TODO: Use a better category.
        from sage.categories.sets_with_partial_maps import SetsWithPartialMaps

        RingMap.__init__(self, Hom(domain, codomain, SetsWithPartialMaps()))

    def _call_(self, x):
        _, _, to_domain_backend = backend_parent(self.domain(), map=True)
        _, from_codomain_backend, _ = backend_parent(self.codomain(), map=True)
        return from_codomain_backend(to_domain_backend(x))

    def _call_with_args(self, x, args=(), kwds={}):
        return self.codomain()._element_constructor_(self._call_(x), *args, **kwds)


class pAdicGeneralRingMap_FractionField(RingMap):
    def __init__(self, domain, codomain, fraction_field_map):
        self._fraction_field_map = fraction_field_map

        RingMap.__init__(self, Hom(domain, codomain))

    def _call_(self, x):
        x = self.domain().fraction_field()(x)
        y = self._fraction_field_map(x)
        return self.codomain()(y)

    def _call_with_args(self, x, args=(), kwds={}):
        return self.codomain()._element_constructor_(self._call_(x), *args, **kwds)
