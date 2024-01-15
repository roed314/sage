# Deprecated header file; use sage/libs/flint/acb_poly.pxd instead
# See https://github.com/sagemath/sage/pull/36449

from sage.libs.flint.types cimport acb_poly_struct, acb_poly_t

from sage.libs.flint.acb_poly cimport (
    acb_poly_init,
    acb_poly_clear,
    acb_poly_fit_length,
    _acb_poly_set_length,
    _acb_poly_normalise,
    acb_poly_swap,
    acb_poly_length,
    acb_poly_degree,
    acb_poly_is_zero,
    acb_poly_is_one,
    acb_poly_is_x,
    acb_poly_zero,
    acb_poly_one,
    acb_poly_set,
    acb_poly_set_round,
    acb_poly_set_coeff_si,
    acb_poly_set_coeff_acb,
    acb_poly_get_coeff_acb,
    acb_poly_get_coeff_ptr,
    _acb_poly_shift_right,
    acb_poly_shift_right,
    _acb_poly_shift_left,
    acb_poly_shift_left,
    acb_poly_truncate,
    acb_poly_printd,
    acb_poly_fprintd,
    acb_poly_randtest,
    acb_poly_equal,
    acb_poly_contains,
    acb_poly_contains_fmpz_poly,
    acb_poly_contains_fmpq_poly,
    _acb_poly_overlaps,
    acb_poly_overlaps,
    acb_poly_get_unique_fmpz_poly,
    acb_poly_is_real,
    acb_poly_set_fmpz_poly,
    acb_poly_set2_fmpz_poly,
    acb_poly_set_arb_poly,
    acb_poly_set2_arb_poly,
    acb_poly_set_fmpq_poly,
    acb_poly_set2_fmpq_poly,
    acb_poly_set_acb,
    acb_poly_set_si,
    _acb_poly_majorant,
    acb_poly_majorant,
    _acb_poly_add,
    acb_poly_add,
    acb_poly_add_si,
    _acb_poly_sub,
    acb_poly_sub,
    acb_poly_neg,
    acb_poly_scalar_mul_2exp_si,
    acb_poly_scalar_mul,
    acb_poly_scalar_div,
    _acb_poly_mullow_classical,
    _acb_poly_mullow_transpose,
    _acb_poly_mullow_transpose_gauss,
    _acb_poly_mullow,
    acb_poly_mullow_classical,
    acb_poly_mullow_transpose,
    acb_poly_mullow_transpose_gauss,
    acb_poly_mullow,
    _acb_poly_mul,
    acb_poly_mul,
    _acb_poly_inv_series,
    acb_poly_inv_series,
    _acb_poly_div_series,
    acb_poly_div_series,
    _acb_poly_div,
    _acb_poly_rem,
    _acb_poly_divrem,
    acb_poly_divrem,
    _acb_poly_div_root,
    _acb_poly_taylor_shift,
    acb_poly_taylor_shift,
    _acb_poly_compose,
    acb_poly_compose,
    _acb_poly_compose_series,
    acb_poly_compose_series,
    _acb_poly_revert_series,
    acb_poly_revert_series,
    _acb_poly_evaluate_horner,
    acb_poly_evaluate_horner,
    _acb_poly_evaluate_rectangular,
    acb_poly_evaluate_rectangular,
    _acb_poly_evaluate,
    acb_poly_evaluate,
    _acb_poly_evaluate2_horner,
    acb_poly_evaluate2_horner,
    _acb_poly_evaluate2_rectangular,
    acb_poly_evaluate2_rectangular,
    _acb_poly_evaluate2,
    acb_poly_evaluate2,
    _acb_poly_product_roots,
    acb_poly_product_roots,
    _acb_poly_tree_alloc,
    _acb_poly_tree_free,
    _acb_poly_tree_build,
    _acb_poly_evaluate_vec_iter,
    acb_poly_evaluate_vec_iter,
    _acb_poly_evaluate_vec_fast_precomp,
    _acb_poly_evaluate_vec_fast,
    acb_poly_evaluate_vec_fast,
    _acb_poly_interpolate_newton,
    acb_poly_interpolate_newton,
    _acb_poly_interpolate_barycentric,
    acb_poly_interpolate_barycentric,
    _acb_poly_interpolation_weights,
    _acb_poly_interpolate_fast_precomp,
    _acb_poly_interpolate_fast,
    acb_poly_interpolate_fast,
    _acb_poly_derivative,
    acb_poly_derivative,
    _acb_poly_integral,
    acb_poly_integral,
    _acb_poly_pow_ui_trunc_binexp,
    acb_poly_pow_ui_trunc_binexp,
    _acb_poly_pow_ui,
    acb_poly_pow_ui,
    _acb_poly_pow_series,
    acb_poly_pow_series,
    _acb_poly_pow_acb_series,
    acb_poly_pow_acb_series,
    _acb_poly_sqrt_series,
    acb_poly_sqrt_series,
    _acb_poly_rsqrt_series,
    acb_poly_rsqrt_series,
    _acb_poly_log_series,
    acb_poly_log_series,
    _acb_poly_atan_series,
    acb_poly_atan_series,
    _acb_poly_exp_series_basecase,
    acb_poly_exp_series_basecase,
    _acb_poly_exp_series,
    acb_poly_exp_series,
    _acb_poly_sin_cos_series,
    acb_poly_sin_cos_series,
    _acb_poly_sin_series,
    acb_poly_sin_series,
    _acb_poly_cos_series,
    acb_poly_cos_series,
    _acb_poly_tan_series,
    acb_poly_tan_series,
    _acb_poly_sin_cos_pi_series,
    acb_poly_sin_cos_pi_series,
    _acb_poly_sin_pi_series,
    acb_poly_sin_pi_series,
    _acb_poly_cos_pi_series,
    acb_poly_cos_pi_series,
    _acb_poly_cot_pi_series,
    acb_poly_cot_pi_series,
    _acb_poly_sinh_cosh_series_basecase,
    acb_poly_sinh_cosh_series_basecase,
    _acb_poly_sinh_cosh_series_exponential,
    acb_poly_sinh_cosh_series_exponential,
    _acb_poly_sinh_cosh_series,
    acb_poly_sinh_cosh_series,
    _acb_poly_sinh_series,
    acb_poly_sinh_series,
    _acb_poly_cosh_series,
    acb_poly_cosh_series,
    _acb_poly_sinc_series,
    acb_poly_sinc_series,
    _acb_poly_lambertw_series,
    acb_poly_lambertw_series,
    _acb_poly_gamma_series,
    acb_poly_gamma_series,
    _acb_poly_rgamma_series,
    acb_poly_rgamma_series,
    _acb_poly_lgamma_series,
    acb_poly_lgamma_series,
    _acb_poly_digamma_series,
    acb_poly_digamma_series,
    _acb_poly_rising_ui_series,
    acb_poly_rising_ui_series,
    _acb_poly_powsum_series_naive,
    _acb_poly_powsum_series_naive_threaded,
    _acb_poly_powsum_one_series_sieved,
    _acb_poly_zeta_em_choose_param,
    _acb_poly_zeta_em_bound1,
    _acb_poly_zeta_em_bound,
    _acb_poly_zeta_em_tail_naive,
    _acb_poly_zeta_em_tail_bsplit,
    _acb_poly_zeta_em_sum,
    _acb_poly_zeta_cpx_series,
    _acb_poly_zeta_series,
    acb_poly_zeta_series,
    _acb_poly_polylog_cpx_small,
    _acb_poly_polylog_cpx_zeta,
    _acb_poly_polylog_cpx,
    _acb_poly_polylog_series,
    acb_poly_polylog_series,
    _acb_poly_erf_series,
    acb_poly_erf_series,
    _acb_poly_agm1_series,
    acb_poly_agm1_series,
    _acb_poly_elliptic_k_series,
    acb_poly_elliptic_k_series,
    _acb_poly_elliptic_p_series,
    acb_poly_elliptic_p_series,
    _acb_poly_root_bound_fujiwara,
    acb_poly_root_bound_fujiwara,
    _acb_poly_root_inclusion,
    _acb_poly_validate_roots,
    _acb_poly_refine_roots_durand_kerner,
    _acb_poly_find_roots,
    acb_poly_find_roots,
    _acb_poly_validate_real_roots,
    acb_poly_validate_real_roots)
