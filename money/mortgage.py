def monthly_repayment(mortgage_amount, mortgage_length_months, interest_apr):
    monthly_interest_rate = interest_apr / 12
    monthly_interest_scale_factor = (1 + monthly_interest_rate)
    repayment_amount = (mortgage_amount * monthly_interest_scale_factor**mortgage_length_months ) / \
            sum(monthly_interest_scale_factor ** n for n in range(mortgage_length_months))
    return repayment_amount

