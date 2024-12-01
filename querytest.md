query BankAccounts {
    bankAccounts {
        id
        name
        bankName
        accountType
        balance
        createdAt
        updatedAt
        deletedAt
    }
}


mutation AddBankAccount {
    addBankAccount(
        name: "GOP"
        bankName: "BBVA"
        accountType: "debito"
        balance: 1.0
    ) {
        id
        name
        bankName
        accountType
        balance
        createdAt
        updatedAt
        deletedAt
    }
}
