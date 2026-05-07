```python
def account_opening_process(application_data):
    if is_anti_social_force(application_data.representative):
        return REJECT("Public Policy Violation")

    funding_intent = application_data.funding_intent

    if funding_intent == False:
        if check_business_reality(application_data.business_plan):
            return ISSUE_RESTRICTED_ACCOUNT(mode="Transaction_Only")
        else:
            return REJECT("Insubstantial Business")
    else:
        return traditional_comprehensive_audit(application_data)

def on_loan_request(account_id, loan_amount):
    performance_score = analyze_transaction_history(account_id)
    if performance_score > THRESHOLD:
        return APPROVE_LOAN(loan_amount)
    else:
        return REJECT("Insufficient Track Record")
