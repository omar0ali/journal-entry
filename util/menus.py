class MAIN_MENU:
    ALL_ACCOUNTS = "All Transactions"
    ACCOUNT_COMPANY = "Transactions of a company"
    All_COMPANIES = "All Companies"
    REMARKS = "Remarks"
    EXIT = "Exit"
    LIST = [
        ALL_ACCOUNTS,
        ACCOUNT_COMPANY,
        All_COMPANIES,
        REMARKS,
        EXIT
    ]
    
    
class COMPANY_MENU:
    INSERT_COMPANY = "Add Company"
    EDIT_COMPANY = "Edit Company"
    REMOVE_COMPANY = "Remove Company"
    GO_BACK = "Go Back"
    LIST = [
        INSERT_COMPANY,
        EDIT_COMPANY,
        REMOVE_COMPANY,
        GO_BACK
    ]
    
class All_TRANSACTIONS_MENU:
    INERT_TRANSACTION = "Add Record"
    EDIT_TRANSACTION = "Edit Record"
    REMOVE_TRANSACTION = "Remove Record" 
    GO_BACK = "Go Back"
    LIST = [
        INERT_TRANSACTION,
        EDIT_TRANSACTION,
        REMOVE_TRANSACTION,
        GO_BACK
    ]


class MESSAGES:
    SUCCESS_DATA_INSERTED = "Data inserted successfully!"
    SUCCESS_DATA_UPDATED = "Data updated successfully!"