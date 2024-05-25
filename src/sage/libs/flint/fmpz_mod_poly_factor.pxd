# distutils: libraries = flint
# distutils: depends = flint/fmpz_mod_poly_factor.h

################################################################################
# This file is auto-generated by the script
#   SAGE_ROOT/src/sage_setup/autogen/flint_autogen.py.
# From the commit 3e2c3a3e091106a25ca9c6fba28e02f2cbcd654a
# Do not modify by hand! Fix and rerun the script instead.
################################################################################

from libc.stdio cimport FILE
from sage.libs.gmp.types cimport *
from sage.libs.mpfr.types cimport *
from sage.libs.flint.types cimport *

cdef extern from "flint_wrap.h":
    void fmpz_mod_poly_factor_init(fmpz_mod_poly_factor_t fac, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_clear(fmpz_mod_poly_factor_t fac, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_realloc(fmpz_mod_poly_factor_t fac, slong alloc, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_fit_length(fmpz_mod_poly_factor_t fac, slong len, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_set(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_factor_t fac, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_print(const fmpz_mod_poly_factor_t fac, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_insert(fmpz_mod_poly_factor_t fac, const fmpz_mod_poly_t poly, slong exp, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_concat(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_factor_t fac, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_pow(fmpz_mod_poly_factor_t fac, slong exp, const fmpz_mod_ctx_t ctx) noexcept
    bint fmpz_mod_poly_is_irreducible(const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    bint fmpz_mod_poly_is_irreducible_ddf(const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    bint fmpz_mod_poly_is_irreducible_rabin(const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    bint fmpz_mod_poly_is_irreducible_rabin_f(fmpz_t r, const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    bint _fmpz_mod_poly_is_squarefree(const fmpz * f, slong len, const fmpz_mod_ctx_t ctx) noexcept
    bint _fmpz_mod_poly_is_squarefree_f(fmpz_t fac, const fmpz * f, slong len, const fmpz_mod_ctx_t ctx) noexcept
    bint fmpz_mod_poly_is_squarefree(const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    bint fmpz_mod_poly_is_squarefree_f(fmpz_t fac, const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    bint fmpz_mod_poly_factor_equal_deg_prob(fmpz_mod_poly_t factor, flint_rand_t state, const fmpz_mod_poly_t pol, slong d, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_equal_deg(fmpz_mod_poly_factor_t factors, const fmpz_mod_poly_t pol, slong d, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_distinct_deg(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_t poly, slong * const * degs, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_distinct_deg_threaded(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_t poly, slong * const * degs, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_squarefree(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_cantor_zassenhaus(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_kaltofen_shoup(fmpz_mod_poly_factor_t res, const fmpz_mod_poly_t poly, const fmpz_mod_ctx_t ctx) noexcept
    void fmpz_mod_poly_factor_berlekamp(fmpz_mod_poly_factor_t factors, const fmpz_mod_poly_t f, const fmpz_mod_ctx_t ctx) noexcept
    void _fmpz_mod_poly_interval_poly_worker(void * arg_ptr) noexcept
    void fmpz_mod_poly_roots(fmpz_mod_poly_factor_t r, const fmpz_mod_poly_t f, int with_multiplicity, const fmpz_mod_ctx_t ctx) noexcept
    int fmpz_mod_poly_roots_factored(fmpz_mod_poly_factor_t r, const fmpz_mod_poly_t f, int with_multiplicity, const fmpz_factor_t n, const fmpz_mod_ctx_t ctx) noexcept
